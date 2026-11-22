# N51: CUDA context 及临时缓冲的 Runtime Overhead 在单卡推理场景下通常为 1-2GB，具体数值取决于 CUDA 版本、驱动版本及是否启用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

CUDA context 及临时缓冲的 Runtime Overhead 在单卡推理场景下通常为 1-2GB，具体数值取决于 CUDA 版本、驱动版本及是否启用特定优化（如 CUDA Graphs） [knowledge]

## Corrected Claim

CUDA context 及临时缓冲的 Runtime Overhead 在单卡推理场景下通常为 1-2GB，具体数值取决于 CUDA 版本、驱动版本及是否启用特定优化（如 CUDA Graphs） [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead GPU inference
