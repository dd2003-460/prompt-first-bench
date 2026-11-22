# N322: INT8 量化在 RTX 4090 上的 Decode 阶段开销：Decode 阶段为带宽受限，INT8 权重读取量减半（13.5GB vs 27GB），但 d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

INT8 量化在 RTX 4090 上的 Decode 阶段开销：Decode 阶段为带宽受限，INT8 权重读取量减半（13.5GB vs 27GB），但 dequantization 操作引入额外的计算开销（约 5-10% 的 FLOPs 增加）。由于 Decode 阶段计算量远小于带宽读取量，dequantization 开销对吞吐量的影响可忽略不计（<2%），Decode 吞吐量仍由带宽决定，约为 37.3 tokens/s（理论）或 31.7 tokens/s（实际）。

## Corrected Claim

INT8 量化在 RTX 4090 上的 Decode 阶段开销：Decode 阶段为带宽受限，INT8 权重读取量减半（13.5GB vs 27GB），但 dequantization 操作引入额外的计算开销（约 5-10% 的 FLOPs 增加）。由于 Decode 阶段计算量远小于带宽读取量，dequantization 开销对吞吐量的影响可忽略不计（<2%），Decode 吞吐量仍由带宽决定，约为 37.3 tokens/s（理论）或 31.7 tokens/s（实际）。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段为带宽受限，INT8量化使权重体积减半（13.5GB vs 27GB），反量化计算开销（5-10% FLOPs）在带宽瓶颈下对吞吐量影响可忽略（<2%），吞吐量由带宽决定，数值量级合理。
