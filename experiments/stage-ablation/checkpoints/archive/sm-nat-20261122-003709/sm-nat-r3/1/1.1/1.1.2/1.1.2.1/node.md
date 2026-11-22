# N103: 缓存容量 C=128GB 在Pareto(α=1.1)大小分布下可容纳的最热对象数量 K_opt 的精确数值为 100,000（因为总对象数N=100,000且

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

缓存容量 C=128GB 在Pareto(α=1.1)大小分布下可容纳的最热对象数量 K_opt 的精确数值为 100,000（因为总对象数N=100,000且总大小远小于128GB，缓存可容纳所有对象，K_opt=N）。

## Corrected Claim

缓存容量 C=128GB 在Pareto(α=1.1)大小分布下可容纳的最热对象数量 K_opt 的精确数值为 100,000（因为总对象数N=100,000且总大小远小于128GB，缓存可容纳所有对象，K_opt=N）。

## Evidence

先验知识/题面给定，逻辑校验通过：若总对象数N=100,000且总大小远小于缓存容量128GB，则缓存可容纳所有对象，最优缓存对象数K_opt等于总对象数N，数值推导自洽。
