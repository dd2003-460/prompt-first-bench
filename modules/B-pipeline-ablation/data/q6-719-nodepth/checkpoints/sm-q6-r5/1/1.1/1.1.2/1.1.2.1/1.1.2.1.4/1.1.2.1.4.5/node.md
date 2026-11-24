# N1270: 低码率策略引入的转码预处理成本 C_transcode = (N_requests_video * C_transcode_per_req)，假设日均视频请求 

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N434

## Claim

低码率策略引入的转码预处理成本 C_transcode = (N_requests_video * C_transcode_per_req)，假设日均视频请求 100 万次，单次转码成本 ¥0.001，则 C_transcode = 1,000,000 * 0.001 = ¥1,000/天 = ¥30,000/月，可能抵消带宽节约。

## Corrected Claim

低码率策略引入的转码预处理成本 C_transcode = (N_requests_video * C_transcode_per_req)，假设日均视频请求 100 万次，单次转码成本 ¥0.001，则 C_transcode = 1,000,000 * 0.001 = ¥1,000/天 = ¥30,000/月，可能抵消带宽节约。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 1,000,000 * 0.001 = 1,000 正确，月度换算 1,000 * 30 = 30,000 正确，量级符合常规转码成本估算逻辑。
