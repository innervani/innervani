## What this changes

<!-- One or two sentences. Link the issue, for example: Closes #123 -->

## Type of change

- [ ] Test cases
- [ ] Standard: wording or explanation only, with no change of meaning
- [ ] Change to the core (link the accepted RFC)
- [ ] Code
- [ ] Documentation
- [ ] Other

## Checks

- [ ] Every commit is signed off (`git commit -s`), as described in CONTRIBUTING.md.
- [ ] CI passes.

**For test cases**

- [ ] Each failure case has its control twin, with the same `pair_id`.
- [ ] Every case passes `python tests/validate_cases.py` and carries the canary string.
- [ ] Borrowed material names its source and license, and nothing is non-commercial or gated.
- [ ] No personal information about real people.

**For code**

- [ ] Tests added or updated.
- [ ] Any new dependency is explained, with its license.
