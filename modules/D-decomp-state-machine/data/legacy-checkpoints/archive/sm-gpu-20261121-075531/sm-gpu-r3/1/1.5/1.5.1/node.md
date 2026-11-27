# N47: TP=2下BF16精度多卡显存分配：每卡承担权重27GB + 全量KV Cache 1.93GB + 激活开销0.75GB = 29.68GB，24GB显存卡不

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

TP=2下BF16精度多卡显存分配：每卡承担权重27GB + 全量KV Cache 1.93GB + 激活开销0.75GB = 29.68GB，24GB显存卡不可行（需≥32GB卡如RTX 5090或48GB卡如L40S），40GB A100可满足但剩余10.32GB。

## Corrected Claim

TP=2下BF16精度多卡显存分配：每卡承担权重27GB + 全量KV Cache 1.93GB + 激活开销0.75GB = 29.68GB，24GB显存卡不可行（需≥32GB卡如RTX 5090或48GB卡如L40S），40GB A100可满足但剩余10.32GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27+1.93+0.75=29.68GB，29.68>24GB故24GB卡不可行，29.68<40GB且40-29.68=10.32GB，数值与逻辑自洽。
