# N199: FP8 (E4M3) 量化下 Qwen3-27B 的静态权重显存占用为 27 GB (27B × 1 byte)，这是多卡分片可行性分析的基础项。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38

## Claim

FP8 (E4M3) 量化下 Qwen3-27B 的静态权重显存占用为 27 GB (27B × 1 byte)，这是多卡分片可行性分析的基础项。

## Corrected Claim

FP8 (E4M3) 量化下 Qwen3-27B 的静态权重显存占用为 27 GB (27B × 1 byte)，这是多卡分片可行性分析的基础项。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 (E4M3) 为 8-bit 格式，27B 参数对应 27GB 显存占用，计算逻辑自洽且符合工程常识。
