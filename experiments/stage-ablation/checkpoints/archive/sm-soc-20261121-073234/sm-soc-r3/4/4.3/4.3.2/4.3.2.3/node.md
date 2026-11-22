# N266: 平台历史数据拟合的具体样本量要求：为准确估计 α 值，至少需要 500 个不同噪音水平（σ_v²）的商品匹配记录，否则标准误过大，无法区分 α=1.5 与 α=

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

平台历史数据拟合的具体样本量要求：为准确估计 α 值，至少需要 500 个不同噪音水平（σ_v²）的商品匹配记录，否则标准误过大，无法区分 α=1.5 与 α=2.0。

## Corrected Claim

平台历史数据拟合需要足够的样本量以准确估计 α 值，样本量不足会导致标准误过大，难以区分相近的 α 值（如 1.5 与 2.0），具体阈值需根据实际数据分布和统计功效分析确定。

## Evidence

[质询]该陈述包含具体的经验性统计阈值（500个样本）和特定的参数区分能力（α=1.5 vs 2.0），这属于依赖具体数据分布、信噪比和模型结构的经验事实，无法仅从第一性原理或逻辑公理中严格推导得出。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

minimum sample size estimate elasticity coefficient matching time noise
