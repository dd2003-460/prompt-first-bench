# N319: 图片对象平均大小s_img的低成本工作点：s_img = 200KB，对应JPEG压缩质量Q=70，分辨率1080x1080，适用于缩略图/列表页场景，带宽成本

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

图片对象平均大小s_img的低成本工作点：s_img = 200KB，对应JPEG压缩质量Q=70，分辨率1080x1080，适用于缩略图/列表页场景，带宽成本最低，但视觉质量下降，用户投诉率可能上升5-10%。

## Corrected Claim

图片对象平均大小s_img的低成本工作点：s_img = 200KB，对应JPEG压缩质量Q=70，分辨率1080x1080，适用于缩略图/列表页场景，带宽成本较低，但视觉质量下降，可能导致部分用户满意度降低。

## Evidence

[质询]「用户投诉率可能上升5-10%」属于具体的经验统计数据，缺乏通用性，不同业务场景、用户群体及竞品对比下该数值波动极大，无法作为通用工程事实成立。 | 先验知识/题面给定，逻辑校验通过：200KB/1080x1080/Q70在工程上确实是常见的低成本平衡点，但投诉率具体数值缺乏来源支持且非普适真理。

## Search Query

image compression size 200kb jpeg quality 70 social media
