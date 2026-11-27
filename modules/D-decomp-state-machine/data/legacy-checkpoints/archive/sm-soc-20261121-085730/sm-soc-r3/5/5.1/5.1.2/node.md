# N106: 模型复杂度 c_model 的量化指标：c_model = 1 - (AIC_model / AIC_benchmark)，其中AIC_model为当前模型赤池

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

模型复杂度 c_model 的量化指标：c_model = 1 - (AIC_model / AIC_benchmark)，其中AIC_model为当前模型赤池信息量，AIC_benchmark为基准模型（如线性回归）的AIC值，通常行为经济学模型c_model在0.5-0.8之间[待核验]

## Corrected Claim

AIC（赤池信息准则）用于衡量模型拟合优度与复杂度的平衡，公式为 AIC = 2k - 2ln(L)，其中k为参数个数，L为最大似然值。来源未提供 c_model = 1 - (AIC_model / AIC_benchmark) 这一特定指标的定义或行为经济学中的典型数值范围。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了公式中的分母（基准模型定义）、分子中的核心变量（模型参数与AIC计算）以及结果的判据（阈值与处理策略）。三者分别对应输入定义、计算细节和输出解释，逻辑上相互独立且互补，无重复或矛盾。）

## Search Query

model complexity metric AIC comparison behavioral economics models

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_43300144/article/details/115709484&rut=a9f8b1dc63e7edae447e71adcdbbf6e7dfdbe5a7cc92cd7a38d9831842b18b13', 'type': 'ddg', 'title': '一文帮你理解模型选择方法：AIC、BIC和交叉验证!_gcv广义交叉验证越小越好-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_33212799/article/details/165640831&rut=9d562d5d96f46e88fa74077398f9f6673dcc3f6d4d1a06a65397599efe558f1c', 'type': 'ddg', 'title': 'Aic与bic模型选择准则：原理、计算与实操避坑指南-csdn博客'}
