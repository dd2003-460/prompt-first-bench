# N383: 工作点C（混合-中等Opex）：5个自建POP+5个公有云，C_opex = C_bw_self(¥25,000) + C_bw_cloud(¥30,000) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

工作点C（混合-中等Opex）：5个自建POP+5个公有云，C_opex = C_bw_self(¥25,000) + C_bw_cloud(¥30,000) + C_eng(¥100,000，3人) + C_power(¥2,592) + C_colocation(¥3,750) = ¥161,342/月，比全自建低24%，比全公有云高47%，但P99延迟更优。

## Corrected Claim

工作点C（混合-中等Opex）：5个自建POP+5个公有云，C_opex = C_bw_self(¥25,000) + C_bw_cloud(¥30,000) + C_eng(¥100,000，3人) + C_power(¥2,592) + C_colocation(¥3,750) = ¥161,342/月，比全自建低24%，比全公有云高47%，但P99延迟更优。

## Evidence

先验知识/题面给定，逻辑校验通过：各项成本加和（25000+30000+100000+2592+3750=161342）计算正确，且作为混合架构，其成本介于全自建与全公有云之间符合经济直觉，延迟优于纯公有云符合物理规律。
