# N203: 工作点B（低价格敏感度/高噪声）：定义浏览型点击率 CTR_browse = CTR_total - CTR_price，基准值 CTR_browse_base

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

工作点B（低价格敏感度/高噪声）：定义浏览型点击率 CTR_browse = CTR_total - CTR_price，基准值 CTR_browse_base = 1.0% (假设基准CTR 2.5%中的40%为浏览噪声)，价格弹性系数 ε_ctr_browse ≈ -0.2 (弱敏感)，代表算法推荐或视觉吸引导致的非理性点击，用于隔离噪声。

## Corrected Claim

工作点B（低价格敏感度/高噪声）：定义浏览型点击率 CTR_browse = CTR_total - CTR_price，基准值 CTR_browse_base = 1.0% (假设基准CTR 2.5%中的40%为浏览噪声)，价格弹性系数 ε_ctr_browse ≈ -0.2 (弱敏感)，代表算法推荐或视觉吸引导致的非理性点击，用于隔离噪声。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

non-price sensitive clicks in e-commerce browsing behavior
