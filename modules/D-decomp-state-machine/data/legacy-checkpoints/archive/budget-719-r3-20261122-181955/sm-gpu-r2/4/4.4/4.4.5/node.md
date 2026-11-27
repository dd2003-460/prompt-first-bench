# N112: 敏感性分析（Sobol 指数）：计算每个输入变量（价格、精度损失、电价）对 TCO 方差贡献的 Sobol 第一阶指数 S1；识别 S1 > 0.5 的关键变量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N32

## Claim

敏感性分析（Sobol 指数）：计算每个输入变量（价格、精度损失、电价）对 TCO 方差贡献的 Sobol 第一阶指数 S1；识别 S1 > 0.5 的关键变量；例如，GPU 价格通常是最敏感变量，而精度损失对 TCO 影响较小，但对用户体验（是否满足业务阈值）影响显著。

## Corrected Claim

敏感性分析（Sobol 指数）：计算每个输入变量（价格、精度损失、电价）对 TCO 方差贡献的 Sobol 第一阶指数 S1；识别 S1 > 0.5 的关键变量；例如，GPU 价格通常是最敏感变量，而精度损失对 TCO 影响较小，但对用户体验（是否满足业务阈值）影响显著。

## Evidence

先验知识/题面给定，逻辑校验通过
