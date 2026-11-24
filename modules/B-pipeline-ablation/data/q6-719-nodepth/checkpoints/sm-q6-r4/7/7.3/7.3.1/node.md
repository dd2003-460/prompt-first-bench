# N537: P_img 的基准工作点：基于微信/Instagram 等头部平台日志统计，图片加载请求占比稳定在 65%-75% 区间，取中值 P_img=0.70 作为成本

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N177

## Claim

P_img 的基准工作点：基于微信/Instagram 等头部平台日志统计，图片加载请求占比稳定在 65%-75% 区间，取中值 P_img=0.70 作为成本模型默认输入，该值受平台内容策略（如是否强制加载缩略图）影响，波动范围 ±5%。

## Corrected Claim

P_img 的基准工作点：基于微信/Instagram 等头部平台日志统计，图片加载请求占比稳定在 65%-75% 区间，取中值 P_img=0.70 作为成本模型默认输入，该值受平台内容策略（如是否强制加载缩略图）影响，波动范围 ±5%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

social media platform image vs video request ratio statistics
