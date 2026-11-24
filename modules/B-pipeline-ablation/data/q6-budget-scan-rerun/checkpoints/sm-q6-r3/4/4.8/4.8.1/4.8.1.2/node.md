# N290: 缓存算法选择对P99延迟的影响机制：LFU通过优先保留高频对象，降低长尾请求的回源概率，从而减少回源队列排队延迟 T_queue_origin；量化关系为 ΔP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

缓存算法选择对P99延迟的影响机制：LFU通过优先保留高频对象，降低长尾请求的回源概率，从而减少回源队列排队延迟 T_queue_origin；量化关系为 ΔP99_LFU_LR = T_origin_tail × (1-CHR_LFU) - T_origin_tail × (1-CHR_LRU) = T_origin_tail × ΔCHR_LFU_LR，若 T_origin_tail=300ms 且 ΔCHR=7%，则 ΔP99_LFU_LR ≈ 21ms，该值直接贡献于P99合规性判断。

## Corrected Claim

缓存算法选择对P99延迟的影响机制：LFU通过优先保留高频对象，降低长尾请求的回源概率，从而减少回源队列排队延迟 T_queue_origin；量化关系为 ΔP99_LFU_LR = T_origin_tail × (1-CHR_LFU) - T_origin_tail × (1-CHR_LRU) = T_origin_tail × ΔCHR_LFU_LR，若 T_origin_tail=300ms 且 ΔCHR=7%，则 ΔP99_LFU_LR ≈ 21ms，该值直接贡献于P99合规性判断。

## Evidence

先验知识/题面给定，逻辑校验通过
