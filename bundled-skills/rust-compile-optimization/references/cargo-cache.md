# Cargo cache reference

Use this file when the task needs exact Cargo behavior rather than general policy.

## Directory meanings

Cargo stores final artifacts in `target-dir` and intermediate artifacts in `build-dir`. Unless configured otherwise, both are under the workspace's `target/` directory. Typical high-volume paths include:

- `debug/deps/`: compiled dependencies and other debug artifacts;
- `debug/incremental/`: incremental compiler state;
- `debug/build/`: build-script outputs;
- `release/`: release artifacts and dependencies;
- `doc/`: generated documentation;
- target-triple subdirectories: outputs for cross-compilation.

`CARGO_TARGET_DIR`, `build.target-dir`, and `--target-dir` select the target directory. `CARGO_BUILD_BUILD_DIR` and `build.build-dir` select the intermediate build directory. Keep the two deliberately separate only when there is a concrete reason; otherwise the default is easier to reason about.

## Profiles and incremental behavior

The built-in profiles are `dev`, `release`, `test`, and `bench`. `dev` defaults to full debug info and incremental compilation; `release` defaults to no debug info and no incremental compilation. `test` inherits from `dev`, while `bench` inherits from `release`.

The `incremental` profile setting or `CARGO_INCREMENTAL=0|1` controls incremental compilation. Incremental output improves repeated workspace/path-dependency rebuilds but consumes additional disk and is not necessary for a one-shot release build.

Cargo's documented disk-saving dev profile is:

```toml
[profile.dev]
debug = "line-tables-only"

[profile.dev.package."*"]
debug = false

[profile.debugging]
inherits = "dev"
debug = true
```

This is a trade-off: smaller output and faster linking, with a less complete debugger experience for dependencies.

## Command selection

`cargo check` compiles enough to diagnose most code errors without final code generation and stores metadata for reuse. It is preferred for edit feedback, but it does not replace `cargo build`, test execution, linking, or release validation.

Use `--lib`, `--bin NAME`, `-p PACKAGE`, `--workspace`, `--all-targets`, and `--all-features` deliberately. Every additional target, package, feature combination, profile, or platform can multiply output.

## Cleaning

`cargo clean --dry-run` previews deletion. `cargo clean --release` removes release artifacts; `cargo clean --doc` removes generated docs; `cargo clean --profile NAME` removes one custom profile; plain `cargo clean` removes the entire target directory. Use `--target-dir` when the artifacts are not in the default location.

Do not use a cleanup command while a build or recursive size scan is active. Afterward, inspect the exact directory and process state instead of running a broad build that recreates the cache.

## Shared caches

Cargo already shares downloaded crate sources through `CARGO_HOME` (normally `~/.cargo`). A shared `CARGO_TARGET_DIR` can also share compatible compiled artifacts across workspaces, but fingerprints still distinguish incompatible profiles, features, toolchains, and targets. `sccache` can share compiler results across workspaces, but adds a separate cache and therefore should be used only with an explicit size/retention policy.
