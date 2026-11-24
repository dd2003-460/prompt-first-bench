# N616: 视频起播场景 P99 延迟目标 T=200ms 的量化依据：基于视频首帧解码缓冲需求（通常需预加载 500KB-1MB 数据），若 P99 > 200ms，起播

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N201

## Claim

视频起播场景 P99 延迟目标 T=200ms 的量化依据：基于视频首帧解码缓冲需求（通常需预加载 500KB-1MB 数据），若 P99 > 200ms，起播黑屏时间增加 > 100ms，导致用户跳出率上升约 2-3%（A/B 测试统计显著性阈值）。

## Corrected Claim

视频起播场景 P99 延迟目标 T=200ms 的量化依据：基于视频首帧解码缓冲需求，若 P99 > 200ms，起播黑屏时间增加，通常会导致用户跳出率显著上升（具体幅度视业务场景而定，常见 A/B 测试显示为 2-3%）。

## Evidence

[质询]该陈述包含具体的经验性数值（500KB-1MB缓冲量、2-3%跳出率增幅），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定网络环境、视频编码格式及用户群体的经验统计值，缺乏通用性。 | 先验知识/题面给定，逻辑校验通过；但具体数值（如2-3%跳出率）属于经验事实，无外部来源支持，故降级。

## Search Query

video start playback latency threshold user drop-off rate 200ms
