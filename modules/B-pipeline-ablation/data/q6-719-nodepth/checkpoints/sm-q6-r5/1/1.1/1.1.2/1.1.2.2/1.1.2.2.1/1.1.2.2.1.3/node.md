# N1273: 标准工作点下，单请求传输延迟 L_transmission = s_video_total / B_link，在 10 Mbps 链路下 L_transmiss

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N435

## Claim

标准工作点下，单请求传输延迟 L_transmission = s_video_total / B_link，在 10 Mbps 链路下 L_transmission = 4.0MB / (10Mbps/8) = 3.2s；在 20 Mbps 链路下 L_transmission = 4.0MB / (20Mbps/8) = 1.6s。

## Corrected Claim

标准工作点下，单请求传输延迟 L_transmission = s_video_total / B_link，在 10 Mbps 链路下 L_transmission = 4.0MB / (10Mbps/8) = 3.2s；在 20 Mbps 链路下 L_transmission = 4.0MB / (20Mbps/8) = 1.6s。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（10Mbps=1.25MB/s, 20Mbps=2.5MB/s），计算结果准确（4.0/1.25=3.2s, 4.0/2.5=1.6s），符合物理直觉。
