---
name: rust-compile-optimization
description: Optimize Rust/Cargo compilation for bounded disk usage and predictable
  rebuilds. Use when Rust projects accumulate huge target, deps, incremental, debug-symbol,
  test, documentation, or cross-target artifacts; when choosing between cargo check,
  build, test, release, or workspace/target selection; when configuring shared Cargo
  caches, target directories, profiles, sccache, or safe cleanup; or when diagnosing
  a disk-space problem caused by Rust builds.
---

# Rust Compile Optimization

## Objective

Keep Rust compilation useful while preventing `target/` and related caches from silently consuming many gigabytes. Preserve correctness and the user's required validation scope. Treat compiled artifacts as disposable, but treat source data, experiment outputs, databases, credentials, and manually stored binaries as non-disposable unless explicitly in scope.

## Non-negotiable safety rules

- Inspect before mutating: identify the manifest/workspace, active Cargo configuration, target directory, profiles, target triples, running Cargo/rustc processes, and the size of the candidate paths.
- Never delete a whole home directory, workspace, or broad cache recursively. Resolve exact paths first.
- Do not run a broad rebuild merely to verify a cleanup; `cargo check --all-targets` or a full workspace build can recreate gigabytes.
- Do not remove `data/`, research/replay outputs, runtime state, databases, credentials, cookies, or session files just because they are ignored by Git.
- Never disable incremental compilation blindly when fast edit/rebuild latency is the priority. It is a disk-versus-rebuild-time trade-off.
- Keep release verification explicit. If the user asks for tests, features, targets, bins, or locked/offline behavior, preserve those constraints.
- Before deleting artifacts, stop or account for active `cargo`, `rustc`, `rustdoc`, linker, and size-scan processes. Concurrent builds can make a cleanup appear ineffective or race with it.

## Decision workflow

### 1. Establish scope and baseline

Start from the exact manifest or project named by the user. For a read-only diagnosis, run the bundled report when available:

```sh
<BUILD_ANYTHING_DIR>/bundled-skills/rust-compile-optimization/scripts/target-report.sh [project-or-target-dir]
```

Then inspect only the relevant configuration and process state:

```sh
rg -n "target-dir|build-dir|incremental|profile\\.|CARGO_TARGET_DIR|CARGO_INCREMENTAL|RUSTC_WRAPPER" \\
  Cargo.toml .cargo/config.toml ~/.cargo/config.toml 2>/dev/null
ps aux | rg '[c]argo|[r]ustc|[r]ustdoc|[l]ld|[c]lang|[d]u ' || true
```

If the project is a workspace, prefer the workspace root and measure the shared output once. Record whether the growth is from debug/test artifacts, release artifacts, multiple target triples, docs, or incremental state.

### 2. Select the smallest sufficient Cargo command

Use the narrowest command that answers the user's need:

| Need | Preferred command |
| --- | --- |
| Compiler feedback while editing | `cargo check --lib` or `cargo check --bin NAME` |
| One package in a workspace | `cargo check -p PACKAGE` or the corresponding targeted test/build |
| One binary | `cargo check --bin NAME` / `cargo build --bin NAME` |
| Run the application locally | `cargo run --bin NAME` |
| Run tests for one package/target | `cargo test -p PACKAGE --lib` or targeted test selection |
| Produce the executable users will run | `cargo build --release --bin NAME` |
| Full validation | Use `--workspace`, `--all-targets`, `--all-features`, `--locked` only when the requested contract requires them |

`cargo check` skips final code generation and is normally smaller and faster than `cargo build`, but it does not replace a requested build or release/test validation. Avoid `--all-targets` and `--all-features` for ordinary edit feedback unless they are part of the task.

### 3. Apply configuration at the right scope

Use project `.cargo/config.toml` when the policy belongs to one repository. Use the user's global Cargo config only for a deliberate personal default that is safe across all projects. Prefer an explicit `CARGO_TARGET_DIR` or `--target-dir` for temporary isolation.

A practical personal default is one shared target directory outside individual repositories, which prevents every checkout from holding its own duplicate dependency artifacts:

```toml
# ~/.cargo/config.toml
[build]
target-dir = "/path/to/user-owned/cargo-target"
```

On another machine, replace the absolute path with a user-owned cache path. A shared target directory reduces duplication across projects, but Cargo fingerprints include build settings and dependency features; incompatible projects still create separate artifacts. Do not share one target directory between simultaneous incompatible toolchains or workflows if it causes lock contention or confusing rebuilds.

