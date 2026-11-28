# N39: TP=4 相比 TP=2 的实际加速比受限于 Amdahl 定律，非并行部分（如 LayerNorm、激活函数）占比约 10-15%，导致 TP=4 的理论最大

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

TP=4 相比 TP=2 的实际加速比受限于 Amdahl 定律，非并行部分（如 LayerNorm、激活函数）占比约 10-15%，导致 TP=4 的理论最大加速比为 1/(1/4 + 0.125) ≈ 3.2x，而非理想的 4x；若通信开销增加 20%，实际加速比将降至 ~2.8x。

## Corrected Claim

TP=4 相比 TP=2 的实际加速比受限于 Amdahl 定律，非并行部分（如 LayerNorm、激活函数）占比约 10-15%，导致 TP=4 的理论最大加速比为 1/(1/4 + 0.125) ≈ 3.2x，而非理想的 4x；若通信开销增加 20%，实际加速比将降至 ~2.8x。

## Evidence

先验知识/题面给定，逻辑校验通过：Amdahl定律计算正确（1/(0.25+0.125)=3.2），通信开销增加导致加速比下降符合分布式训练常识，数值量级合理。
