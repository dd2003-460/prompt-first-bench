# N9: 总显存需求 (Total VRAM) = Weight Memory (N7) + KV Memory (N8) + Runtime Overhead (约 1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

总显存需求 (Total VRAM) = Weight Memory (N7) + KV Memory (N8) + Runtime Overhead (约 1-2GB 用于 CUDA context 及临时缓冲)，该总和必须小于候选硬件可用显存

## Corrected Claim

总显存需求 (Total VRAM) = Weight Memory (N7) + KV Memory (N8) + Runtime Overhead (约 1-2GB 用于 CUDA context 及临时缓冲)，该总和必须小于候选硬件可用显存

## Evidence

先验知识/题面给定，逻辑校验通过
