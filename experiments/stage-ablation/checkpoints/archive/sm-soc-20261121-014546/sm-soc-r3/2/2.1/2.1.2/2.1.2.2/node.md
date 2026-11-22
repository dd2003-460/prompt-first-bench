# N190: 下游投影 1：SNR 临界值推导，SNR = ΔP / σ_buyer = (0.1·P_ask) / (0.1·P_ask) = 1.0，当 ΔP < 0.1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N54

## Claim

下游投影 1：SNR 临界值推导，SNR = ΔP / σ_buyer = (0.1·P_ask) / (0.1·P_ask) = 1.0，当 ΔP < 0.15·P_ask 时 SNR < 1.5，低于信号检测理论中区分信号与噪声所需的 d' = 1.0 阈值。

## Corrected Claim

下游投影 1：SNR 临界值推导，SNR = ΔP / σ_buyer = (0.1·P_ask) / (0.1·P_ask) = 1.0。当 ΔP < 0.15·P_ask 时 SNR < 1.5。在信号检测理论框架下，SNR=1.0 对应 d'=1.0，此时信号与噪声分布重叠较大，区分度有限（正确识别率约 76%），通常认为需要更高的 d' 值（如 >1.5）才能实现稳健的信号区分。

## Evidence

[质询]陈述中关于信号检测理论（SDT）的阈值引用存在概念混淆或数值错误。在标准信号检测理论中，d'（d-prime）是衡量信号与噪声分布分离程度的指标，其值取决于两个分布均值之差与标准差之比（即 SNR 的某种归一化形式）。通常，d'=1.0 对应约 76% 的正确识别率，并非一个绝对的“区分信号与噪声所需的阈值”（通常认为 d'>1.5 或 2.0 才具有较好的区分度，或者根据具体业务需求设定）。此外，将 SNR 直接等同于 d' 并设定 1.0 为硬性阈值缺乏通用的理论依据，属于对统计概念的简化或误用。 | 先验知识/题面给定，逻辑校验通过。数学推导部分（SNR=1.0 当 ΔP=0.1P_ask）自洽，但关于 SDT 阈值 d'=1.0 的定性描述在统计学上不够严谨，属于经验性/模型假设层面的表述，缺乏通用理论支持，故降级。

## Search Query

signal detection theory d prime threshold price discount noise
