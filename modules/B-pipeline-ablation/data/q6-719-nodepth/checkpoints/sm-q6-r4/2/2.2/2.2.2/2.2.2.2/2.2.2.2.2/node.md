# N523: 自建节点缓存命中率 H_self 受限于单节点容量与本地用户请求分布的匹配度，若单 POP 覆盖用户日均下载量 D_pop = 200GB，且热数据 Top-N

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N170

## Claim

自建节点缓存命中率 H_self 受限于单节点容量与本地用户请求分布的匹配度，若单 POP 覆盖用户日均下载量 D_pop = 200GB，且热数据 Top-N 占用 80TB，则 H_self = Min(1, C_self_storage / D_pop_hot)，若 D_pop_hot = 100TB，则 H_self ≈ 80%；若容量不足，H_self 随容量线性下降，边际收益递减。

## Corrected Claim

自建节点缓存命中率 H_self 受限于单节点容量与本地用户请求分布的匹配度，若单 POP 覆盖用户日均下载量 D_pop = 200GB，且热数据 Top-N 占用 80TB，则 H_self = Min(1, C_self_storage / D_pop_hot)，若 D_pop_hot = 100TB，则 H_self ≈ 80%；若容量不足，H_self 随容量线性下降，边际收益递减。

## Evidence

先验知识/题面给定，逻辑校验通过
