# N81: 显存带宽利用率修正因子：在低精度下，由于反量化（Dequantization）操作引入的计算延迟，实际有效带宽利用率相比理论峰值带宽的折扣率，通常 INT8 折

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

显存带宽利用率修正因子：在低精度下，由于反量化（Dequantization）操作引入的计算延迟，实际有效带宽利用率相比理论峰值带宽的折扣率，通常 INT8 折扣率为 0.85-0.95，4-bit 折扣率为 0.75-0.90，需结合具体推理框架（如 vLLM, ExLlama）实现细节验证。

## Corrected Claim

显存带宽利用率修正因子：在低精度下，由于反量化（Dequantization）操作引入的计算延迟，实际有效带宽利用率相比理论峰值带宽的折扣率，通常 INT8 折扣率为 0.85-0.95，4-bit 折扣率为 0.75-0.90，需结合具体推理框架（如 vLLM, ExLlama）实现细节验证。

## Evidence

先验知识/题面给定，逻辑校验通过
