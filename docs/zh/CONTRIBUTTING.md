## 贡献须知
1. 签署开发者协议（签署链接）
2. 所有PR必须包含：
   - 中英双语文档更新
   - 单元测试覆盖率 ≥80%
3. 代码风格要求：
   ```bash
   black . --line-length 120
   flake8 --max-line-length=120
   
#### (2) 自动化检查
`.github/workflows/ci.yml`示例：
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