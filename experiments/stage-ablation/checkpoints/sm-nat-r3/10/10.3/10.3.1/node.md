# N185: LRU 栈内容中“冷大对象”的识别标准：定义对象 i 为“冷”若其访问频率 λ_i < λ_threshold，其中 λ_threshold 取中位数频率或特定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

LRU 栈内容中“冷大对象”的识别标准：定义对象 i 为“冷”若其访问频率 λ_i < λ_threshold，其中 λ_threshold 取中位数频率或特定分位数（如 P10）。在 Zipf(β=0.9) 下，λ_i ∝ i^{-0.9}，需计算满足 λ_i < λ_threshold 的对象排名范围 [i_min, N]。

## Corrected Claim

LRU 栈内容中“冷大对象”的识别标准：定义对象 i 为“冷”若其访问频率 λ_i < λ_threshold，其中 λ_threshold 取中位数频率或特定分位数（如 P10）。在 Zipf(β=0.9) 下，λ_i ∝ i^{-0.9}，需计算满足 λ_i < λ_threshold 的对象排名范围 [i_min, N]。

## Evidence

先验知识/题面给定，逻辑校验通过
