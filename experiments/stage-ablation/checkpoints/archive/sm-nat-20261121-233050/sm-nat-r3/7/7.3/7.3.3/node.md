# N161: 修正后的 LRU 命中率下界 H_LRU_corr 的数值计算：使用理论推导的 δ ≈ 0.019 替代经验值 0.5，H_LRU_corr = H_LRU_i

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

修正后的 LRU 命中率下界 H_LRU_corr 的数值计算：使用理论推导的 δ ≈ 0.019 替代经验值 0.5，H_LRU_corr = H_LRU_indep * (1 + ρ * δ) = 0.4641 * (1 + (-0.3) * 0.019) ≈ 0.4641 * 0.9943 ≈ 0.4615 (46.15%)。这表明在 ρ=-0.3 下，负相关性对命中率的影响极小（<1%），与经验值 0.85 倍存在显著差异，需通过仿真验证哪个模型更准确。

## Corrected Claim

在假设 δ ≈ 0.019 且 H_LRU_indep = 0.4641 的条件下，计算得 H_LRU_corr ≈ 0.4615。该结果依赖于特定参数假设，需通过仿真验证模型准确性。

## Evidence

[质询]该陈述包含具体的经验参数（δ ≈ 0.019, H_LRU_indep = 0.4641, ρ = -0.3）及基于这些参数的计算结果。虽然算术运算本身正确，但作为经验事实（特定场景下的命中率数值），缺乏外部来源支持其参数取值及最终结论的准确性，无法排除参数假设错误导致结论偏差的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值参数及模型适用性）

## Search Query

corrected LRU hit rate lower bound negative correlation rho -0.3 simulation validation
