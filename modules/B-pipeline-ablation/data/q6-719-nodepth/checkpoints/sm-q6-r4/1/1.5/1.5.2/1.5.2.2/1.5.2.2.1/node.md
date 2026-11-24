# N551: 纯软件转码工作点：基于x264/FFmpeg CPU转码，单线程1080p 15s视频耗时约为视频时长的2-3倍（30-45s），P99 T_processin

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187

## Claim

纯软件转码工作点：基于x264/FFmpeg CPU转码，单线程1080p 15s视频耗时约为视频时长的2-3倍（30-45s），P99 T_processing_vid ≈ 30-45s，适用于低QPS、无硬件加速卡、追求零CapEx增量的场景。

## Corrected Claim

纯软件转码工作点：基于x264/FFmpeg CPU转码，单线程1080p 15s视频耗时约为视频时长的2-3倍（30-45s），P99 T_processing_vid ≈ 30-45s，适用于低QPS、无硬件加速卡、追求零CapEx增量的场景。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

x264 1080p encode time per second CPU benchmark
