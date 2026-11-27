# N186: 频率估计误差 $\epsilon_{freq}$ 的量化模型：对于计数精度为 $b$ 位的 LFU 实现，$\epsilon_{freq}$ 近似为 $1/2^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

频率估计误差 $\epsilon_{freq}$ 的量化模型：对于计数精度为 $b$ 位的 LFU 实现，$\epsilon_{freq}$ 近似为 $1/2^b$。若 $b=16$，$\epsilon_{freq} \approx 0.000015$；若采用滑动窗口或指数衰减，$\epsilon_{freq}$ 取决于窗口长度 $W$ 与访问间隔 $\Delta t$ 的比值，通常 $\epsilon_{freq} \approx \min(1, \lambda_{acc}/W)$。

## Corrected Claim

频率估计误差 $\epsilon_{freq}$ 的量化模型：对于计数精度为 $b$ 位的 LFU 实现，$\epsilon_{freq}$ 近似为 $1/2^b$。若 $b=16$，$\epsilon_{freq} \approx 0.000015$；若采用滑动窗口或指数衰减，$\epsilon_{freq}$ 取决于窗口长度 $W$ 与访问间隔 $\Delta t$ 的比值，通常 $\epsilon_{freq} \approx \min(1, \lambda_{acc}/W)$。

## Evidence

先验知识/题面给定，逻辑校验通过：1/2^16 的数值计算正确（约 0.000015），滑动窗口误差模型符合信号处理与缓存理论的基本直觉。
