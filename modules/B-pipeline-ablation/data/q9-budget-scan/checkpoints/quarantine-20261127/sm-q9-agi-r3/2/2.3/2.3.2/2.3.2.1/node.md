# N131: Blocked 分支的定义需量化：当 Self-Consistency 一致率 < 0.5 或 连续 2 次工具调用解析失败时标记为 Blocked；在科研任务

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

Blocked 分支的定义需量化：当 Self-Consistency 一致率 < 0.5 或 连续 2 次工具调用解析失败时标记为 Blocked；在科研任务中，'假设生成'阶段的 Blocked 率通常高于 '数据分析' 阶段，若全局 Blocked 率 > 20% 且 '假设生成' 子项 Blocked 率 > 30%，则优先触发云端假设生成而非整个任务升级。

## Corrected Claim

Blocked 分支的定义需量化：当 Self-Consistency 一致率低于设定阈值（如 0.5）或连续多次工具调用解析失败时标记为 Blocked；在科研任务中，'假设生成'阶段的 Blocked 率通常高于 '数据分析' 阶段，若全局 Blocked 率超过预设警戒线（如 20%）且 '假设生成' 子项 Blocked 率显著偏高（如 > 30%），则优先触发云端假设生成而非整个任务升级。

## Evidence

[质询]该陈述包含具体的经验阈值（一致率<0.5、连续2次失败、Blocked率>20%/30%）及特定场景下的统计规律（假设生成阶段Blocked率高于数据分析阶段），这些属于经验事实而非第一性原理可推导内容，缺乏通用标准或权威来源支持其普适性。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但涉及具体经验参数与统计规律，非纯逻辑/数学推导，故降级）
