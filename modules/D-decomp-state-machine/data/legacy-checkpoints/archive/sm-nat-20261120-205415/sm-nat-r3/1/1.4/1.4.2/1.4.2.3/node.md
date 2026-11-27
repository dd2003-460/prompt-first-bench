# N113: 工作点3（LFU 稳态）：LFU 缓存对象平均大小 E[S|LFU] ≈ 0.5MB（更偏向极小热门对象），K_LFU = 128GB/0.5MB = 262,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

工作点3（LFU 稳态）：LFU 缓存对象平均大小 E[S|LFU] ≈ 0.5MB（更偏向极小热门对象），K_LFU = 128GB/0.5MB = 262,144 > N=100,000，同样可容纳所有对象，Cov_byte = 100%；此时覆盖率不再是瓶颈，命中率差异完全由热度分布和替换策略决定。

## Corrected Claim

工作点3（LFU 稳态）：LFU 缓存对象平均大小 E[S|LFU] ≈ 0.5MB（更偏向极小热门对象），K_LFU = 128GB/0.5MB = 262,144 > N=100,000，同样可容纳所有对象，Cov_byte = 100%；此时覆盖率不再是瓶颈，命中率差异完全由热度分布和替换策略决定。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/0.5MB=262,144计算正确，且大于N=100,000，故容量充足，覆盖率100%的结论在逻辑上自洽。
