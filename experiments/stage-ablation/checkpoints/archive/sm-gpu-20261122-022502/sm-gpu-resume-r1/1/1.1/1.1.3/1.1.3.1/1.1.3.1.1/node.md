# N442: INT4 (AWQ, group_size=128) 量化后模型权重与量化参数总显存占用为 14.344 GB，计算式为 (27e9 * 4 bits / 8)

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

INT4 (AWQ, group_size=128) 量化后模型权重与量化参数总显存占用为 14.344 GB，计算式为 (27e9 * 4 bits / 8) / 1e9 + 0.844 GB = 13.5 GB + 0.844 GB。

## Corrected Claim

INT4 (AWQ, group_size=128) 量化后模型权重与量化参数总显存占用为 14.344 GB，计算式为 (27e9 * 4 bits / 8) / 1e9 + 0.844 GB = 13.5 GB + 0.844 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 4bits / 8 / 1e9 = 13.5GB，加上0.844GB量化参数，总和14.344GB，计算无误。
