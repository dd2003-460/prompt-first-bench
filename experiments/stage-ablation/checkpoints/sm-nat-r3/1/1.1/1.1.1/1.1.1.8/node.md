# N117: 敏感性场景对缓存容量 N_cache 的影响：基于 N109 计算的 E[S] ≈ 8.8 KB，128GB 缓存可容纳对象数 N_cache = 128 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

敏感性场景对缓存容量 N_cache 的影响：基于 N109 计算的 E[S] ≈ 8.8 KB，128GB 缓存可容纳对象数 N_cache = 128 * 1024^3 / (8.8 * 1024) ≈ 14,874,255 个对象；N_cache 进一步增大，强化 N108 的结论，即缓存容量远大于总对象数，容量约束不是命中率瓶颈。

## Corrected Claim

敏感性场景对缓存容量 N_cache 的影响：基于 N109 计算的 E[S] ≈ 8.8 KB，128GB 缓存可容纳对象数 N_cache = 128 * 1024^3 / (8.8 * 1024) ≈ 14,874,255 个对象；N_cache 进一步增大，强化 N108 的结论，即缓存容量远大于总对象数，容量约束不是命中率瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB转换为字节后除以8.8KB，计算结果约1487万，量级与逻辑自洽。
