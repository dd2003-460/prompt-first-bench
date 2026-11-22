# N297: 卖家对算法权重变化的敏感度 $\sigma_s$ 的量化基准：定义为卖家调整挂价 $P_{ask}$ 对算法曝光权重 $W$ 变化的响应系数。在缺乏内部日志的情

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

卖家对算法权重变化的敏感度 $\sigma_s$ 的量化基准：定义为卖家调整挂价 $P_{ask}$ 对算法曝光权重 $W$ 变化的响应系数。在缺乏内部日志的情况下，可通过观察自然实验中 $W$ 波动（如季节性流量调整）引起的 $P_{ask}$ 分布变化来估计。若 $\sigma_s < 0.5$，则卖家行为惯性大，均衡难以通过微调 $W$ 打破；若 $\sigma_s > 1.0$，则卖家高度敏感。[待核验] 需结合平台公开的卖家定价指南更新频率与价格波动率数据进行校准。

## Corrected Claim

卖家对算法权重变化的敏感度 $\sigma_s$ 的量化基准：定义为卖家调整挂价 $P_{ask}$ 对算法曝光权重 $W$ 变化的响应系数。在缺乏内部日志的情况下，可通过观察自然实验中 $W$ 波动（如季节性流量调整）引起的 $P_{ask}$ 分布变化来估计。若 $\sigma_s < 0.5$，则卖家行为惯性大，均衡难以通过微调 $W$ 打破；若 $\sigma_s > 1.0$，则卖家高度敏感。[待核验] 需结合平台公开的卖家定价指南更新频率与价格波动率数据进行校准。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller price adjustment sensitivity to platform algorithm ranking weight changes empirical study
