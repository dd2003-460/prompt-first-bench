# N197: 权重 w_img 和 w_video 的确定：基于请求量占比，w_img = 60%（图片请求占比），w_video = 40%（短视频请求占比）；T_targ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

权重 w_img 和 w_video 的确定：基于请求量占比，w_img = 60%（图片请求占比），w_video = 40%（短视频请求占比）；T_target = 0.6 * 100ms + 0.4 * 500ms = 260ms；此加权方式假设各类型请求对用户体验贡献线性可加

## Corrected Claim

权重 w_img 和 w_video 的确定：基于请求量占比，w_img = 60%（图片请求占比），w_video = 40%（短视频请求占比）；T_target = 0.6 * 100ms + 0.4 * 500ms = 260ms；此加权方式假设各类型请求对用户体验贡献线性可加

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.6*100 + 0.4*500 = 60 + 200 = 260ms 正确，线性可加假设在工程估算中合理。
