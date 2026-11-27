# N154: 在 u=0.5 且 T_res/L_object=0.5 的工作点下，u*T_res=0.25 开始显现非线性效应，线性模型 δ=0.75 与指数模型 δ=ex

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

在 u=0.5 且 T_res/L_object=0.5 的工作点下，u*T_res=0.25 开始显现非线性效应，线性模型 δ=0.75 与指数模型 δ=exp(-0.25)≈0.779 的误差扩大至 3.9%，需采用指数模型进行修正

## Corrected Claim

在 u=0.5 且 T_res/L_object=0.5 的工作点下，u*T_res=0.25 开始显现非线性效应，线性模型 δ=0.75 与指数模型 δ=exp(-0.25)≈0.779 的误差扩大至 3.9%，需采用指数模型进行修正

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（0.75 vs 0.7788，相对误差约3.84%≈3.9%），物理/数学逻辑自洽（指数模型通常用于修正线性近似在特定参数下的偏差）。
