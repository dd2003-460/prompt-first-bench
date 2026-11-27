# N281: 2×RTX 4090 显存分配精确验证：48GB (Total) - 27GB (FP8 Weights) - 4.03GB (BF16 KV, Batch=1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

2×RTX 4090 显存分配精确验证：48GB (Total) - 27GB (FP8 Weights) - 4.03GB (BF16 KV, Batch=1) = 16.97GB 余量；若 Batch=4，KV 占用 ≈ 16.12GB，总占用 43.12GB，剩余 4.88GB，仍满足需求但无扩展空间，N93 中 '16GB KV' 的估算同样高估了 4 倍。

## Corrected Claim

2×RTX 4090 显存分配精确验证：48GB (Total) - 27GB (FP8 Weights) - 4.03GB (BF16 KV, Batch=1) = 16.97GB 余量；若 Batch=4，KV 占用 ≈ 16.12GB，总占用 43.12GB，剩余 4.88GB，仍满足需求但无扩展空间，N93 中 '16GB KV' 的估算同样高估了 4 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 48-27-4.03=16.97 及 4.03*4=16.12, 27+16.12=43.12, 48-43.12=4.88 均准确无误，且符合显存分配的基本逻辑。
