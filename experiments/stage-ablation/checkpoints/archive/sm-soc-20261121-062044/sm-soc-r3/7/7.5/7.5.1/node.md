# N259: 定义曝光次数 (Impressions) 为商品详情页被加载的总次数，包含同一用户多次刷新或重复浏览，该指标作为咨询率分母时需满足日志记录粒度为 'page_v

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

定义曝光次数 (Impressions) 为商品详情页被加载的总次数，包含同一用户多次刷新或重复浏览，该指标作为咨询率分母时需满足日志记录粒度为 'page_view' 事件而非 'user_session' 事件，以区别于独立用户数。

## Corrected Claim

定义曝光次数 (Impressions) 为商品详情页被加载的总次数，包含同一用户多次刷新或重复浏览，该指标作为咨询率分母时需满足日志记录粒度为 'page_view' 事件而非 'user_session' 事件，以区别于独立用户数。

## Evidence

先验知识/题面给定，逻辑校验通过：Impressions 的标准定义即为页面加载次数（PV），与独立用户数（UV/Session）区分的关键在于统计粒度为 page_view 而非 user_session，逻辑自洽且符合行业通用定义。

## Search Query

e-commerce platform metric definition page view vs unique user session
