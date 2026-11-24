# N305: 工作点 B（中视频占比，中 s_avg）：假设 P_video=0.3, P_img=0.7，s_img=1MB, s_vid=10MB，则 s_avg = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

工作点 B（中视频占比，中 s_avg）：假设 P_video=0.3, P_img=0.7，s_img=1MB, s_vid=10MB，则 s_avg = 0.7*1 + 0.3*10 = 3.7MB。此工作点代表典型社交/内容混合平台，平衡带宽与请求数成本。

## Corrected Claim

工作点 B（中视频占比，中 s_avg）：假设 P_video=0.3, P_img=0.7，s_img=1MB, s_vid=10MB，则 s_avg = 0.7*1 + 0.3*10 = 3.7MB。此工作点代表典型社交/内容混合平台，平衡带宽与请求数成本。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.7*1 + 0.3*10 = 3.7 正确，量纲一致，符合混合内容平台典型特征。
