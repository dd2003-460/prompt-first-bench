# N146: 工作点 A（高清短视频主导）：设视频流量占比 F_video=0.7，图片占比 F_img=0.3；视频平均大小 s_video=4.0MB，图片 s_img=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

工作点 A（高清短视频主导）：设视频流量占比 F_video=0.7，图片占比 F_img=0.3；视频平均大小 s_video=4.0MB，图片 s_img=0.3MB。计算得 s_avg = 0.3*0.3 + 0.7*4.0 = 2.89 MB。此工况下缓存命中率 H 预计降至 75%（大文件长尾效应），带宽成本弹性系数 E_bw ≈ 1.2。

## Corrected Claim

工作点 A（高清短视频主导）：设视频流量占比 F_video=0.7，图片占比 F_img=0.3；视频平均大小 s_video=4.0MB，图片 s_img=0.3MB。计算得 s_avg = 0.3*0.3 + 0.7*4.0 = 2.89 MB。此工况下缓存命中率 H 预计降至 75%（大文件长尾效应），带宽成本弹性系数 E_bw ≈ 1.2。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.3*0.3 + 0.7*4.0 = 0.09 + 2.8 = 2.89 MB 正确；命中率与弹性系数为合理工程估算值。
