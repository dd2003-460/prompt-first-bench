# N163: 量化更新率与热度的相关性系数 \rho_{u,h}：通过业务日志计算 Pearson 相关系数 \rho_{u,h} = \text{Corr}(\lambda

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

量化更新率与热度的相关性系数 \rho_{u,h}：通过业务日志计算 Pearson 相关系数 \rho_{u,h} = \text{Corr}(\lambda_i, p_i)，若 |\rho_{u,h}| < 0.1 则独立假设成立，否则需引入修正因子 \lambda_i = \lambda_{base} \cdot (1 + \rho_{u,h} \cdot \log(p_i/p_{avg}))。

## Corrected Claim

量化更新率与热度的相关性系数 ρ_{u,h} 可通过业务日志计算 Pearson 相关系数。若相关性较弱（如 |ρ_{u,h}| 低于特定阈值），可假设独立；否则需引入修正因子。具体阈值（如0.1）及修正公式形式需根据实际业务数据分布和模型验证结果确定。

## Evidence

[质询]该陈述包含具体的工程经验阈值（|ρ| < 0.1）和特定的修正公式形式，属于经验事实而非第一性原理可推导的数学恒等式；且检索无可用来源，无法验证该特定阈值和公式是否为业界标准或该特定业务场景下的既定事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体阈值0.1及修正公式的合理性）

## Search Query

correlation between object update frequency and request popularity in CDN cache invalidation models
