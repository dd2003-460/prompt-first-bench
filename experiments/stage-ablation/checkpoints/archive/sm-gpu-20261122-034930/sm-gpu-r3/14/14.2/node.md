# N433: 临界吞吐量提升倍数公式推导：设 $V_{INT8} = T_{INT8} \times Q_{INT8} / TCO_{INT8}$，$V_{W4} = T_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N156

## Claim

临界吞吐量提升倍数公式推导：设 $V_{INT8} = T_{INT8} \times Q_{INT8} / TCO_{INT8}$，$V_{W4} = T_{W4} \times Q_{W4} / TCO_{W4}$。令 $V_{W4} > V_{INT8}$，解得 $T_{W4}/T_{INT8} > (Q_{INT8}/Q_{W4}) \times (TCO_{W4}/TCO_{INT8})$。代入 $Q_{INT8}=0.98, Q_{W4}=0.95, TCO_{W4}/TCO_{INT8} \approx 0.6$ (假设 W4 硬件成本更低或功耗更低)，临界比值为 $(0.98/0.95) \times 0.6 \approx 0.62$，即 W4 吞吐量只需达到 INT8 的 62% 即可在加权性价比上胜出，前提是硬件成本显著降低。

## Corrected Claim

临界吞吐量提升倍数公式推导：设 $V_{INT8} = T_{INT8} \times Q_{INT8} / TCO_{INT8}$，$V_{W4} = T_{W4} \times Q_{W4} / TCO_{W4}$。令 $V_{W4} > V_{INT8}$，解得 $T_{W4}/T_{INT8} > (Q_{INT8}/Q_{W4}) \times (TCO_{W4}/TCO_{INT8})$。代入 $Q_{INT8}=0.98, Q_{W4}=0.95, TCO_{W4}/TCO_{INT8} \approx 0.6$ (假设 W4 硬件成本更低或功耗更低)，临界比值为 $(0.98/0.95) \times 0.6 \approx 0.62$，即 W4 吞吐量只需达到 INT8 的 62% 即可在加权性价比上胜出，前提是硬件成本显著降低。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导正确，数值计算 (0.98/0.95)*0.6 ≈ 0.62 准确，量纲与逻辑自洽。
