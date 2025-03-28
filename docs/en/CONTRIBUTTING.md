## Contribution Notice
1. Sign the Developer Agreement (sign the link)
2. All PRs must contain:
- Bilingual documentation updates in English and Chinese
- Unit test coverage ≥80%
3. Code style requirements:
```bash
black . --line-length 120
flake8 --max-line-length=120


#### (2) Automated checks
'.github/workflows/ci.yml' example:
```yaml
name: CI
on: [push, pull_request]

jobs:
license-check:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v3
- name: Verify License Headers
uses: google/new-project-license-check@v1
with:
license: "AGPL-3.0"
paths: autotrain/**.py