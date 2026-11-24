# N1261: Buffer_Ratio 公式中的 T_buffer_window 应基于用户感知阈值设定：通常 T_buffer_window = 2s 为行业基准（确保 2

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N431, N432, N433

## Claim

Buffer_Ratio 公式中的 T_buffer_window 应基于用户感知阈值设定：通常 T_buffer_window = 2s 为行业基准（确保 2 秒内无卡顿），但若视频为短视频（15s 总长），预加载策略可将 T_buffer_window 扩展至 T_preload = T_video_duration / 3 = 5s，此时 Buffer_Ratio = 2.0MB / (1.5Mbps * 5s) = 2.0 * 8 / (1.5 * 5) = 2.13，仍高于 1.0，表明即使预加载 5 秒，弱网下仍需依赖分段缓存或降码率策略。

## Corrected Claim

Buffer_Ratio 公式中的 T_buffer_window 应基于用户感知阈值设定：通常 T_buffer_window = 2s 为行业基准（确保 2 秒内无卡顿），但若视频为短视频（15s 总长），预加载策略可将 T_buffer_window 扩展至 T_preload = T_video_duration / 3 = 5s，此时 Buffer_Ratio = 2.0MB / (1.5Mbps * 5s) = 2.0 * 8 / (1.5 * 5) = 2.13，仍高于 1.0，表明即使预加载 5 秒，弱网下仍需依赖分段缓存或降码率策略。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 2.0*8/(1.5*5) ≈ 2.13 正确，单位换算（Mbps到MB/s）逻辑自洽，结论符合流媒体缓冲原理。

## Search Query

video streaming buffer window size optimization weak network
