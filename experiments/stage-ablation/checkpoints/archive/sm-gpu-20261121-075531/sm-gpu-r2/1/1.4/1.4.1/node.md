# N44: INT8/FP8精度单卡显存需求计算：权重27GB + KV Cache 1.93GB + 激活开销1.5GB = 30.43GB，需32GB显存（仅RTX 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

INT8/FP8精度单卡显存需求计算：权重27GB + KV Cache 1.93GB + 激活开销1.5GB = 30.43GB，需32GB显存（仅RTX 5090满足）或48GB显存（L40S/A6000），24GB卡（RTX 4090/3090）因显存不足31GB而不可行。

## Corrected Claim

INT8/FP8精度单卡显存需求计算：权重27GB + KV Cache 1.93GB + 激活开销1.5GB = 30.43GB，需32GB显存（仅RTX 5090满足）或48GB显存（L40S/A6000），24GB卡（RTX 4090/3090）因显存不足31GB而不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：27+1.93+1.5=30.43GB，小于32GB且大于24GB，硬件匹配逻辑自洽。
