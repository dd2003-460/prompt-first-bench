# N107: 修正 N41 中 k_max 的定义：在容量非绑定约束下（N70），k_max 不再由 C/E[S] 决定，而是等于总对象数 N=100,000；因此 ∑_{i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

修正 N41 中 k_max 的定义：在容量非绑定约束下（N70），k_max 不再由 C/E[S] 决定，而是等于总对象数 N=100,000；因此 ∑_{i=1}^{k_max} S_i 变为 ∑_{i=1}^{100,000} S_i，即所有对象的总大小。

## Corrected Claim

修正 N41 中 k_max 的定义：在容量非绑定约束下（N70），k_max 不再由 C/E[S] 决定，而是等于总对象数 N=100,000；因此 ∑_{i=1}^{k_max} S_i 变为 ∑_{i=1}^{100,000} S_i，即所有对象的总大小。

## Evidence

先验知识/题面给定，逻辑校验通过：在容量非绑定约束下，缓存可容纳所有对象，故 k_max 等于总对象数 N，求和范围覆盖所有对象。
