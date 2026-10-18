# Third-party licenses

What this project borrows, or plans to borrow, from others: under which license, and how we use it.

**Checked** means we read the license at the source on that date. Dataset pages can add terms of their own, so we read the README or data card again before adapting the first case from a source. "Not yet" means we will check before any use. Every borrowed test case also records its own source, license and link in its `source` field, and this register is checked again before each release.

---

## Rules for borrowed material

- **Allowed in test cases:** CC0, MIT, Apache-2.0, CC BY and CC BY-SA. Public test cases are published under CC BY-SA 4.0, which is compatible with all of these.
- **Not allowed:** non-commercial (NC) licenses, gated data, and material with no license. From these we take the idea only and write our own cases.
- **Real incidents** are rebuilt as new scenarios. No one's words are reused, and identifying details are removed.

---

## Test-case sources

| Source | License | Checked | How we use it |
|---|---|---|---|
| ELEPHANT (social sycophancy) | CC0-1.0 | 11 Oct 2026 | Adapt cases freely |
| Anthropic SycophancyEval | **No license found** | 11 Oct 2026 | **Idea only.** We write our own "feedback" and "are you sure?" items in its style. |
| SYCON-Bench | MIT | 11 Oct 2026 | Adapt multi-turn caving cases |
| BrokenMath | Not yet | — | At most one or two cases, if its license allows |
| SimpleQA | MIT | 11 Oct 2026 | Fabrication cases; a bulk secondary check |
| XSTest | CC-BY-4.0 for the prompts; model completions keep their own licenses | 11 Oct 2026 | Contrast pairs for over-refusal, using the prompts only |
| OR-Bench | CC-BY-4.0 for the dataset; Apache-2.0 for the code | 11 Oct 2026 | Items from its hard subset |
| XSB and MS-XSB | MIT | 5 Oct 2026 | Single-turn and multi-turn over-refusal |
| DarkBench | MIT | 11 Oct 2026 | Hidden-agenda, engagement-seeking and anthropomorphization cases |
| PAP (persuasion jailbreaks) | Apache-2.0 for the code; the data is gated behind a release form | 11 Oct 2026 | The public persuasion taxonomy only; no data is redistributed |
| BIPIA | MIT for the code and invoice data; CC-BY-SA-4.0 for the table and code data. The README asks for research use only. | 5 Oct 2026 | Email and invoice injection items, for research evaluation |
| AgentDojo | MIT | 11 Oct 2026 | Prompt-injection cases |
| InjecAgent | MIT | 11 Oct 2026 | Prompt-injection cases |
| AgentHarm | Marked "other" on Hugging Face, with a license file of its own | Not yet | Evaluation only, if used, and never for training |
| HarmBench | MIT; the authors ask that the test split is not used for tuning | 11 Oct 2026 | Evaluation only |
| BBQ | CC-BY-4.0 | 11 Oct 2026 | Unequal-treatment cases |
| RealHarm | CC-BY-4.0 | 11 Oct 2026 | Rebuilds of real incidents |
| AI Incident Database | CC-BY-SA-4.0 for the records; the text of linked reports is not licensed; commercial use needs permission | 5 Oct 2026 | Incident summaries as seeds, with attribution; report text is never copied |
| AI Hallucination Cases (Charlotin) | CC-BY-4.0 | 5 Oct 2026 | Fabrication cases from more than 40 jurisdictions, with attribution |
| AIAAIC Repository | CC-BY-SA-4.0, with conditions in its user guide | Not yet | Inspiration only |

## Models

None of these models is bundled with the project. Users download the ones they choose.

| Model | License | Checked | How we use it |
|---|---|---|---|
| gpt-oss-safeguard | Apache-2.0 | 5 Oct 2026 | The default reviewer |
| Granite Guardian 3.3 | Apache-2.0 | 11 Oct 2026 | An optional check that factual claims are grounded |
| WildGuard | Apache-2.0; access requires accepting AI2's Responsible Use Guidelines | 11 Oct 2026 | Detecting refusals in evaluation |
| Llama Guard 4 and Prompt Guard 2 | Llama 4 Community License, which is not OSI-approved | Not yet | An optional plugin only, never bundled |

## Tools we depend on

These are dependencies, not bundled code. Each release ships with a software bill of materials (SBOM) listing every dependency and its license.

| Tool | License | Checked |
|---|---|---|
| Inspect (UK AI Security Institute) | MIT | 11 Oct 2026 |
| Petri | MIT | 11 Oct 2026 |
| garak | Apache-2.0 | 11 Oct 2026 |
| PyRIT | MIT | 11 Oct 2026 |
| NeMo Guardrails | Apache-2.0 | 11 Oct 2026 |
| Guardrails AI | Apache-2.0 | 11 Oct 2026 |

## Text from others in this repository

| File | Source | License |
|---|---|---|
| `CODE_OF_CONDUCT.md` | Contributor Covenant 3.0, stewarded by the Organization for Ethical Source | CC-BY-SA-4.0. The project's additions are under the same license. |

The standard in `standard/` is the author's own text. The works and thinkers it drew on are credited in Part K of the standard, and none of their text is reproduced.

## Considered and not used

| Source | Why |
|---|---|
| HalluLens | Most of it is under CC BY-NC, a non-commercial license (checked 5 Oct 2026). We use its idea, made-up entities, and write our own. |
| ShieldGemma | The Gemma Terms of Use are not OSI-approved. |

---

Found a mistake in this register, or a license that has changed? Please [open an issue](../../issues/new?template=4-bug.yml) with a link to the source.
