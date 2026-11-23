# N7: P99延迟目标值 T 的推导公式：T = T_base + T_jitter_buffer + T_sla_margin，其中 T_base 为业务可接受的基础

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

P99延迟目标值 T 的推导公式：T = T_base + T_jitter_buffer + T_sla_margin，其中 T_base 为业务可接受的基础延迟（如图片加载 200ms，短视频首帧 500ms），T_jitter_buffer 为网络抖动缓冲（通常取 P99-P50 差值的 1.5 倍），T_sla_margin 为 SLA 安全边际（通常 10%-20%）。

## Corrected Claim

P99延迟目标值 T 的推导公式：T = T_base + T_jitter_buffer + T_sla_margin，其中 T_base 为业务可接受的基础延迟（如图片加载 200ms，短视频首帧 500ms），T_jitter_buffer 为网络抖动缓冲（通常取 P99-P50 差值的 1.5 倍），T_sla_margin 为 SLA 安全边际（通常 10%-20%）。

## Evidence

先验知识/题面给定，逻辑校验通过
