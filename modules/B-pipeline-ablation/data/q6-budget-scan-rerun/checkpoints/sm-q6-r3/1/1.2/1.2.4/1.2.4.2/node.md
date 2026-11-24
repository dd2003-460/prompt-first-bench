# N119: 客户端解码/渲染时间 $T_{decode}$ 与编码格式及硬件加速相关。JPEG 解码耗时 $\approx 10-50$ms/MB（中端手机），H.264 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

客户端解码/渲染时间 $T_{decode}$ 与编码格式及硬件加速相关。JPEG 解码耗时 $\approx 10-50$ms/MB（中端手机），H.264 视频首帧解码耗时 $\approx 50-100$ms（取决于分辨率及是否启用 GPU 加速）。

## Corrected Claim

客户端解码/渲染时间 $T_{decode}$ 与编码格式及硬件加速相关。JPEG 解码耗时 $\approx 10-50$ms/MB（中端手机），H.264 视频首帧解码耗时 $\approx 50-100$ms（取决于分辨率及是否启用 GPU 加速）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

JPEG decode latency mobile CPU vs H264 first frame decode time GPU
