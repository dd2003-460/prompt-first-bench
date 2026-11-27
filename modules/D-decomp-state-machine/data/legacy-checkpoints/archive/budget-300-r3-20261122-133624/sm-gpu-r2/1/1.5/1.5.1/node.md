# N56: INT8 量化下权重显存占用精确计算：$27 \times 10^9 \times 1$ byte = 27GB，需考虑量化校准数据（Calibration D

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

INT8 量化下权重显存占用精确计算：$27 \times 10^9 \times 1$ byte = 27GB，需考虑量化校准数据（Calibration Data）和 Scale 因子的额外占用（通常 <0.5GB），实际权重占用约为 27.5GB。

## Corrected Claim

INT8 量化下权重显存占用精确计算：$27 \times 10^9 \times 1$ byte = 27GB，需考虑量化校准数据（Calibration Data）和 Scale 因子的额外占用（通常 <0.5GB），实际权重占用约为 27.5GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×1字节=27GB，加上少量校准/Scale开销，总量级合理且符合INT8量化常识。

## Search Query

INT8 quantization scale factor memory overhead LLM
