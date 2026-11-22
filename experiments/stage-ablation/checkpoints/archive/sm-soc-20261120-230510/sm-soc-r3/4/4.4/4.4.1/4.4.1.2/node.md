# N231: 价格敏感度系数 β_price 的实证估计方法：β_price = (Δη/η_base) / (ΔP/P_median)，需基于平台 A/B 测试数据或历史降

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

价格敏感度系数 β_price 的实证估计方法：β_price = (Δη/η_base) / (ΔP/P_median)，需基于平台 A/B 测试数据或历史降价事件回归计算，典型值范围 [0.5, 1.5]，若 β_price < 0.5 则价格变动对转化率影响微弱，公式简化为 η ≈ η_base。

## Corrected Claim

价格敏感度系数 β_price 通常定义为转化率相对变化与价格相对变化之比，其具体数值范围及估计方法需依据特定平台的历史数据或A/B测试结果进行回归分析确定，不同行业和市场环境下典型值可能存在差异。

## Evidence

[质询]该陈述包含具体的经验性数值范围（典型值 [0.5, 1.5]）和特定的实证估计方法，属于经验事实而非第一性原理可推导的数学或逻辑恒等式。在缺乏外部来源支持的情况下，无法验证该特定数值范围和公式定义的普适性或准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

price sensitivity coefficient conversion rate A/B test second-hand marketplace
