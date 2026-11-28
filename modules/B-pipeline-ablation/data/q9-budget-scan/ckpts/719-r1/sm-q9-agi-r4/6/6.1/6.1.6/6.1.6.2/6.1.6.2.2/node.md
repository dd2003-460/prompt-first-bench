# N714: 寿命缩短比例 43% 是基于稳态温度假设的静态计算，实际服务器负载波动导致温度呈非稳态分布，需引入 Arrhenius 积分模型 ∫k(T(t))dt 来计算累

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N262

## Claim

寿命缩短比例 43% 是基于稳态温度假设的静态计算，实际服务器负载波动导致温度呈非稳态分布，需引入 Arrhenius 积分模型 ∫k(T(t))dt 来计算累积损伤，若平均温度从 85°C 升至 90°C，累积寿命损耗率将非线性增加，需模拟典型推理负载的温度曲线

## Corrected Claim

寿命缩短比例 43% 是基于稳态温度假设的静态计算，实际服务器负载波动导致温度呈非稳态分布，需引入 Arrhenius 积分模型 ∫k(T(t))dt 来计算累积损伤，若平均温度从 85°C 升至 90°C，累积寿命损耗率将非线性增加，需模拟典型推理负载的温度曲线

## Evidence

先验知识/题面给定，逻辑校验通过：Arrhenius方程描述了化学反应速率随温度变化的指数关系，在电子器件可靠性工程中，累积损伤确实通过积分形式 ∫k(T(t))dt 计算，且由于指数特性，温度升高会导致寿命损耗率非线性增加，符合物理直觉和工程常识。

## Search Query

non-steady state thermal aging Arrhenius integral cumulative damage GPU lifetime estimation
