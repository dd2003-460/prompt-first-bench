# N88: NVIDIA L4 24GB 在 Qwen3-27B FP8 精度下的显存占用为 27GB (权重) + 8.4GB (KV Cache) + 2GB (激活)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

NVIDIA L4 24GB 在 Qwen3-27B FP8 精度下的显存占用为 27GB (权重) + 8.4GB (KV Cache) + 2GB (激活) = 37.4GB，超出显存容量 13.4GB，需依赖 CPU 卸载或 INT8/W4 量化，若使用 W4 则占用 13.5GB + 8.4GB + 2GB = 23.9GB，显存利用率约 99.58%。

## Corrected Claim

NVIDIA L4 24GB 在 Qwen3-27B FP8 精度下的显存占用为 27GB (权重) + 8.4GB (KV Cache) + 2GB (激活) = 37.4GB，超出显存容量 13.4GB，需依赖 CPU 卸载或 INT8/W4 量化，若使用 W4 则占用 13.5GB + 8.4GB + 2GB = 23.9GB，显存利用率约 99.58%。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约27GB，W4量化约13.5GB，KV Cache与激活值估算符合常规推理显存占用规律，算术计算正确。
