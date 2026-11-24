# N306: 工作点 C（低视频占比，低 s_avg）：假设 P_video=0.1, P_img=0.9，s_img=0.5MB, s_vid=5MB，则 s_avg = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

工作点 C（低视频占比，低 s_avg）：假设 P_video=0.1, P_img=0.9，s_img=0.5MB, s_vid=5MB，则 s_avg = 0.9*0.5 + 0.1*5 = 0.95MB。此工作点代表图片主导平台，请求数主导，缓存命中率影响更大。

## Corrected Claim

工作点 C（低视频占比，低 s_avg）：假设 P_video=0.1, P_img=0.9，s_img=0.5MB, s_vid=5MB，则 s_avg = 0.9*0.5 + 0.1*5 = 0.95MB。此工作点代表图片主导平台，请求数主导，缓存命中率影响更大。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.9*0.5 + 0.1*5 = 0.45 + 0.5 = 0.95MB 正确，且低视频占比确实意味着请求数主导，符合缓存原理。
