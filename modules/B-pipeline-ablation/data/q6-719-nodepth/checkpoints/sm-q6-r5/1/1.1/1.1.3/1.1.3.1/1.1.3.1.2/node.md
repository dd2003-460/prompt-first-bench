# N450: 图片主导工作点下的单请求传输延迟 L_trans_img = s_avg / Bandwidth = 0.67 MB / (10 Gbps / 8) ≈ 0.5

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

图片主导工作点下的单请求传输延迟 L_trans_img = s_avg / Bandwidth = 0.67 MB / (10 Gbps / 8) ≈ 0.54 ms (假设边缘出口带宽为 10 Gbps 共享，实际需除以并发连接数，此处为单流上限估算)，显著低于视频工作点。

## Corrected Claim

图片主导工作点下的单请求传输延迟 L_trans_img = s_avg / Bandwidth = 0.67 MB / (10 Gbps / 8) ≈ 0.54 ms (假设边缘出口带宽为 10 Gbps 共享，实际需除以并发连接数，此处为单流上限估算)，显著低于视频工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：0.67MB * 8 / 10Gbps = 0.536ms，计算准确且量级合理。
