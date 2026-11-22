# N107: 自然实验数据中‘流量波动标准差 $\sigma_{traffic}$’的基准估计：在缺乏A/B测试数据时，可利用平台历史数据计算每日流量变异系数 $CV_{da

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

自然实验数据中‘流量波动标准差 $\sigma_{traffic}$’的基准估计：在缺乏A/B测试数据时，可利用平台历史数据计算每日流量变异系数 $CV_{daily} = \sigma_{daily} / \mu_{daily}$。典型二手平台 $CV_{daily}$ 约为 0.1-0.2，据此可推算单商品层面的 $\sigma_{traffic}$，作为贝叶斯估计中 $\sigma_{data}$ 的替代输入。

## Corrected Claim

自然实验数据中‘流量波动标准差 $\sigma_{traffic}$’的基准估计：在缺乏A/B测试数据时，可利用平台历史数据计算每日流量变异系数 $CV_{daily} = \sigma_{daily} / \mu_{daily}$。典型二手平台 $CV_{daily}$ 约为 0.1-0.2，据此可推算单商品层面的 $\sigma_{traffic}$，作为贝叶斯估计中 $\sigma_{data}$ 的替代输入。

## Evidence

先验知识/题面给定，逻辑校验通过
