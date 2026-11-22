# N171: 信号强度 s_signal 的计算公式：s_signal = α * (P_high / P_low) + β * R_good + γ * N_reviews

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54, N55, N56

## Claim

信号强度 s_signal 的计算公式：s_signal = α * (P_high / P_low) + β * R_good + γ * N_reviews，其中 α, β, γ 为权重系数，R_good 为卖家好评率，N_reviews 为评价数量，需通过逻辑回归模型拟合买家咨询概率与这三个变量的关系以确定系数。

## Corrected Claim

信号强度 s_signal 可通过线性加权模型估算，形式如 s_signal = α * (P_high / P_low) + β * R_good + γ * N_reviews，其中系数需基于特定数据集通过逻辑回归等统计方法拟合，而非通用固定公式。

## Evidence

[质询]该公式为特定经验模型，非通用物理或数学定律，且具体系数（α, β, γ）及变量组合方式（线性加权）缺乏通用标准支持，属于特定场景下的假设性建模。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该公式非第一性原理可推导的通用真理，而是特定业务场景下的统计模型假设）。

## Search Query

signal strength formula second hand marketplace price reputation reviews logistic regression
