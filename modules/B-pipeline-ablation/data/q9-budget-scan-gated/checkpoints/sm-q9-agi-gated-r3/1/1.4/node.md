# N10: MTP×4 投机解码的接受率（acceptance rate）在长上下文（>32k tokens）场景下预计降至 60-75%，导致实际加速比从理论 4x 衰减

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

MTP×4 投机解码的接受率（acceptance rate）在长上下文（>32k tokens）场景下预计降至 60-75%，导致实际加速比从理论 4x 衰减至 2.5-3x；瓶颈在于 draft model 在长距离依赖上的预测置信度下降

## Corrected Claim

MTP×4 投机解码在长上下文（>32k tokens）场景下，由于 draft model 在长距离依赖上的预测置信度下降，接受率通常会显著低于短上下文场景，导致实际加速比低于理论上限（4x），具体数值取决于模型架构和数据分布。

## Evidence

[质询]具体数值区间（60-75%接受率，2.5-3x加速比）缺乏通用基准支持，不同模型架构和任务分布下波动极大，属于特定实验条件下的经验数据而非普适规律。 | 先验知识/题面给定，逻辑校验通过：长上下文导致注意力分散和KV Cache压力增加，确实会降低Draft Model的置信度和接受率，从而降低实际加速比，方向正确但具体数值需视具体实现而定。
