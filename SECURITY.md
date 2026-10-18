# Security policy

This project builds a reviewer that other systems may rely on, so a way to fool it is a security problem, not just a bug. Please report it privately, so that it can be fixed before it is used against anyone.

---

## Report privately

- **Fooling the reviewer.** A draft, conversation or document that makes the conscience layer return the wrong verdict through text aimed at the reviewer: hidden instructions, flattery of the reviewer, fake "approved" markers, or arguments for passing a draft that clearly fails. A PASS for a fabricated answer, or a DECLINE for a harmless request, both count.
- **Getting around a commitment.** A repeatable way to get output that breaks one of the six commitments (C1–C6) past the layer.
- **Tampering.** Running an altered or unverified runtime pack without the fingerprint check noticing, or forging or changing verdicts or the audit log.
- **Leaks.** Personal data exposed through the audit log, the proxy or error messages; credentials or keys; or any part of the private holdout test set.
- **Software vulnerabilities** in the engine, the proxy, the command-line tool or the release process, such as injection, server-side request forgery, unsafe deserialization, or a vulnerable dependency we ship.

## Report in public instead

- **A verdict you disagree with**, where no one tried to fool the reviewer: [propose a test case](../../issues/new?template=1-test-case.yml). Disagreement is how the standard improves.
- **A failure of an AI model itself**, such as flattery or a made-up fact: [report an AI failure](../../issues/new?template=2-ai-failure.yml). A jailbreak of a vendor's model, rather than of our reviewer, belongs with that vendor.
- **Other bugs** that affect neither safety nor security.

If you're unsure, report privately. It is easy to make a private report public, and impossible to do the reverse.

---

## How to report

Use GitHub's private vulnerability reporting: open the **Security** tab of this repository and choose **Report a vulnerability** ([direct link](https://github.com/innervani/innervani/security/advisories/new)). If you can't use GitHub, email **security@innervani.org**.

Please include:

1. **What you did**, step by step, with the exact inputs: the conversation, the draft and any documents.
2. **The versions:** the engine version, the runtime pack fingerprint, and the reviewer model and its settings.
3. **What happened**, and what should have happened.
4. **How often it works**, for example 7 runs out of 10, since model outputs vary.

Please leave out personal data about real people. If a real conversation is involved, rebuild it with invented details.

---

## What happens next

| Step | Target |
|---|---|
| We acknowledge your report | Within 5 working days |
| We tell you whether it is in scope, and how severe we think it is | Within 15 working days |
| A fix or mitigation for a confirmed issue | Within 90 days, with the timing agreed with you |
| Public disclosure | When the fix is released, or after 90 days, whichever comes first, unless we agree otherwise |

The project is run by a small team, so these are targets rather than guarantees. We will keep you informed either way.

## What we do with what you find

- **Credit.** Reporters are credited in the security advisory and the release notes, by name or anonymously, as they prefer.
- **New tests.** With your permission, an attack on the reviewer becomes a test case in our reviewer-manipulation track. It stays private until the fix ships.
- **Published rates.** Every results release reports how often attacks on the reviewer succeed, including attacks we have not yet fixed.

---

## Supported versions

Until the first release, v0.1 (planned for January 2027), only the `main` branch is supported. After that, the latest release is supported; please upgrade before reporting an issue in an older one.

## Good-faith research

We welcome security research done in good faith. Please:

- test only against your own installation, models and accounts;
- never access, change or delete other people's data, or degrade services that others rely on;
- give us a reasonable time to fix an issue before you disclose it.

If you follow this policy, we will treat your research on this project as authorized and will not pursue or support legal action against you for it. We cannot authorize testing of anyone else's systems, including deployments of this project that others run.

## What the layer is not

The conscience layer reviews AI responses for failures of character, such as flattery, fabrication and caving under pushback. It does not replace a filter for harmful content, or the security of the application around it.
