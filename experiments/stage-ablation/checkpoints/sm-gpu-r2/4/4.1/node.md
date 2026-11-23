# N16: 价格不确定性量化：定义价格波动系数 CV_price = σ_price / μ_price，基于2024Q4-2025Q1主流GPU（RTX 4090, A1

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

价格不确定性量化：定义价格波动系数 CV_price = σ_price / μ_price，基于2024Q4-2025Q1主流GPU（RTX 4090, A100, H100）在主要渠道（Newegg, Amazon, 国内电商平台）的30日价格历史数据，计算各档位的CV值；若CV > 0.15，则标记为高不确定性变量，需在最终排序中引入价格区间下界/上界敏感性分析。

## Corrected Claim

价格不确定性量化：定义价格波动系数 CV_price = σ_price / μ_price，基于近期主流GPU在主要渠道的价格历史数据计算CV值；若CV超过预设阈值（如0.15，需根据具体市场情况校准），则标记为高不确定性变量，需在最终排序中引入价格区间敏感性分析。

## Evidence

[质询]该陈述包含具体的经验性阈值（CV > 0.15）和特定的数据窗口（2024Q4-2025Q1），属于经验事实而非第一性原理可推导的数学或逻辑恒等式。在缺乏外部来源支持的情况下，无法验证该阈值在行业内的通用性或合理性，且具体数值可能因市场波动而异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该阈值非数学公理或物理定律，不适用第一性原理推导豁免）

## Search Query

RTX 4090 A100 H100 GPU price history 30 days 2025 volatility
