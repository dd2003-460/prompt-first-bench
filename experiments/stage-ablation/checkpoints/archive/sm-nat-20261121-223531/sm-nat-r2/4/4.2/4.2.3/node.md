# N58: 前1%对象在 128GB 缓存中的驻留时间 T_res,top1% 计算：前1%对象总大小 ≈ 1000 * 5KB = 5MB，远小于 128GB，因此这些对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

前1%对象在 128GB 缓存中的驻留时间 T_res,top1% 计算：前1%对象总大小 ≈ 1000 * 5KB = 5MB，远小于 128GB，因此这些对象始终驻留在缓存中，T_res,top1% = ∞（在 LRU 策略下不会被淘汰），更新率 1%/天对其命中率无直接干扰。

## Corrected Claim

前1%对象在 128GB 缓存中的驻留时间 T_res,top1% 计算：前1%对象总大小 ≈ 1000 * 5KB = 5MB，远小于 128GB，因此这些对象始终驻留在缓存中，T_res,top1% = ∞（在 LRU 策略下不会被淘汰），更新率 1%/天对其命中率无直接干扰。

## Evidence

先验知识/题面给定，逻辑校验通过：5MB远小于128GB，LRU策略下热数据不会被淘汰，驻留时间视为无穷大符合缓存原理。

## Search Query

top 1 percent objects residence time LRU cache capacity
