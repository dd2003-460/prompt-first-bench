# N113: 共享随机源：买家搜索耐心阈值 $\delta_{patience}$ 的个体异质性由认知疲劳累积项 $\epsilon_{cog}$ 和外部干扰项 $\epsi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N33

## Claim

共享随机源：买家搜索耐心阈值 $\delta_{patience}$ 的个体异质性由认知疲劳累积项 $\epsilon_{cog}$ 和外部干扰项 $\epsilon_{ext}$ 共同驱动，其中 $\epsilon_{cog} \sim N(0, \sigma_{cog}^2)$ 代表注意力衰减的随机波动（$\sigma_{cog} \approx 0.15$ 小时，基于眼动追踪实验先验），$\epsilon_{ext} \sim N(0, \sigma_{ext}^2)$ 代表突发中断（如消息通知）的随机延迟（$\sigma_{ext} \approx 0.20$ 小时）。总耐心阈值 $\delta_{patience} = \mu_{patience} + \epsilon_{cog} + \epsilon_{ext}$，其复合标准差 $\sigma_{\delta} = \sqrt{\sigma_{cog}^2 + \sigma_{ext}^2} \approx 0.25$ 小时。

## Corrected Claim

共享随机源：买家搜索耐心阈值 $\delta_{patience}$ 的个体异质性由认知疲劳累积项 $\epsilon_{cog}$ 和外部干扰项 $\epsilon_{ext}$ 共同驱动，其中 $\epsilon_{cog} \sim N(0, \sigma_{cog}^2)$ 代表注意力衰减的随机波动（$\sigma_{cog} \approx 0.15$ 小时，基于眼动追踪实验先验），$\epsilon_{ext} \sim N(0, \sigma_{ext}^2)$ 代表突发中断（如消息通知）的随机延迟（$\sigma_{ext} \approx 0.20$ 小时）。总耐心阈值 $\delta_{patience} = \mu_{patience} + \epsilon_{cog} + \epsilon_{ext}$，其复合标准差 $\sigma_{\delta} = \sqrt{\sigma_{cog}^2 + \sigma_{ext}^2} \approx 0.25$ 小时。

## Evidence

先验知识/题面给定，逻辑校验通过：独立正态变量之和的方差为各方差之和，计算 sqrt(0.15^2 + 0.20^2) ≈ 0.25 正确，量纲一致。

## Search Query

user attention span variance marketplace search session duration noise
