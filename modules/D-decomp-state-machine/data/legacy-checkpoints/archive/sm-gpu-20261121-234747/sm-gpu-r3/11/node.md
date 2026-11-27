# N158: 在无硬性延迟约束下，衡量性价比的核心指标定义为 $/Token（美元/令牌），计算公式为 TCO_annual / Total_Tokens_Generated

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在无硬性延迟约束下，衡量性价比的核心指标定义为 $/Token（美元/令牌），计算公式为 TCO_annual / Total_Tokens_Generated_Annual；对于单用户本地工作站场景，需引入'每瓦特吞吐量'（Tokens/s/W）作为能效辅助指标，以区分高功耗低吞吐方案与低功耗高吞吐方案（如 Apple Silicon vs RTX 4090）

## Corrected Claim

在无硬性延迟约束下，衡量性价比的核心指标定义为 $/Token（美元/令牌），计算公式为 TCO_annual / Total_Tokens_Generated_Annual；对于单用户本地工作站场景，需引入'每瓦特吞吐量'（Tokens/s/W）作为能效辅助指标，以区分高功耗低吞吐方案与低功耗高吞吐方案（如 Apple Silicon vs RTX 4090）

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的分子（TCO）、分母（Total Tokens）以及辅助能效指标（Tokens/s/W），逻辑上互斥且无重复。它们共同构成了父节点定义的完整计算框架，没有遗漏关键组成部分，也不存在可合并的冗余参数。）
