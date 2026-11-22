# N42: 平台打破信号机制的反事实量化：若移除价格-质量相关性权重，高挂价商品成交周期 $T_{new}$ 将延长。基于搜索匹配摩擦，假设原周期 $T_{old}=10$

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

平台打破信号机制的反事实量化：若移除价格-质量相关性权重，高挂价商品成交周期 $T_{new}$ 将延长。基于搜索匹配摩擦，假设原周期 $T_{old}=10$ 天，信号移除后买家搜索成本增加，$T_{new} = T_{old} \times (1 + \gamma)$，其中 $\gamma$ 为信号缺失导致的搜索效率损失系数（假设0.3），则 $T_{new}=13$ 天，延长30%。

## Corrected Claim

平台打破信号机制的反事实量化：若移除价格-质量相关性权重，高挂价商品成交周期 $T_{new}$ 将延长。基于搜索匹配摩擦，假设原周期 $T_{old}=10$ 天，信号移除后买家搜索成本增加，$T_{new} = T_{old} \times (1 + \gamma)$，其中 $\gamma$ 为信号缺失导致的搜索效率损失系数（假设0.3），则 $T_{new}=13$ 天，延长30%。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 28 (char 93)

## Search Query

counterfactual analysis removing price quality signal effect on transaction time
