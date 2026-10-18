# Governance

How decisions are made in this project, who makes them, and how the core standard can change.

---

## Mission

Build an open, model-agnostic conscience layer for AI assistants, based on a public standard that states its reasons, and show in the open whether it works.

## Principles behind every decision

- **Measure both directions.** Any drop in a failure is reported together with any rise in over-correction.
- **Reasons must be real.** Cited principles are tested for faithfulness, not assumed.
- **Publish what fails.** Negative results are published with the positive ones.
- **Reasons over authority.** Every principle states why it holds. Sources are credited, never relied on.
- **Small, stable core.** The core changes only through review, never in response to a single result.
- **Any model.** Every component can run on open-weight models, offline.

---

## Roles

| Role | Who | Responsibilities |
|---|---|---|
| **Project lead** | The founder | Final decisions until a steering group forms; stewardship of the standard; releases |
| **Maintainers** | Contributors invited after sustained, high-quality work | Review and merge; triage; uphold this document |
| **Area leads** | Maintainers responsible for the standard, evaluation, or the engine | The roadmap and reviews for their area |
| **Contributors** | Anyone who opens an issue, a discussion or a pull request | Following the [code of conduct](CODE_OF_CONDUCT.md) |
| **Outside readers** | People from a different cultural and philosophical background than the authors, invited for each review of the core | Reviewing proposed changes to the core |
| **Raters** | Invited for labelling and blind rating | Independent labels; confidentiality for the private holdout |
| **Community Moderators** | Three people independent of the project lead, named in the [code of conduct](CODE_OF_CONDUCT.md): one for now, with two more planned before the first release. New moderators are chosen by the existing moderators with the project lead, and the lead cannot remove a moderator alone. | Handling conduct reports. Until there are three moderators, the moderator and the project lead handle reports together, and reports about the lead go to the moderator alone. Once there are three, suspensions and bans need two of the three to agree, and the project lead carries out their decisions without overruling them |

---

## How decisions are made

1. **Everyday changes** (test cases, documentation, small code changes): a pull request with passing checks and approval from at least one maintainer. Anyone may raise an objection during review.
2. **Larger changes** (new features, architecture, new packs, new dependencies, anything touching licenses): an issue or discussion first, then maintainer consensus. If consensus fails, the project lead decides and records why.
3. **Changes to the core:** the RFC process below.
4. **Records:** every decision beyond everyday changes is recorded in `docs/decisions/`, one short file each, giving the context, the decision and its consequences.

---

## The core, and how it changes

**The core** is the six commitments (C1–C6), the five premises (M1–M5), the runtime pack (which also holds the principles, questions and scope rules) and the verdict format.

**The RFC process**, from Part J2 of [the standard](standard/foundation_v0.1.md):

1. **Proposal.** Open an issue labelled `rfc` with the change, the reasoning, and the test cases it affects.
2. **Comment period.** At least 14 days.
3. **Review.** By at least one engineer, the evaluation lead, and one outside reader from a different cultural and philosophical background.
4. **Evidence.** The test suite is run before and after the change on at least two different AI models, and the results are published.
5. **Decision.** Accepted, or closed with reasons, and recorded in `docs/decisions/`.
6. **Release.** A new version number. Any change to the runtime pack produces a new fingerprint, which CI checks.

Nothing said in a live conversation can trigger a change, and no single result is a reason to change the core.

Other parts of the standard, such as explanations, examples and the "why it holds" lines, change through normal review, provided the meaning of the core does not change. Any change of meaning goes through the RFC process.

---

## Versioning

Every part of the project has its own version number, starting at 0.1. Below 1.0, a part is still being proven and may change; it reaches 1.0 once it has been validated. Versions go up when a part is released, not with every commit; changes in between are listed under "Unreleased" in [CHANGELOG.md](CHANGELOG.md).

| What | Scheme |
|---|---|
| **Engine** | [Semantic versioning](https://semver.org), starting at 0.1.0 |
| **Standard** | Before 1.0, a change of meaning to the core raises the second number (0.1 to 0.2), and a change of wording or explanation adds a third (0.1 to 0.1.1). From 1.0, a change of meaning raises the first number (1.0 to 2.0), and a change of wording the second (1.0 to 1.1). |
| **Runtime pack and test suite** | Separate version lines starting at 0.1, each with a SHA-256 fingerprint. Any change to the pack is a new version. |
| **Releases** | Each release states the standard, pack and suite versions it was tested with |

---

## Evaluation integrity

- **Pre-registration.** Targets and analysis plans are committed before any layer runs, and are not changed afterwards.
- **The holdout.** A small private set of cases is run once per release and rotated every year. Access is limited to named maintainers and raters.
- **No training on the tests.** Results from models trained on the suite are invalid. Every public case carries a canary string for filtering.
- **Full results.** Every result is published with its configuration, model versions, failures, cost and latency.

## Conflicts of interest

Maintainers, reviewers and moderators disclose any affiliation with AI developers or vendors whose models are evaluated, and step back from decisions where they have a conflict. Funding sources are listed publicly. Early partners, the teams that try pre-release versions of the engine, help shape its practical design but have no special say over the core: their proposals for it go through the RFC process like anyone else's. They are named only with their permission.

## Responsible use

The project will not accept features designed to suppress lawful speech or to impose one worldview. Helping is the default (S5), and legitimate aims are respected (S4).

---

## Becoming a maintainer

- **Criteria:** about three months of sustained contributions (test cases, reviews, code or documentation), sound judgment in review, and respect for the code of conduct.
- **Process:** nomination by a maintainer and approval by the project lead, or by the steering group once it exists.
- **Stepping back:** maintainers inactive for six months become emeritus, and can return at any time.

## Steering group

When the project has at least three active maintainers, expected after the v0.1 release, the project lead will propose a steering group of three to five people. At least one member will come from a different cultural and philosophical background than the founder.

---

## Code of conduct

The project follows the [code of conduct](CODE_OF_CONDUCT.md). Reports go to the address given there. Until there are three Community Moderators, the moderator and the project lead handle them together, and reports about the lead go to the moderator alone. People involved in an incident take no part in handling it.

## Security

Ways to fool the reviewer are security issues. Report them privately, as described in [SECURITY.md](SECURITY.md). Reporters are credited.

## Changing this document

Open a pull request labelled `governance`. Changes need a 14-day comment period and approval by the project lead, or by the steering group once it exists.
