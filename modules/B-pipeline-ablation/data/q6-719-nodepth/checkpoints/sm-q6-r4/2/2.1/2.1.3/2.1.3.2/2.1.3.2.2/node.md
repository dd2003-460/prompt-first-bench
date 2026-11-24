# N505: 工作点 B（边缘实时转码/CPU 加速）：5% 请求触发边缘 CPU 实时转码（x264 fast preset, 1.5MB 视频）。L_transform_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N162

## Claim

工作点 B（边缘实时转码/CPU 加速）：5% 请求触发边缘 CPU 实时转码（x264 fast preset, 1.5MB 视频）。L_transform_weighted = 0.95 * 1.0ms + 0.05 * 80ms = 5.0ms。此工作点牺牲部分边缘 CPU 资源换取源站带宽节省，适用于视频格式多样且源站带宽成本远高于 CPU 成本的场景。

## Corrected Claim

工作点 B（边缘实时转码/CPU 加速）：5% 请求触发边缘 CPU 实时转码（x264 fast preset, 1.5MB 视频）。L_transform_weighted = 0.95 * 1.0ms + 0.05 * 80ms = 5.0ms。此工作点牺牲部分边缘 CPU 资源换取源站带宽节省，适用于视频格式多样且源站带宽成本远高于 CPU 成本的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.95*1.0 + 0.05*80 = 0.95 + 4.0 = 4.95 ≈ 5.0ms，数值量级合理，场景描述符合边缘计算与源站带宽成本权衡的工程直觉。
