# AI 测试用例生成对话记录

日期：2026-09-09

## AI Prompt（提交给 AI 的原始要求）

> 被测对象是 Arrow 1.4.0。测试范围见 `assignment/module2/scope.md`。
> 请基于以下四个功能生成不少于 15 条测试用例：
> `arrow.get()`、`.shift()`、`.format()`、`.humanize()`。
> 要求覆盖等价类、边界值和场景法，并给出预期结果。

## AI 生成的测试用例清单

| 编号 | 功能 | 用例名称 | 测试数据/输入 | 预期结果 | 设计方法 |
| --- | --- | --- | --- | --- | --- |
| AI-PARSE-001 | arrow.get | 标准 ISO 日期字符串 | `"2026-09-08"` | 格式化后仍为 `2026-09-08` | 等价类 |
| AI-PARSE-002 | arrow.get | Unix 时间戳 0 | `0` | `1970-01-01 00:00:00` | 边界值 |
| AI-PARSE-003 | arrow.get | 负时间戳 | `-1` | `1969-12-31 23:59:59` | 边界值 |
| AI-PARSE-004 | arrow.get | 带时区的 ISO 字符串 | `"2026-09-08T10:00:00+08:00"` | 保留 `+08:00` 时区偏移 | 等价类 |
| AI-PARSE-005 | arrow.get | 非法月份 | `"2026-13-01"` | 抛出 ValueError | 等价类（非法输入） |
| AI-PARSE-006 | arrow.get | 非法日期 | `"2026-02-30"` | 抛出 ValueError | 边界值（非法输入） |
| AI-PARSE-007 | arrow.get | 空字符串 | `""` | 抛出 ParserError | 边界值（非法输入） |
| AI-PARSE-008 | arrow.get | None 输入 | `None` | 抛出 TypeError | 等价类（非法输入） |
| AI-SHIFT-001 | shift | 非闰年 2 月加一天 | `2026-02-28`, `days=1` | `2026-03-01` | 边界值 |
| AI-SHIFT-002 | shift | 闰年 2 月加一天 | `2024-02-28`, `days=1` | `2024-02-29` | 边界值 |
| AI-SHIFT-003 | shift | 元旦前一天 | `2026-01-01`, `days=-1` | `2025-12-31` | 边界值 |
| AI-SHIFT-004 | shift | 月末加一个月 | `2026-01-31`, `months=1` | `2026-02-28`（月末收拢） | 边界值/场景 |
| AI-SHIFT-005 | shift | 加 12 个月跨年 | `2026-03-15`, `months=12` | `2027-03-15` | 等价类/场景 |
| AI-SHIFT-006 | shift | 非法时间单位 | `decades=1` | 抛出 ValueError | 等价类（非法输入） |
| AI-FORMAT-001 | format | 基础日期格式 | `YYYY-MM-DD` | `2026-09-08` | 等价类 |
| AI-FORMAT-002 | format | 完整星期与月份 | `dddd, DD MMMM YYYY` | `Tuesday, 08 September 2026` | 等价类/场景 |
| AI-FORMAT-003 | format | 日期时间格式 | `YYYY-MM-DD HH:mm:ss` | `2026-09-08 09:30:15` | 等价类 |
| AI-FORMAT-004 | format | 月/日格式 | `MM/DD` | `12/25` | 等价类 |
| AI-HUMAN-001 | humanize | 过去 3 天 | 基准时间前 3 天 | `3 days ago` | 场景法 |
| AI-HUMAN-002 | humanize | 未来 3 天 | 基准时间后 3 天 | `in 3 days` | 场景法 |
| AI-HUMAN-003 | humanize | 同一日历月内相差 16 天 | 基准时间后 16 天 | `in 2 weeks`（怀疑缺陷） | 边界值 |

## 人工/AI 核验结果

- AI-PARSE-001 至 AI-FORMAT-004：已用 Arrow 1.4.0 实际运行核对，预期正确。
- AI-HUMAN-001、002：运行结果正确。
- AI-HUMAN-003：Arrow 1.4.0 实际输出 `in a month`，与预期 `in 2 weeks` 不一致。
  该问题与 GitHub issue #1240 描述一致，暂记为疑似缺陷，进入缺陷分析流程。
