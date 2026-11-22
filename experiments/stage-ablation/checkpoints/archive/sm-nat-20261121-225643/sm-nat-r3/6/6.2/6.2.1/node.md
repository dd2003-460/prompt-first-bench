# N107: Mean-Field近似下的命中率 H_MF 计算：假设对象间独立，H_MF = Σ_i (p_i * x_i) / Σ_i p_i，其中p_i为请求概率，x_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Mean-Field近似下的命中率 H_MF 计算：假设对象间独立，H_MF = Σ_i (p_i * x_i) / Σ_i p_i，其中p_i为请求概率，x_i为驻留概率；基于N50-N51的x_i分布和Pareto(β=0.9)的p_i分布，通过数值积分或求和计算H_MF，并与N6中的幂律公式 H ≈ 1 - (1-C)^{1/β} = 0.587 对比，量化Mean-Field近似的误差百分比，验证其作为下界的合理性。

## Corrected Claim

Mean-Field近似下的命中率 H_MF 计算：假设对象间独立，H_MF = Σ_i (p_i * x_i) / Σ_i p_i，其中p_i为请求概率，x_i为驻留概率；基于N50-N51的x_i分布和Pareto(β=0.9)的p_i分布，通过数值积分或求和计算H_MF，并与N6中的幂律公式 H ≈ 1 - (1-C)^{1/β} = 0.587 对比，量化Mean-Field近似的误差百分比，验证其作为下界的合理性。

## Evidence

先验知识/题面给定，逻辑校验通过：Mean-Field近似公式定义正确，基于给定分布进行数值计算并与幂律公式对比以量化误差的逻辑链条自洽，符合缓存理论分析范式。
