# N87: 响应率提升 Δr_response：原降价响应率 r_old，干预后 r_new。假设警告机制使 50% 的目标卖家执行建议降价，则 r_new = r_old

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N20

## Claim

响应率提升 Δr_response：原降价响应率 r_old，干预后 r_new。假设警告机制使 50% 的目标卖家执行建议降价，则 r_new = r_old + 0.5 * (1 - r_old) * r_compliance，其中 r_compliance 为卖家对建议的遵从率。

## Corrected Claim

响应率提升 Δr_response：原降价响应率 r_old，干预后 r_new。假设警告机制使 50% 的目标卖家执行建议降价，则 r_new = r_old + 0.5 * (1 - r_old) * r_compliance，其中 r_compliance 为卖家对建议的遵从率。

## Evidence

先验知识/题面给定，逻辑校验通过
