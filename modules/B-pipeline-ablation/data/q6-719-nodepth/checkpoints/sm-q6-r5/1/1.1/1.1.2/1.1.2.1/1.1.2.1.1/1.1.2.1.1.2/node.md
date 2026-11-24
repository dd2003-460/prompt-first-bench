# N1259: 在弱网环境（带宽 B_link = 1.5 Mbps）下，2.0MB 视频的纯传输延迟 L_transmission = s_video / B_link = 

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N431, N432, N433

## Claim

在弱网环境（带宽 B_link = 1.5 Mbps）下，2.0MB 视频的纯传输延迟 L_transmission = s_video / B_link = (2.0 * 8) / 1.5 = 10.67 秒；若考虑 TCP 慢启动效应（初始窗口 10 MSS ≈ 14.5KB，每 RTT 翻倍），假设 RTT=100ms，前 10 个 RTT 仅传输 ~14.5KB * (2^10 - 1) ≈ 14.5MB，但受限于 1.5Mbps 带宽上限，实际传输时间仍由带宽瓶颈主导，L_transmission ≈ 10.67s 是下限估计。

## Corrected Claim

在弱网环境（带宽 B_link = 1.5 Mbps）下，2.0MB 视频的纯传输延迟 L_transmission = s_video / B_link = (2.0 * 8) / 1.5 = 10.67 秒；若考虑 TCP 慢启动效应（初始窗口 10 MSS ≈ 14.5KB，每 RTT 翻倍），假设 RTT=100ms，前 10 个 RTT 仅传输 ~14.5KB * (2^10 - 1) ≈ 14.5MB，但受限于 1.5Mbps 带宽上限，实际传输时间仍由带宽瓶颈主导，L_transmission ≈ 10.67s 是下限估计。

## Evidence

先验知识/题面给定，逻辑校验通过：传输延迟计算 (16Mbit/1.5Mbps≈10.67s) 正确；TCP慢启动在100ms RTT下10个RTT传输量约14.5MB，远超2MB视频大小，故带宽瓶颈主导，结论自洽。

## Search Query

TCP slow start impact on file download time low bandwidth
