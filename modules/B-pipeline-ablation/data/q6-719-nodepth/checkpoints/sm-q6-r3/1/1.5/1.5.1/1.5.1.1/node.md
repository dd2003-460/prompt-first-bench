# N184: 对象大小分布对 T_transfer 的影响：图片对象 s_img ≈ 500KB，短视频对象 s_vid ≈ 10MB；混合请求中图片占比 80%（按请求数）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

对象大小分布对 T_transfer 的影响：图片对象 s_img ≈ 500KB，短视频对象 s_vid ≈ 10MB；混合请求中图片占比 80%（按请求数），则平均传输对象大小 s_avg_req = 0.8×0.5MB + 0.2×10MB = 2.4MB；T_transfer_avg = 2.4MB / Effective_Bandwidth。

## Corrected Claim

对象大小分布对 T_transfer 的影响：图片对象 s_img ≈ 500KB，短视频对象 s_vid ≈ 10MB；混合请求中图片占比 80%（按请求数），则平均传输对象大小 s_avg_req = 0.8×0.5MB + 0.2×10MB = 2.4MB；T_transfer_avg = 2.4MB / Effective_Bandwidth。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.8*0.5 + 0.2*10 = 0.4 + 2.0 = 2.4MB 正确，量纲一致。
