# 软件测试实践作业仓库

本仓库用于完成《软件测试与质量保证实践》小组实践作业，采用“模块二：AI 测”方案。

## 被测对象

- 项目：Arrow（Python 日期时间处理库）
- 被测版本：`1.4.0`（Git tag：`1.4.0`）
- 上游地址：https://github.com/arrow-py/arrow

Arrow 的源码位于仓库根目录 `arrow/` 下，作为被测对象基线，原则上不修改；小组自己的测试、报告和 AI 对话记录统一放在 `assignment/` 下。

## 目录结构

```text
assignment/
  module2/
    tests/           # AI 生成并人工核对的 pytest 测试
    test_cases/      # 附录 1：AI 生成测试用例清单（Excel）
    reports/         # 附录 4：模块二测试报告（Word）等交付材料
    ai_dialogues/    # 关键 AI 对话记录
arrow/               # 被测对象 Arrow 源码（固定 1.4.0）
```

## 环境配置

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r assignment/requirements.txt
```

## 运行测试

在仓库根目录执行：

```bash
python -m pytest assignment/module2/tests -v
```

## Git 分支约定

- `assignment`：小组作业主分支，基于 Arrow `1.4.0`。
- 每个缺陷的修复在单独分支上进行，例如 `fix/defect-001`。
