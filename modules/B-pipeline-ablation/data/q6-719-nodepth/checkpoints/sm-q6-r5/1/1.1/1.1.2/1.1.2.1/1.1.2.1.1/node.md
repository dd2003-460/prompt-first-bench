# N431: 低码率工作点（720p H.265 @ 1 Mbps, 15s）的精确文件体积 s_video = (1 Mbps / 8) * 15 s = 1.875 MB

- **status**: pending
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

低码率工作点（720p H.265 @ 1 Mbps, 15s）的精确文件体积 s_video = (1 Mbps / 8) * 15 s = 1.875 MB，加上容器开销约 0.125 MB，总计 2.0 MB；该值直接决定单次请求的传输延迟项 L_transmission = s_video / B_link 和带宽成本项 C_bw = s_video * P_bw。

## Corrected Claim

低码率工作点（720p H.265 @ 1 Mbps, 15s）的精确文件体积 s_video = (1 Mbps / 8) * 15 s = 1.875 MB，加上容器开销约 0.125 MB，总计 2.0 MB；该值直接决定单次请求的传输延迟项 L_transmission = s_video / B_link 和带宽成本项 C_bw = s_video * P_bw。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 880)
