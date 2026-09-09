# 缺陷报告：AI-DEFECT-001

## 基本信息

- 缺陷标题：`humanize()` 将同一日历月内 16 天的时间差报告为 “in a month”
- 被测对象：Arrow 1.4.0
- 被测模块：`Arrow.humanize()`（auto granularity）
- 发现方式：AI 生成测试用例 AI-HUMAN-003 后执行 pytest 发现
- 关联用例：AI-HUMAN-003
- 严重程度：中（输出不符合用户直觉，会造成误导）

## 缺陷现象

在同一日历月内，两个时间点相差 16 天时，`humanize()` 输出 `in a month`；
按用户预期（GitHub issue #1240），16 天更接近“两周”，应输出 `in 2 weeks`。

## 复现步骤

在 Arrow 1.4.0 环境中执行：

```python
import arrow

base = arrow.get("2026-01-09T00:00:00+00:00")
print(base.shift(days=16).humanize(base))
```

## 预期结果与实际结果

| 项目 | 内容 |
| --- | --- |
| 预期结果 | `in 2 weeks` |
| 实际结果 | `in a month` |

## 原因分析

`Arrow.humanize()` 位于 `arrow/arrow.py` 的自动粒度选择逻辑中。

原逻辑大约如下：

```python
if calendar_diff.days > 14:
    calendar_months += 1
```

这段代码无条件把“超过 14 天的剩余天数”进位成 1 个月，即使此时**尚未跨过任何完整的日历月**（即 `calendar_months == 0`）。因此同一月内 16 天的差值也会被升级成 `a month`。

此外，`weeks` 判断分支位于 `months` 分支之后，导致同一月内 15–30 天左右的差值在进位后永远走不到“周”的分支。

## 修复思路

1. 只有当至少已经跨过 1 个完整日历月（`calendar_months >= 1`）时，才根据剩余天数进行月份进位；
2. 对未跨月的差值，让“周”的判断先于“月”的判断执行。

## 修复验证

- 修复分支：`fix/ai-defect-001-humanize-16-days`
- 验证方式：修复后在仓库根目录执行 `python -m pytest -v`
- 期望结果：AI-HUMAN-003 由失败变为通过，其余用例不回归
