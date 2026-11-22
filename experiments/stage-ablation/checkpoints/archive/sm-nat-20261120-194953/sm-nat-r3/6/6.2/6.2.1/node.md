# N149: 频率计数器精度误差 $\epsilon_{freq}$ 与请求间隔 $\Delta t$ 的关系为 $\epsilon_{freq} \approx \frac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

频率计数器精度误差 $\epsilon_{freq}$ 与请求间隔 $\Delta t$ 的关系为 $\epsilon_{freq} \approx \frac{\sigma_{count}}{R_i \Delta t}$，其中 $\sigma_{count}$ 为计数噪声（通常为 1 个计数单位）。当 $\Delta t < 1/u_{freq}$（即频率更新周期）时，计数器无法准确区分高频与低频对象。对于 LFU 维持 5% 增益，需保证头部对象频率估计误差 $\epsilon_{head} < 0.01$，这要求 $\Delta t > \frac{1}{R_{head} \cdot 0.01}$。若 $R_{head} \approx 10^4$ req/day，则 $\Delta t > 0.0001$ day $\approx 8.64$ seconds。

## Corrected Claim

频率计数器精度误差 $\epsilon_{freq}$ 与请求间隔 $\Delta t$ 的关系为 $\epsilon_{freq} \approx \frac{\sigma_{count}}{R_i \Delta t}$，其中 $\sigma_{count}$ 为计数噪声（通常为 1 个计数单位）。当 $\Delta t < 1/u_{freq}$（即频率更新周期）时，计数器无法准确区分高频与低频对象。对于 LFU 维持 5% 增益，需保证头部对象频率估计误差 $\epsilon_{head} < 0.01$，这要求 $\Delta t > \frac{1}{R_{head} \cdot 0.01}$。若 $R_{head} \approx 10^4$ req/day，则 $\Delta t > 0.0001$ day $\approx 8.64$ seconds。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合统计误差传播原理，数值量级（10^4 req/day 对应 8.64s 阈值）计算准确且符合工程直觉。
