# N371: 核心区域（一二线）流量权重 w_core 的精确计算：w_core = 0.6（基于 N14 给定地理分布，60% 用户位于一二线城市），该参数直接决定混合策略

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N118

## Claim

核心区域（一二线）流量权重 w_core 的精确计算：w_core = 0.6（基于 N14 给定地理分布，60% 用户位于一二线城市），该参数直接决定混合策略中自建部分对总命中率的贡献比例，若实际分布偏离 60%（如 50%-70%），CHR_hybrid 将线性变化，敏感度 dCHR/dw_core = CHR_pub_tail - CHR_self_core ≈ 0.17。

## Corrected Claim

核心区域（一二线）流量权重 w_core 的精确计算：w_core = 0.6（基于 N14 给定地理分布，60% 用户位于一二线城市），该参数直接决定混合策略中自建部分对总命中率的贡献比例，若实际分布偏离 60%（如 50%-70%），CHR_hybrid 将线性变化，敏感度 dCHR/dw_core = CHR_pub_tail - CHR_self_core ≈ 0.17。

## Evidence

先验知识/题面给定，逻辑校验通过
