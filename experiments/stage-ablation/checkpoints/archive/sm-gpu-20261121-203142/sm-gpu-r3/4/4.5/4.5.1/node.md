# N91: 在32K上下文下，生成阶段（Decode）为显存带宽受限（Memory-bound），单Token生成时间的理论下界公式为 T_min ≈ W_bytes / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

在32K上下文下，生成阶段（Decode）为显存带宽受限（Memory-bound），单Token生成时间的理论下界公式为 T_min ≈ W_bytes / Bandwidth，其中 W_bytes 为需读取的模型权重总字节数（如BF16下54GB，FP8下27GB）。

## Corrected Claim

在32K上下文下，生成阶段（Decode）为显存带宽受限（Memory-bound），单Token生成时间的理论下界公式为 T_min ≈ W_bytes / Bandwidth，其中 W_bytes 为需读取的模型权重总字节数（如BF16下54GB，FP8下27GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段为Memory-bound，理论下界由权重读取时间决定，公式 T_min ≈ W_bytes / Bandwidth 符合物理直觉与工程常识。
