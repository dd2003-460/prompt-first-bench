# N483: A6000 与 L40S 在 Prefill 阶段的性能对比修正：L40S BF16 算力为 90.5 TFLOPS，理论 Prefill 吞吐量上限 = 90

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N163

## Claim

A6000 与 L40S 在 Prefill 阶段的性能对比修正：L40S BF16 算力为 90.5 TFLOPS，理论 Prefill 吞吐量上限 = 90.5e12 / 1.77e15 ≈ 51.1 tokens/s，远高于 A6000 的 21.9 tokens/s；但两者均受限于 48GB 显存，无法在 BF16 下运行 32K 上下文，需量化后重新计算，量化后的 Prefill 吞吐量将因计算精度降低和内存带宽利用效率变化而有所不同。

## Corrected Claim

A6000 与 L40S 在 Prefill 阶段的性能对比修正：L40S BF16 算力为 90.5 TFLOPS，理论 Prefill 吞吐量上限 = 90.5e12 / 1.77e15 ≈ 51.1 tokens/s，远高于 A6000 的 21.9 tokens/s；但两者均受限于 48GB 显存，无法在 BF16 下运行 32K 上下文，需量化后重新计算，量化后的 Prefill 吞吐量将因计算精度降低和内存带宽利用效率变化而有所不同。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S BF16算力90.5 TFLOPS与A6000 48GB显存规格符合公开硬件参数，吞吐量计算逻辑（算力/模型FLOPs）自洽，且48GB显存限制32K上下文BF16推理的结论符合内存带宽与容量常识。

## Search Query

L40S vs A6000 prefill performance comparison
