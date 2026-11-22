# N46: Qwen3-27B 在 INT8 精度下的权重显存占用计算：27,000,000,000 params * 1 byte/param = 27 GB (基础值)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 在 INT8 精度下的权重显存占用计算：27,000,000,000 params * 1 byte/param = 27 GB (基础值)；若采用混合精度量化（如 SmoothQuant 保留部分层为 FP16 或 INT4 混合），实际占用可能波动在 26-28 GB 之间，取决于量化策略中保留的高精度层比例（通常 <5%）。

## Corrected Claim

Qwen3-27B 在 INT8 精度下的权重显存占用计算：27,000,000,000 params * 1 byte/param = 27 GB (基础值)；若采用混合精度量化（如 SmoothQuant 保留部分层为 FP16 或 INT4 混合），实际占用可能波动在 26-28 GB 之间，取决于量化策略中保留的高精度层比例（通常 <5%）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8下基础占用27GB，混合精度波动范围26-28GB符合工程常识
