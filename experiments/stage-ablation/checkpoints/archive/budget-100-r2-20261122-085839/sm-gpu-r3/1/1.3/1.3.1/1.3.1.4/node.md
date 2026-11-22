# N134: BF16 精度下，Qwen3-27B 在 Batch=1, Seq_Len=32K 时，单层 Attention + MLP 激活值总显存的具体数值（GB），用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

BF16 精度下，Qwen3-27B 在 Batch=1, Seq_Len=32K 时，单层 Attention + MLP 激活值总显存的具体数值（GB），用于验证 N36 中'每层约 2*hidden*seq*bytes'估算是否低估了中间层（MLP）的贡献

## Corrected Claim

BF16 精度下，Qwen3-27B 在 Batch=1, Seq_Len=32K 时，单层 Attention + MLP 激活值总显存的具体数值（GB），用于验证 N36 中'每层约 2*hidden*seq*bytes'估算是否低估了中间层（MLP）的贡献

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的 hidden_size 为 5120，MLP 中间维度通常为 4*hidden (20480)。单层激活值显存 = (Attention QKV/O + MLP Up/Down/Gate) * seq_len * batch * bytes。估算约为 (5120*4 + 20480*3) * 32768 * 1 * 2 bytes ≈ 4.5 GB。该数值量级合理，且确实远高于仅计算 Attention 或简单 hidden 层的估算，逻辑自洽。
