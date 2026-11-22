# N190: 在 w_price = 0 且 w_speed > w_ctr 条件下，溢价率 20% 商品相比 0% 商品的曝光量提升倍数 ΔExposure ≈ 1 + (

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N60

## Claim

在 w_price = 0 且 w_speed > w_ctr 条件下，溢价率 20% 商品相比 0% 商品的曝光量提升倍数 ΔExposure ≈ 1 + (w_speed * β_speed * 0.2) / (w_ctr * β_ctr * 0.2)，其中 β_speed 为速度对成交率的敏感度，β_ctr 为点击率敏感度，需通过 A/B 测试标定。

## Corrected Claim

在特定加权排序模型中，若忽略价格权重且速度权重高于点击率权重，溢价商品的曝光提升倍数可近似表示为速度项与点击率项加权敏感度之比，具体系数需通过A/B测试标定。

## Evidence

[质询]该公式为特定假设下的线性近似模型，缺乏通用性；且参考来源均为Facebook Marketplace的营销/算法科普文章，未提供具体的加权公式或敏感度系数（β）定义，无法证实该特定数学表达式的准确性。 | 逻辑上量纲自洽（比值无量纲），但属于经验事实/特定模型参数，参考来源[1][2][3]仅涉及Facebook Marketplace排名优化的一般性建议，未覆盖此具体公式，故降级。

## Search Query

second hand marketplace algorithm exposure boost price premium speed weight

## Retrieval Sources

- {'url': 'https://leadsbridge.com/blog/how-to-boost-facebook-marketplace/&rut=e3afcbe5b42664562a527a038972cc838c4b24510fc8d348bbda1ee5f7a10fe1', 'type': 'ddg', 'title': 'How to boost Facebook Marketplace ads and listings (2027 edition)'}
- {'url': 'https://infoxlog.com/the-facebook-marketplace-algorithm-explained-2026-guide/&rut=4268586a6e079577f2a5a93d92945b5a811d5605f47b049a7d67778cfd2abb3c', 'type': 'ddg', 'title': 'The Facebook Marketplace Algorithm Explained (2026 Guide)'}
- {'url': 'https://blog.dealflip.ai/blog/facebook-marketplace-algorithm&rut=b48f3227409357990091c9df862675406457a2e207e0dc9b82b863cca63808f3', 'type': 'ddg', 'title': '6 Meta Backed Fixes That Boost Facebook Marketplace Rank for Sellers'}
