# N272: 若启用 FP8 KV Cache (E4M3)，32K 上下文下的 KV Cache 占用减半为 4.615 GB，总显存占用降至 14.5 + 4.615 +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

若启用 FP8 KV Cache (E4M3)，32K 上下文下的 KV Cache 占用减半为 4.615 GB，总显存占用降至 14.5 + 4.615 + 2.0 = 21.115 GB，低于 24 GB 上限，此时方案可行，剩余缓冲约 2.885 GB。

## Corrected Claim

若启用 FP8 KV Cache (E4M3)，32K 上下文下的 KV Cache 占用减半为 4.615 GB，总显存占用降至 14.5 + 4.615 + 2.0 = 21.115 GB，低于 24 GB 上限，此时方案可行，剩余缓冲约 2.885 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 (8-bit) 相比 FP16/BF16 (16-bit) 确实使 KV Cache 占用减半；算术运算 14.5 + 4.615 + 2.0 = 21.115 正确，且 24 - 21.115 = 2.885 正确，符合显存预算逻辑。
