# N296: 似然比 LR = P(Data|H1) / P(Data|H0) 的计算：基于 N60 的显著性检验 p<0.01，假设检验统计量 Z=2.33，则 LR ≈ 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

似然比 LR = P(Data|H1) / P(Data|H0) 的计算：基于 N60 的显著性检验 p<0.01，假设检验统计量 Z=2.33，则 LR ≈ exp(0.5 * Z²) ≈ 3.0；需明确 H0（高溢价无高曝光）下的数据分布假设，以计算精确的似然比，支撑后验概率 0.85 的推导。

## Corrected Claim

在 H0 和 H1 均为正态分布且方差相同的假设下，基于 Z=2.33，LR ≈ exp(0.5 * Z²) ≈ 3.0；若分布假设不同，需重新计算精确似然比以支撑后验概率 0.85 的推导。

## Evidence

[质询]LR ≈ exp(0.5 * Z²) 这一近似公式仅在特定条件下成立（如 H0 和 H1 均为正态分布且方差相同，H1 的均值偏移量与 Z 统计量直接对应），若 H0 和 H1 的分布假设不同（例如方差不同或 H1 为复合假设），该公式不成立。此外，Z=2.33 对应的单侧 p 值约为 0.01，但 LR 的计算依赖于具体的效应量和样本量，仅凭 Z 值无法唯一确定 LR，除非假设 H1 是点假设且与 H0 具有相同的方差结构。 | 先验知识/题面给定，逻辑校验通过，但 LR 的近似公式依赖特定分布假设，缺乏来源支持其普适性，故降级为定性表述。

## Search Query

likelihood ratio from p-value in Bayesian hypothesis testing
