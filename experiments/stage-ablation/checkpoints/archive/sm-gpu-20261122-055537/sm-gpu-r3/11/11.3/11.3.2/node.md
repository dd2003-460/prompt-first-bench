# N381: 若单卡 4090 仅 offload 部分层（例如保留前 27 层在 GPU，后 27 层在 CPU），由于 Transformer 层间依赖，每生成一个 to

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

若单卡 4090 仅 offload 部分层（例如保留前 27 层在 GPU，后 27 层在 CPU），由于 Transformer 层间依赖，每生成一个 token 必须串行执行 GPU 层计算和 CPU 层计算。CPU 层计算时间由 RAM 带宽决定（~0.7s/token），GPU 层计算时间由显存带宽决定（~0.05s/token），总延迟为两者之和，导致有效吞吐量进一步降低至 ~1.3 tokens/s，且无法利用 GPU 的高算力并行优势。

## Corrected Claim

若单卡 4090 仅 offload 部分层（例如保留前 27 层在 GPU，后 27 层在 CPU），由于 Transformer 层间依赖，每生成一个 token 必须串行执行 GPU 层计算和 CPU 层计算。CPU 层计算时间由 RAM 带宽决定（~0.7s/token），GPU 层计算时间由显存带宽决定（~0.05s/token），总延迟为两者之和，导致有效吞吐量进一步降低至 ~1.3 tokens/s，且无法利用 GPU 的高算力并行优势。

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer 层间串行依赖导致 GPU/CPU 计算无法重叠，总延迟为两者之和（0.7s + 0.05s = 0.75s），吞吐量 1/0.75 ≈ 1.33 tokens/s，与陈述一致；CPU 层受 RAM 带宽限制、GPU 层受显存带宽限制的物理直觉合理。
