# N710: 工作点3的P99延迟中回源项的权重修正：原计算 0.20*30ms 仅考虑 L1 Miss 概率，未考虑 L2 Miss 后的二次回源，完整 P99 回源延迟项

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N235

## Claim

工作点3的P99延迟中回源项的权重修正：原计算 0.20*30ms 仅考虑 L1 Miss 概率，未考虑 L2 Miss 后的二次回源，完整 P99 回源延迟项应为 (1-H_l1)*RTT_L1_L2_p99 + H_l1*(1-H_l2)*RTT_L2_origin_p99 = 0.2*30ms + 0.8*0.1*80ms = 6ms + 6.4ms = 12.4ms，导致 P99_tail 修正为 60+12+12.4 = 84.4ms，仍满足 T=200ms 但余量减小。

## Corrected Claim

工作点3的P99延迟中回源项的权重修正：原计算 0.20*30ms 仅考虑 L1 Miss 概率，未考虑 L2 Miss 后的二次回源，完整 P99 回源延迟项应为 (1-H_l1)*RTT_L1_L2_p99 + H_l1*(1-H_l2)*RTT_L2_origin_p99 = 0.2*30ms + 0.8*0.1*80ms = 6ms + 6.4ms = 12.4ms，导致 P99_tail 修正为 60+12+12.4 = 84.4ms，仍满足 T=200ms 但余量减小。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合分层缓存延迟模型，数值计算（0.2*30 + 0.8*0.1*80 = 12.4）准确，且结论（84.4ms < 200ms）与前提一致。
