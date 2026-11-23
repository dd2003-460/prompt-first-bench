# N302: 混合内容Zipf参数α_hybrid的加权公式：α_hybrid = (V_img * α_img + V_video * α_video) / (V_img 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

混合内容Zipf参数α_hybrid的加权公式：α_hybrid = (V_img * α_img + V_video * α_video) / (V_img + V_video)，其中V_img和V_video为日均图片/短视频下载量（GB）；基于2TB总下载量，若图片占500GB、视频占1.5TB，则α_hybrid ≈ 0.9-1.0

## Corrected Claim

混合内容Zipf参数α_hybrid的加权公式：α_hybrid = (V_img * α_img + V_video * α_video) / (V_img + V_video)，其中V_img和V_video为日均图片/短视频下载量（GB）；基于2TB总下载量，若图片占500GB、视频占1.5TB，则α_hybrid ≈ 0.9-1.0

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式在数学上自洽，且0.9-1.0的Zipf指数符合混合媒体流量分布的经验量级。
