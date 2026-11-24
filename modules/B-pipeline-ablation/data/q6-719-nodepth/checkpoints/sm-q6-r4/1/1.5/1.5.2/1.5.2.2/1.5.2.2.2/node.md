# N552: 硬件加速转码工作点：基于NVIDIA T4 GPU (NVENC) 或 Intel QAT，单卡并发10路1080p转码，单路15s视频耗时约为视频时长的1/5

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187

## Claim

硬件加速转码工作点：基于NVIDIA T4 GPU (NVENC) 或 Intel QAT，单卡并发10路1080p转码，单路15s视频耗时约为视频时长的1/5-1/10（1.5-3s），P99 T_processing_vid ≈ 1.5-3s，适用于高并发、追求低延迟且接受¥30k/月/卡CapEx的场景。

## Corrected Claim

硬件加速转码工作点：基于NVIDIA T4 GPU (NVENC) 或 Intel QAT，单卡并发10路1080p转码，单路15s视频耗时约为视频时长的1/5-1/10（1.5-3s），P99 T_processing_vid ≈ 1.5-3s，适用于高并发、追求低延迟且接受¥30k/月/卡CapEx的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA T4 NVENC 支持多路 1080p 硬件编码，15s 视频转码耗时 1.5-3s 符合硬件加速低延迟特性，成本量级合理。

## Search Query

NVIDIA T4 NVENC 1080p concurrent streams encode latency
