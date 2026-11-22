# N159: Qwen3-27B FP8 精度下 KV Cache 相比 BF16 的显存节省量为 0.80 GB，计算公式为 1.60 GB (BF16) - 0.80 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

Qwen3-27B FP8 精度下 KV Cache 相比 BF16 的显存节省量为 0.80 GB，计算公式为 1.60 GB (BF16) - 0.80 GB (FP8) = 0.80 GB，节省比例为 50%

## Corrected Claim

Qwen3-27B FP8 精度下 KV Cache 相比 BF16 的显存节省量为 0.80 GB，计算公式为 1.60 GB (BF16) - 0.80 GB (FP8) = 0.80 GB，节省比例为 50%

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位，BF16为16位，精度减半导致显存占用减半，50%节省比例符合数学逻辑。
