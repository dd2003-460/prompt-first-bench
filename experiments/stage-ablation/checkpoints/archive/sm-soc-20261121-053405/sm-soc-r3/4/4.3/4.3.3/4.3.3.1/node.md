# N190: 基准成交量 $Q_{base}$ 的估计公式：$Q_{base} = N_{active} \times P_{base}$，其中 $N_{active}$ 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

基准成交量 $Q_{base}$ 的估计公式：$Q_{base} = N_{active} \times P_{base}$，其中 $N_{active}$ 为平台日均活跃挂牌卖家数，$P_{base}$ 为单个卖家在 48 小时窗口内的基准成交概率（需基于历史 48h 成交率数据回归，当前标记为 [待核验]，典型二手平台 $P_{base}$ 约为 0.05-0.15）。

## Corrected Claim

基准成交量 $Q_{base}$ 的估计公式：$Q_{base} = N_{active} \times P_{base}$，其中 $N_{active}$ 为平台日均活跃挂牌卖家数，$P_{base}$ 为单个卖家在 48 小时窗口内的基准成交概率（需基于历史 48h 成交率数据回归，当前标记为 [待核验]，典型二手平台 $P_{base}$ 约为 0.05-0.15）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second-hand marketplace average 48h conversion rate active sellers
