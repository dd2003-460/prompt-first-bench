# N100: E[S|Miss] 的条件期望计算：由于 LRU 驱逐的是最冷对象（通常也是最大对象，因 ρ=-0.3），E[S|Miss] ≈ E[S | S > s_thr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

E[S|Miss] 的条件期望计算：由于 LRU 驱逐的是最冷对象（通常也是最大对象，因 ρ=-0.3），E[S|Miss] ≈ E[S | S > s_threshold]，其中 s_threshold 是驻留边界，该值显著高于全局均值 E[S]。

## Corrected Claim

E[S|Miss] 的条件期望计算：由于 LRU 驱逐的是最冷对象（通常也是最大对象，因 ρ=-0.3），E[S|Miss] ≈ E[S | S > s_threshold]，其中 s_threshold 是驻留边界，该值显著高于全局均值 E[S]。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驱逐最冷对象且冷对象通常较大（ρ=-0.3），故Miss时的对象大小条件期望显著高于全局均值，符合缓存替换策略的基本逻辑。
