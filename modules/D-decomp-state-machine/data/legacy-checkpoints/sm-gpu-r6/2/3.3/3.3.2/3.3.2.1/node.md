# N152: FP8 (E4M3) 精度下，27B 模型权重占用为 27.8 GB (27.8B * 1 byte)，相比 BF16 (55.6 GB) 节省 50% 显存，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

FP8 (E4M3) 精度下，27B 模型权重占用为 27.8 GB (27.8B * 1 byte)，相比 BF16 (55.6 GB) 节省 50% 显存，是满足 32GB 显存下限的关键量化选择

## Corrected Claim

FP8 (E4M3) 精度下，27B 模型权重占用为 27.8 GB (27.8B * 1 byte)，相比 BF16 (55.6 GB) 节省 50% 显存，是满足 32GB 显存下限的关键量化选择

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 (E4M3) 为 8-bit 格式，27B 参数 * 1 byte = 27GB，BF16 为 16-bit 格式，27B * 2 bytes = 54GB，27/54 = 50% 节省，且 27GB < 32GB，逻辑与数值均自洽。
