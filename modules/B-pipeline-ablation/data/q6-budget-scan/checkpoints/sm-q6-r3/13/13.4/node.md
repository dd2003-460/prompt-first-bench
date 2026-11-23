# N401: 短视频首帧加载延迟基准：首帧时间 $T_{first} = T_{network} + T_{decode} + T_{render}$，其中 $T_{deco

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

短视频首帧加载延迟基准：首帧时间 $T_{first} = T_{network} + T_{decode} + T_{render}$，其中 $T_{decode}$ 取决于视频编码格式（H.265 比 H.264 解码慢约 20%），行业 P99 目标通常为 500-800ms，受终端设备性能影响显著。

## Corrected Claim

短视频首帧加载延迟基准：首帧时间 $T_{first} = T_{network} + T_{decode} + T_{render}$，其中 $T_{decode}$ 取决于视频编码格式（H.265 比 H.264 解码慢约 20%），行业 P99 目标通常为 500-800ms，受终端设备性能影响显著。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

short video first frame load time P99 benchmark
