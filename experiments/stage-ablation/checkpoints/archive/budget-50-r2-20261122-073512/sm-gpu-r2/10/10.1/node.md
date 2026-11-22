# N194: INT4 (W4) 量化下 Qwen3-27B 的静态权重显存占用为 13.5 GB (27B × 0.5 bytes)，这是单卡 24GB 可行性分析的基础项

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38

## Claim

INT4 (W4) 量化下 Qwen3-27B 的静态权重显存占用为 13.5 GB (27B × 0.5 bytes)，这是单卡 24GB 可行性分析的基础项。

## Corrected Claim

INT4 (W4) 量化下 Qwen3-27B 的静态权重显存占用为 13.5 GB (27B × 0.5 bytes)，这是单卡 24GB 可行性分析的基础项。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 × 0.5 bytes/param (INT4) = 13.5 GB，计算准确且符合量化显存估算基本逻辑。
