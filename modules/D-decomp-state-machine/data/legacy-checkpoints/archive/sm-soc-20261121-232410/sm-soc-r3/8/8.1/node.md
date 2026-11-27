# N83: 买家搜索成本 C_search 在均衡前后的稳定性量化：定义 ΔC_search = (C_search_post - C_search_pre) / C_se

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

买家搜索成本 C_search 在均衡前后的稳定性量化：定义 ΔC_search = (C_search_post - C_search_pre) / C_search_pre，其中 C_search_pre 为高挂价现象出现前同类目买家平均单次有效搜索耗时（分钟）* 时间机会成本，C_search_post 为当前状态下的对应值；题面断言 ΔC_search < 5% 且统计显著性 p-value < 0.05。

## Corrected Claim

买家搜索成本 C_search 在均衡前后的稳定性量化：定义 ΔC_search = (C_search_post - C_search_pre) / C_search_pre，其中 C_search_pre 为高挂价现象出现前同类目买家平均单次有效搜索耗时（分钟）* 时间机会成本，C_search_post 为当前状态下的对应值；题面断言 ΔC_search < 5% 且统计显著性 p-value < 0.05。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点定义中的三个核心组件：前置成本估算、后置成本估算（含阈值推导）、以及统计显著性检验。三者逻辑独立，无重复计算或矛盾，且共同构成了对父节点断言的完整量化分解。）

## Search Query

eBay second-hand market buyer search cost change before after high listing price phenomenon empirical data
