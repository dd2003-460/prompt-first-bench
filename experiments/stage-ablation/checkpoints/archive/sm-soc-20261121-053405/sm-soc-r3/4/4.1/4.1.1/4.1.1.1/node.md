# N170: 共享随机源：定义回归误差项 $\epsilon$ 的分布参数为 $\epsilon \sim N(0, \sigma_{\epsilon}^2)$，其中 $\s

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

共享随机源：定义回归误差项 $\epsilon$ 的分布参数为 $\epsilon \sim N(0, \sigma_{\epsilon}^2)$，其中 $\sigma_{\epsilon}$ 为残差标准差，其数值取决于 $T_{cycle}$ 的测量精度（通常含 $\sigma_{data}$ 成分）及模型设定误差（遗漏变量偏差），需通过历史数据残差分析估计，典型值在 [1.5, 3.0] 天区间。

## Corrected Claim

共享随机源：定义回归误差项 $\epsilon$ 的分布参数为 $\epsilon \sim N(0, \sigma_{\epsilon}^2)$，其中 $\sigma_{\epsilon}$ 为残差标准差，其数值取决于 $T_{cycle}$ 的测量精度及模型设定误差，需通过历史数据残差分析估计，具体量级依业务场景而定。

## Evidence

[质询]典型值区间 [1.5, 3.0] 天缺乏普适性，高度依赖于具体的业务场景（如物流、制造、金融）和数据频率，将其作为通用‘典型值’陈述存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值区间属于经验事实，缺乏通用来源支持，故降级。

## Search Query

regression residual standard error time-to-event data marketplace
