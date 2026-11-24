# N315: 高码率工作点（AV1/HEVC, 1080p, 60s, 8 Mbps）：s_vid = 60 MB，单请求带宽成本贡献 C_bw_vid = 60 * ¥0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

高码率工作点（AV1/HEVC, 1080p, 60s, 8 Mbps）：s_vid = 60 MB，单请求带宽成本贡献 C_bw_vid = 60 * ¥0.25/GB * 1000/1024 ≈ ¥0.014648/req，适用于长视频或极高画质需求，显著增加回源与边缘带宽压力。

## Corrected Claim

高码率工作点（AV1/HEVC, 1080p, 60s, 8 Mbps）：s_vid = 60 MB，单请求带宽成本贡献 C_bw_vid = 60 * ¥0.25/GB * 1000/1024 ≈ ¥0.014648/req，适用于长视频或极高画质需求，显著增加回源与边缘带宽压力。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 60MB * 0.25¥/GB * (1000/1024) ≈ 0.014648¥ 数学上自洽，且符合高码率视频传输的成本量级直觉。
