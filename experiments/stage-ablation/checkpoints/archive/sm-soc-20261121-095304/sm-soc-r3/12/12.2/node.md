# N203: 似然函数 L(Data | High_Price -> Short_Cycle) 的构建：基于观测到的成交周期缩短幅度 ΔT/T_base，假设 ΔT 服从正态

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

似然函数 L(Data | High_Price -> Short_Cycle) 的构建：基于观测到的成交周期缩短幅度 ΔT/T_base，假设 ΔT 服从正态分布 N(μ_causal, σ²_data)，其中 μ_causal 为因果效应均值（估计值 0.2-0.3），σ²_data 为数据方差。似然值取决于观测值与 μ_causal 的距离。

## Corrected Claim

似然函数 L(Data | High_Price -> Short_Cycle) 的构建：基于观测到的成交周期缩短幅度 ΔT/T_base，假设 ΔT 服从正态分布 N(μ_causal, σ²_data)，其中 μ_causal 为因果效应均值（估计值 0.2-0.3），σ²_data 为数据方差。似然值取决于观测值与 μ_causal 的距离。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

likelihood function causal effect estimation normal distribution pricing data
