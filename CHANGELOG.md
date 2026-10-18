# Changelog

All notable changes to innerVANI are recorded here, newest first, in the format of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Each part has its own version number, starting at 0.1: the standard, the runtime pack, the test suite, and the engine, which uses [semantic versioning](https://semver.org/spec/v2.0.0.html). Versions go up when a part is released, not with every commit, and changes in between are listed under Unreleased. The rules are in [GOVERNANCE.md](GOVERNANCE.md#versioning).

## [Unreleased]

Work towards the first release, v0.1, planned for January 2027.

### Added

- **Standard v0.1**, the first public edition of the Conscience Foundation, approved on 11 October 2026: five premises, six commitments, thirteen principles, the conscience questions, 18 failure modes, six scope rules and 14 test cases. From this edition on, changes go through the process in part J2 of the standard. ([standard/foundation_v0.1.md](standard/foundation_v0.1.md))
- **Runtime pack v0.1**, frozen, with the fingerprint `7f0a1936a3528242`. ([standard/runtime_pack_v0.1.md](standard/runtime_pack_v0.1.md))
- **The test-case format**: a schema, a template and a checker for two-sided cases, in which every failure case is paired with a control twin. Cases about agents can list the tools the AI can call and fix an action for the conscience to review before it runs. ([tests/](tests/))
- **28 seed test cases**: the standard's 14 test cases, each with its control twin. ([tests/public/](tests/public/))
- **How the project runs**: the contributing guide, governance, code of conduct, security policy, roadmap, contributors list and register of third-party licenses, with templates for issues and pull requests.
- **Automatic checks** on every pull request and every change to `main`: the runtime pack's fingerprint, the test cases and the license of every file, plus, for pull requests, a sign-off on every commit.
- **License texts and a citation file**: the full license texts in `LICENSES/`, the license of every file in `REUSE.toml`, this changelog, and `CITATION.cff`.

[Unreleased]: https://github.com/innervani/innervani/commits/main
