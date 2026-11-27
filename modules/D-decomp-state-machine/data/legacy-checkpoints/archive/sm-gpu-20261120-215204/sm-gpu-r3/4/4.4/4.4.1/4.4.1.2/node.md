# N296: BF16 精度下 KV Cache 占用量：2 * 64 * 10 * 128 * 32768 * 2 bytes = 10.74 GB (修正 N106 中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104, N105, N106

## Claim

BF16 精度下 KV Cache 占用量：2 * 64 * 10 * 128 * 32768 * 2 bytes = 10.74 GB (修正 N106 中 2.68GB 的计算错误，原错误可能源于误用 Head Dim 或层数)

## Corrected Claim

BF16 精度下 KV Cache 占用量：2 * 64 * 10 * 128 * 32768 * 2 bytes = 10.74 GB (修正 N106 中 2.68GB 的计算错误，原错误可能源于误用 Head Dim 或层数)

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 64 * 10 * 128 * 32768 * 2 = 10,737,418,240 bytes ≈ 10.74 GB，数值量级与算术结果一致。
