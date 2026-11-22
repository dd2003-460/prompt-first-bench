# N116: INT4 精度在消费级硬件上的可行性阈值：定义在 RTX 4090 上运行 INT4 Qwen3-27B 时，若 HumanEval 分数下降 >5 分或 MM

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

INT4 精度在消费级硬件上的可行性阈值：定义在 RTX 4090 上运行 INT4 Qwen3-27B 时，若 HumanEval 分数下降 >5 分或 MMLU 下降 >3 分，则视为‘不可接受’，需回退至 INT8 或 FP8 的具体判定逻辑

## Corrected Claim

在 RTX 4090 上运行 INT4 Qwen3-27B 时，若 HumanEval 分数下降超过 5 分或 MMLU 下降超过 3 分，通常被视为精度损失不可接受，需回退至 INT8 或 FP8（注：具体阈值依应用场景而定，此处为示例性判定逻辑）。

## Evidence

[质询]该陈述定义了一个具体的工程判定阈值（HumanEval下降>5分或MMLU下降>3分），但缺乏行业公认的标准或权威来源支持这一特定数值组合的普适性，属于特定场景下的经验性设定而非通用事实。 | 先验知识/题面给定，逻辑校验通过；但作为具体数值阈值，缺乏外部来源直接支持，且属于经验性工程决策标准，故降级。
