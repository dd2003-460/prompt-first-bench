# N9: Qwen3-27B 在 INT4/W4 精度下的基础权重显存占用约为 13.5 GB (27B * 0.5 bytes/token)，需额外考虑量化校准数据或 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B 在 INT4/W4 精度下的基础权重显存占用约为 13.5 GB (27B * 0.5 bytes/token)，需额外考虑量化校准数据或 Group Quantization 带来的少量开销（约 5-10%）。

## Corrected Claim

Qwen3-27B 在 INT4/W4 精度下的基础权重显存占用约为 13.5 GB (27B * 0.5 bytes/token)，需额外考虑量化校准数据或 Group Quantization 带来的少量开销（约 5-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 0.5 bytes/param (INT4) = 13.5 GB，计算准确且符合工程常识。

## Search Query

Qwen3-27B INT4 quantization memory footprint
