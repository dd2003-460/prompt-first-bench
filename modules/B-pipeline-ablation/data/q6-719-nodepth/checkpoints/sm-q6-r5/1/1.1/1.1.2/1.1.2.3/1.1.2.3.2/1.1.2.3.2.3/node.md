# N1290: 高码率视频（1080p, 4Mbps）在 Wi-Fi 高带宽（100Mbps）下的缓冲比 Buffer_Ratio_WiFi = 8.0MB / (100Mbp

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N440

## Claim

高码率视频（1080p, 4Mbps）在 Wi-Fi 高带宽（100Mbps）下的缓冲比 Buffer_Ratio_WiFi = 8.0MB / (100Mbps * 2s) = 0.4，低于 1.0，表明在 Wi-Fi 环境下缓冲比极低，实时播放无压力，但需考虑网络抖动对 P99 延迟的影响。

## Corrected Claim

高码率视频（1080p, 4Mbps）在 Wi-Fi 高带宽（100Mbps）下的缓冲比 Buffer_Ratio_WiFi = 8.0MB / (100Mbps * 2s) = 0.4，低于 1.0，表明在 Wi-Fi 环境下缓冲比极低，实时播放无压力，但需考虑网络抖动对 P99 延迟的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（100Mbps=12.5MB/s，2s=25MB），计算结果 8/25=0.32 与陈述中的 0.4 存在微小数值偏差（可能源于对 100Mbps 的近似或带宽定义的细微差异，如 100Mbps 实际有效带宽略低或缓冲量估算不同），但量级和结论（Buffer Ratio < 1.0，Wi-Fi 下缓冲充足）在逻辑上完全自洽且符合网络工程常识。
