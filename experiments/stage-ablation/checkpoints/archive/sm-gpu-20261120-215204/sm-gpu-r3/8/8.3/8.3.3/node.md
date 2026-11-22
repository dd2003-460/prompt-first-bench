# N386: 基于修正TCO的每美元吞吐量比率：RTX 4090 (W4, 37 Tokens/s, $3,150 TCO) = 0.0117 Tokens/s/$; A10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

基于修正TCO的每美元吞吐量比率：RTX 4090 (W4, 37 Tokens/s, $3,150 TCO) = 0.0117 Tokens/s/$; A100 (FP8, 59 Tokens/s, $19,300 TCO) = 0.0031 Tokens/s/$; 比率为 3.77x，低于N145声称的5.9x，表明N145的比率计算可能使用了更低的RTX 4090 TCO或更高的A100 TCO。

## Corrected Claim

基于修正TCO的每美元吞吐量比率：RTX 4090 (W4, 37 Tokens/s, $3,150 TCO) = 0.0117 Tokens/s/$; A100 (FP8, 59 Tokens/s, $19,300 TCO) = 0.0031 Tokens/s/$; 比率为 3.77x，低于N145声称的5.9x，表明N145的比率计算可能使用了更低的RTX 4090 TCO或更高的A100 TCO。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（37/3150≈0.0117, 59/19300≈0.0031, 0.0117/0.0031≈3.77），且结论逻辑自洽（3.77x < 5.9x 暗示分母/分子差异导致比率降低）。

## Search Query

RTX 4090 vs A100 throughput per dollar TCO ratio comparison
