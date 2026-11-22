# N636: NVIDIA NVLink 带宽为 64 GB/s，实际通信延迟 T_comm = D_step / 64 GB/s ≈ 10^-7 s，可忽略不计。

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N196

## Claim

NVIDIA NVLink 带宽为 64 GB/s，实际通信延迟 T_comm = D_step / 64 GB/s ≈ 10^-7 s，可忽略不计。

## Corrected Claim

NVIDIA NVLink 带宽通常远高于 64 GB/s（如 NVLink 4.0 为 400 GB/s），实际通信延迟 T_comm = D_step / Bandwidth 通常远小于 10^-7 s，可忽略不计。

## Evidence

[质询]数值量级错误：NVIDIA NVLink 的带宽通常远高于 64 GB/s（例如 NVLink 3.0 为 200 GB/s，NVLink 4.0 为 400 GB/s，NVLink 5.0 为 900 GB/s）。64 GB/s 更接近 PCIe 4.0 x16 或早期 NVLink 1.0 的带宽，将其作为通用 NVLink 带宽陈述不准确，导致延迟计算基于错误的带宽假设。 | 先验知识/题面给定，逻辑校验通过（公式 T=D/B 自洽），但经验事实（NVLink 带宽具体数值）与当前主流硬件规格不符，且无来源支持，故降级。
