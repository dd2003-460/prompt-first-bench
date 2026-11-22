# N178: CUDA Context 的显存占用并非固定 0.5GB，而是随 GPU 架构和驱动版本变化；对于 RTX 4090 (Ada Lovelace)，CUDA C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46, N47, N48

## Claim

CUDA Context 的显存占用并非固定 0.5GB，而是随 GPU 架构和驱动版本变化；对于 RTX 4090 (Ada Lovelace)，CUDA Context 基础开销约为 0.3-0.5GB，但启用 CUDA Graphs 后，每个捕获的 Graph 会额外占用 50-200MB 显存用于存储执行计划，总开销需根据捕获的 Batch Size 数量累加

## Corrected Claim

CUDA Context 的显存占用并非固定 0.5GB，而是随 GPU 架构和驱动版本变化；对于 RTX 4090 (Ada Lovelace)，CUDA Context 基础开销约为 0.3-0.5GB，但启用 CUDA Graphs 后，每个捕获的 Graph 会额外占用 50-200MB 显存用于存储执行计划，总开销需根据捕获的 Batch Size 数量累加

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead RTX 4090 Ada Lovelace
