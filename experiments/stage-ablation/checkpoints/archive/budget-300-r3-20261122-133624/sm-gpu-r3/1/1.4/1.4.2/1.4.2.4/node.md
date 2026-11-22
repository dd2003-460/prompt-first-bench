# N207: INT8 量化权重的精确显存占用计算：$M_{weights} = P_{total} \times S_{dtype} + M_{scales} + M_{z

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54, N56, N57

## Claim

INT8 量化权重的精确显存占用计算：$M_{weights} = P_{total} \times S_{dtype} + M_{scales} + M_{zero\_points}$。其中 $P_{total} = 27 \times 10^9$，$S_{dtype} = 1$ byte/param。Scale 因子和 Zero Point 通常为 FP16/FP32 存储，若每 128 个参数共享一组 scale/zero，则 $M_{scales} \approx (27 \times 10^9 / 128) \times 4 \text{ bytes} \approx 0.84$GB。总权重占用 $M_{weights} \approx 27 + 0.84 = 27.84$GB。

## Corrected Claim

INT8 量化权重的精确显存占用计算：$M_{weights} = P_{total} \times S_{dtype} + M_{scales} + M_{zero\_points}$。其中 $P_{total} = 27 \times 10^9$，$S_{dtype} = 1$ byte/param。Scale 因子和 Zero Point 通常为 FP16/FP32 存储，若每 128 个参数共享一组 scale/zero，则 $M_{scales} \approx (27 \times 10^9 / 128) \times 4 \text{ bytes} \approx 0.84$GB。总权重占用 $M_{weights} \approx 27 + 0.84 = 27.84$GB。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8权重27GB，Scale/ZeroPoint按128分组FP32存储约0.84GB，总显存27.84GB，计算与量级均合理。
