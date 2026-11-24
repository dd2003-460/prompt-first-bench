# N65: 带宽成本地域差异：一线城市BGP带宽价格 ¥/Gbps/month ≈ 2,000-3,000，三四线城市 ≈ 1,000-1,500；混合策略中核心区域带宽成

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

带宽成本地域差异：一线城市BGP带宽价格 ¥/Gbps/month ≈ 2,000-3,000，三四线城市 ≈ 1,000-1,500；混合策略中核心区域带宽成本权重 = 0.6 * High_Price + 0.4 * Low_Price。

## Corrected Claim

一线城市BGP带宽价格通常高于三四线城市，具体数值需参考实时市场报价；混合策略成本权重需根据实际业务分布确定。

## Evidence

[质询]参考来源均与带宽成本无关，无法提供外部证据支持具体的价格数值（¥/Gbps/month）及权重系数（0.6/0.4），属于缺乏来源支持的经验事实。 | 逻辑自洽（一线城市带宽成本高于三四线城市符合市场常识，加权公式数学上成立），但参考来源[1][2][3]均涉及薪资、通胀或关税，与带宽成本主题完全无关，无可用外部证据支持具体数值。

## Search Query

China BGP bandwidth price per Gbps monthly 2024 tier 1 vs tier 3 cities

## Retrieval Sources

- {'url': 'https://thinkmatrix.blog/minimum-salary-china-guide&rut=0f3a88f0dfc477ede86a2fc99dfec74f6743330b2b6502565e761a0e5e4ab853', 'type': 'ddg', 'title': 'Minimum Salary in China: [2024 Regional Guide for US Businesses]'}
- {'url': 'https://www.statista.com/statistics/271667/monthly-inflation-rate-in-china/&rut=96aed0a01eeb1cf143644bea40edc8ed645bed420290b05d8c79867aee2b7e23', 'type': 'ddg', 'title': 'China: monthly inflation rate 2026 | Statista'}
- {'url': 'https://tariffos.com/en/measures/section-301-china-tariffs&rut=10b7ef09418914afd4fabb7f801d27c43ece4b1646feabc808458e259cc66e42', 'type': 'ddg', 'title': 'Section 301 tariffs on China (Lists 1-4A and 2024 strategic increases)'}
