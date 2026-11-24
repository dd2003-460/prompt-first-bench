# N8: 日均缓存命中流量比例 H_traffic = (H_img * F_img + H_video * F_video)，其中 H_img 为图片缓存命中率（通常 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

日均缓存命中流量比例 H_traffic = (H_img * F_img + H_video * F_video)，其中 H_img 为图片缓存命中率（通常 80-95%），H_video 为短视频缓存命中率（通常 40-60%），F_img 和 F_video 分别为图片和视频流量占比。

## Corrected Claim

日均缓存命中流量比例 H_traffic = (H_img * F_img + H_video * F_video)，其中 H_img 为图片缓存命中率（通常 80-95%），H_video 为短视频缓存命中率（通常 40-60%），F_img 和 F_video 分别为图片和视频流量占比。

## Evidence

父节点级核验未通过：不完备（子节点定义了流量占比（F）和对象大小（s），但完全缺失了父节点公式中核心的命中率参数（H_img, H_video），导致无法计算最终结果，完备性不足。）
