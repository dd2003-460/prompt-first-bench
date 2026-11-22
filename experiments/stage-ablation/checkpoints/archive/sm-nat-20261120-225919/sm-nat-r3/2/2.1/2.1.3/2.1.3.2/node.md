# N137: 工作点 2（中容量约束）：假设 S_min=10KB, S_max=10MB，S_total ≈ 50GB < 128GB，k_max = N = 10^5，H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点 2（中容量约束）：假设 S_min=10KB, S_max=10MB，S_total ≈ 50GB < 128GB，k_max = N = 10^5，H_req = 100%，但平均大小增大导致缓存替换频率增加，LRU 有效命中率因更新失效打 0.99 折（基于 N69 的 1%/天 更新率），H_eff ≈ 99%。

## Corrected Claim

工作点 2（中容量约束）：假设 S_min=10KB, S_max=10MB，S_total ≈ 50GB < 128GB，k_max = N = 10^5，H_req = 100%，但平均大小增大导致缓存替换频率增加，LRU 有效命中率因更新失效打 0.99 折（基于 N69 的 1%/天 更新率），H_eff ≈ 99%。

## Evidence

先验知识/题面给定，逻辑校验通过：容量约束满足（50GB < 128GB），命中率折损计算（100% * 0.99 = 99%）符合算术逻辑，且基于给定的更新率假设推导自洽。
