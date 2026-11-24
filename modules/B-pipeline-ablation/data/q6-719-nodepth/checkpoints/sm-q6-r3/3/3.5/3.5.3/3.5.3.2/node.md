# N265: 混合策略等效成本指数 b_hybrid 的计算公式为 b_hybrid = (Core_Traffic_Ratio × b_self_core + Long_T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

混合策略等效成本指数 b_hybrid 的计算公式为 b_hybrid = (Core_Traffic_Ratio × b_self_core + Long_Tail_Traffic_Ratio × b_cloud) / (Core_Traffic_Ratio + Long_Tail_Traffic_Ratio)，其中 b_self_core 在核心流量段接近 0（固定成本已摊销），b_cloud 为公有云边际成本弹性（通常 <1）

## Corrected Claim

混合策略等效成本指数 b_hybrid 的计算公式为 b_hybrid = (Core_Traffic_Ratio × b_self_core + Long_Tail_Traffic_Ratio × b_cloud) / (Core_Traffic_Ratio + Long_Tail_Traffic_Ratio)，其中 b_self_core 在核心流量段接近 0（固定成本已摊销），b_cloud 为公有云边际成本弹性（通常 <1）

## Evidence

先验知识/题面给定，逻辑校验通过：公式为标准的加权平均成本计算，量纲一致（成本/流量），且符合混合云架构中核心流量固定成本摊销后边际成本趋近于0、长尾流量使用公有云边际成本的经济直觉。

## Search Query

hybrid CDN cost elasticity index calculation formula
