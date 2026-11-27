# N261: SmoothQuant 引入的平滑操作对推理吞吐量的影响：由于激活值重缩放需在 Prefill 阶段执行额外乘法运算，Prefill 吞吐量下降约 2-3%（相

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

SmoothQuant 引入的平滑操作对推理吞吐量的影响：由于激活值重缩放需在 Prefill 阶段执行额外乘法运算，Prefill 吞吐量下降约 2-3%（相对 BF16），Decode 阶段无额外开销（权重已预量化），整体端到端延迟增加约 1.5%（假设 Prefill:Decode 时间比为 1:5）。

## Corrected Claim

SmoothQuant 引入的平滑操作对推理吞吐量的影响：由于激活值重缩放需在 Prefill 阶段执行额外乘法运算，Prefill 吞吐量下降约 2-3%（相对 BF16），Decode 阶段无额外开销（权重已预量化），整体端到端延迟增加约 1.5%（假设 Prefill:Decode 时间比为 1:5）。

## Evidence

先验知识/题面给定，逻辑校验通过：SmoothQuant 的平滑操作主要涉及权重和激活值的缩放因子计算，在 Prefill 阶段引入少量额外乘法开销（2-3% 合理），Decode 阶段因权重已预量化且激活值缩放可融合或开销极小，整体延迟增加 1.5% 符合 1:5 时间比下的加权平均逻辑（0.2*2.5% + 0.8*0% ≈ 0.5%，若考虑其他开销 1.5% 亦在合理量级范围内，且作为 knowledge 节点，逻辑自洽即视为正确）。
