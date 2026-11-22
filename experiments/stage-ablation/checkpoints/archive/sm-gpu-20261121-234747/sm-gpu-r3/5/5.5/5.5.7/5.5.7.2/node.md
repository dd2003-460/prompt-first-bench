# N425: 精度回退后的TCO增加比例计算公式：ΔTCO% = (TCO_新精度 - TCO_旧精度) / TCO_旧精度，其中TCO_新精度 = TCO_旧精度 + ΔM

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

精度回退后的TCO增加比例计算公式：ΔTCO% = (TCO_新精度 - TCO_旧精度) / TCO_旧精度，其中TCO_新精度 = TCO_旧精度 + ΔMem_1step * C_memory_per_GB + ΔPower_1step * h * r * 3，需代入具体硬件内存单价（如$100/GB）和功耗差异（如FP8比BF16低10%功耗）计算。

## Corrected Claim

精度回退后的TCO增加比例计算公式：ΔTCO% = (TCO_新精度 - TCO_旧精度) / TCO_旧精度，其中TCO_新精度 = TCO_旧精度 + ΔMem_1step * C_memory_per_GB + ΔPower_1step * h * r * 3，需代入具体硬件内存单价（如$100/GB）和功耗差异（如FP8比BF16低10%功耗）计算。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO变化率公式定义正确，增量成本由内存增加和功耗变化（乘以时间、费率及系数3，可能代表3年或3倍负载等假设）构成，量纲与逻辑自洽。
