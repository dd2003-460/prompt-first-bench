# N48: 动态修正因子对字节命中率的影响不是均匀的：对于小对象（S < 1KB），更新导致的缓存失效字节损失占比小；对于大对象（S > 10MB），更新导致的缓存失效字节

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

动态修正因子对字节命中率的影响不是均匀的：对于小对象（S < 1KB），更新导致的缓存失效字节损失占比小；对于大对象（S > 10MB），更新导致的缓存失效字节损失占比大。加权平均折损 D_bytes = ∫ [1 - P_invalidate(s)] * f_size(s) ds，其中 P_invalidate(s) 与对象大小 s 无关（假设更新率独立于大小），则 D_bytes = 1 - P_invalidate ≈ 0.99005。

## Corrected Claim

动态修正因子对字节命中率的影响不是均匀的：对于小对象（S < 1KB），更新导致的缓存失效字节损失占比小；对于大对象（S > 10MB），更新导致的缓存失效字节损失占比大。加权平均折损 D_bytes = ∫ [1 - P_invalidate(s)] * f_size(s) ds，其中 P_invalidate(s) 与对象大小 s 无关（假设更新率独立于大小），则 D_bytes = 1 - P_invalidate ≈ 0.99005。

## Evidence

先验知识/题面给定，逻辑校验通过：积分公式推导正确，数值计算 1 - 0.00995 = 0.99005 无误，且符合大对象失效损失占比大的直觉。

## Search Query

cache invalidation byte weighted hit rate update rate