For a one-off command, avoid persistent configuration:

```sh
CARGO_TARGET_DIR="${TMPDIR:-/tmp}/cargo-target" cargo check --lib
```

### 4. Control incremental compilation intentionally

Cargo's default `dev` profile has incremental compilation enabled; `release` defaults to it disabled. Incremental state is primarily useful for repeated edits to workspace members and path dependencies. It can become large in long-lived debug builds.

Use this policy:

- Keep incremental enabled for an actively edited project when rebuild latency matters.
- Disable it for CI, one-shot builds, large batch/replay jobs, or disk-constrained release-like checks.
- Prefer a local project policy or command-scoped `CARGO_INCREMENTAL=0`; do not globally force it off without checking the user's workflow.

Examples:

```sh
CARGO_INCREMENTAL=0 cargo check --workspace --locked
CARGO_INCREMENTAL=0 cargo test --lib --locked
CARGO_INCREMENTAL=0 cargo build --release --locked
```

When debugging a large project, reduce debug information rather than disabling every useful cache. A reasonable project-level option is:

```toml
[profile.dev]
debug = "line-tables-only"

[profile.dev.package."*"]
debug = false

[profile.debugging]
inherits = "dev"
debug = true
```

Explain that this reduces disk use and link time but makes dependency debugging less rich. Use `--profile debugging` only when that extra information is needed. Do not add `strip`, `lto`, `panic = "abort"`, or unusual codegen settings merely to save build-cache space without checking runtime, debugging, and deployment requirements.

### 5. Reduce artifact multiplication

- Avoid alternating unnecessary `cargo build`, `cargo test`, `cargo doc`, multiple feature sets, and multiple target triples in the same long-lived target directory.
- Select one package, library, binary, example, or target where possible.
- Use `cargo doc --no-deps` when dependency documentation is not required.
- Keep `Cargo.lock` and use `--locked` for deterministic builds/CI; this does not by itself reduce artifacts, but prevents accidental dependency-resolution churn.
- Review unused dependencies/features periodically. Removing real dependency and feature bloat reduces compilation work, but do not remove them based only on an automated false positive.
- Consider `sccache` only when repeated builds across workspaces justify its extra cache footprint. It trades disk for rebuild speed; configure and cap/clean it deliberately rather than adding it automatically.

### 6. Clean narrowly and verify without rebuilding

Preview first:

```sh
cargo clean --dry-run
cargo clean --dry-run --release
cargo clean --dry-run --doc
```

Use the smallest cleanup that matches the request:

```sh
cargo clean --release       # release artifacts only
cargo clean --doc           # generated docs only
cargo clean --profile NAME  # one custom profile
cargo clean                 # entire target directory, only with explicit scope
```

For a target directory managed outside the project, pass `--target-dir` or use the same `CARGO_TARGET_DIR` that created it. Never manually delete `deps` or `incremental` while Cargo is running. After cleanup, verify the exact path and process state (`du -sh`, `find`/directory listing, and `ps`), not by launching a broad Cargo command.

## Recommended default policy

For most personal macOS Rust work:

1. Share a user-owned `CARGO_TARGET_DIR` across ordinary projects to avoid duplicate dependency artifacts.
2. Use `cargo check --lib` or `--bin NAME` during edits.
3. Keep dev incremental only for actively edited projects; use `CARGO_INCREMENTAL=0` for batch/CI/one-shot work.
4. Limit dev debug info and dependency debug info when full debugger detail is not needed.
5. Build/test only the requested package/target; reserve all-targets/all-features for explicit validation.
6. Run `cargo clean --dry-run` first and use `cargo clean --release`, `--doc`, or `--profile` before considering a full clean.
7. Re-measure and report exactly what was removed, what remains, and whether any rebuild was intentionally avoided.

## Reporting requirements

State:

- the target/build directory and before/after size when measured;
- which profile(s), targets, and commands were involved;
- whether incremental compilation was kept, disabled, or cleaned;
- whether the change is project-local, command-scoped, or global;
- the validation actually run and any validation deliberately not run because it would rebuild the cache.

Do not claim that a target directory will stay below a fixed number of gigabytes: dependency graph, features, profiles, platforms, compiler versions, and source size determine the result. Report the trade-off between disk use and rebuild time.

## References

- For Cargo cache layout, target/build directories, incremental artifacts, and shared `sccache`, read [references/cargo-cache.md](references/cargo-cache.md).
- For the deterministic diagnostic helper, use `scripts/target-report.sh`.
