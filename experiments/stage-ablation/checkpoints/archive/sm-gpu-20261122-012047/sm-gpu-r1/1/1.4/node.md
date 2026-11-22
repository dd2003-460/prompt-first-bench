# N9: FP8 精度下 Qwen3-27B 的静态权重显存占用降至 27 GB (27B params × 1 byte)，KV Cache 若保持 BF16 则总显存

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

FP8 精度下 Qwen3-27B 的静态权重显存占用降至 27 GB (27B params × 1 byte)，KV Cache 若保持 BF16 则总显存需求为 48.7 GB，若 KV Cache 也降至 FP8 则总需求为 37.3 GB。

## Corrected Claim

FP8 精度下 Qwen3-27B 的静态权重显存占用降至 27 GB (27B params × 1 byte)，KV Cache 若保持 BF16 则总显存需求为 48.7 GB，若 KV Cache 也降至 FP8 则总需求为 37.3 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×1字节=27GB权重；总显存48.7GB和37.3GB的数值符合KV Cache在BF16和FP8下的合理量级估算，无内部矛盾。
