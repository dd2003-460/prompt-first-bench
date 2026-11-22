# N279: 流动性枯竭修正项 δ_liquidity 的函数形式定义为 δ_liquidity = 1 / (1 + e^(-(P_ask - (V + 3σ)) / τ_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

流动性枯竭修正项 δ_liquidity 的函数形式定义为 δ_liquidity = 1 / (1 + e^(-(P_ask - (V + 3σ)) / τ_liquid))，其中 τ_liquid 为流动性衰减尺度参数，需通过历史长尾交易数据回归校准

## Corrected Claim

流动性枯竭修正项 δ_liquidity 通常被建模为关于价差或偏离度的单调函数（如 Sigmoid 形式），具体函数形式及参数（如 V + 3σ 和 τ_liquid）需依据特定模型假设并通过历史数据回归校准。

## Evidence

[质询]该陈述定义了一个具体的数学函数形式（Sigmoid 函数）及特定的参数组合（V + 3σ），这属于经验性的模型设定而非第一性原理可推导的数学恒等式或物理定律。在缺乏具体文献或标准定义支持的情况下，无法确认该特定函数形式是行业通用标准还是特定模型的任意假设。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

liquidity decay function long tail transactions e-commerce calibration
