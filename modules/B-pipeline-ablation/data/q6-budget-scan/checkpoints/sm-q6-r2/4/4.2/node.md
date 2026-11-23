# N49: 图片与视频的请求比例 r_img : r_vid 通常约为 10:1 或 5:1（因图片加载频率远高于短视频）；假设 r_img=0.9, r_vid=0.1，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

图片与视频的请求比例 r_img : r_vid 通常约为 10:1 或 5:1（因图片加载频率远高于短视频）；假设 r_img=0.9, r_vid=0.1，则 s_avg = 0.9*500KB + 0.1*5MB = 950KB。

## Corrected Claim

图片与视频的请求比例 r_img : r_vid 通常约为 10:1 或 5:1（因图片加载频率远高于短视频）；假设 r_img=0.9, r_vid=0.1，则 s_avg = 0.9*500KB + 0.1*5MB = 950KB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.9*500 + 0.1*5000 = 450 + 500 = 950KB 正确，且图片与视频请求比例及平均大小符合常见CDN/网络流量经验分布。

## Search Query

image vs video request ratio social media platform
