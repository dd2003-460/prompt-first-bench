# N168: Qwen3-27B 在 W4 精度下，权重显存占用区间为 13.5-17.0 GB，下限 13.5 GB 对应理想 4-bit 量化 (27e9 * 0.5 b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Qwen3-27B 在 W4 精度下，权重显存占用区间为 13.5-17.0 GB，下限 13.5 GB 对应理想 4-bit 量化 (27e9 * 0.5 bytes)，上限 17.0 GB 包含量化组块缩放因子 (Scale Factors) 及嵌入层未量化开销。

## Corrected Claim

Qwen3-27B 在 W4 精度下，权重显存占用区间为 13.5-17.0 GB，下限 13.5 GB 对应理想 4-bit 量化 (27e9 * 0.5 bytes)，上限 17.0 GB 包含量化组块缩放因子 (Scale Factors) 及嵌入层未量化开销。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在4-bit下理论最小值为13.5GB，加上量化开销（Scale Factors等）后17.0GB符合工程常识。
