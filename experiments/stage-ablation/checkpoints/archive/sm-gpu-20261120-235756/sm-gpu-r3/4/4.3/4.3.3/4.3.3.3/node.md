# N254: GPU_Total_VRAM 的有效可用率：由于 CUDA 驱动、操作系统和框架预留，GPU 总显存中通常有 1-2 GB 不可用；例如，RTX 5090 的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

GPU_Total_VRAM 的有效可用率：由于 CUDA 驱动、操作系统和框架预留，GPU 总显存中通常有 1-2 GB 不可用；例如，RTX 5090 的 32 GB 显存中，实际可用显存约为 30-31 GB；该值需在 Batch_Size 公式中作为 GPU_Total_VRAM 的实际输入，以避免 OOM 风险。

## Corrected Claim

GPU_Total_VRAM 的有效可用率：由于 CUDA 驱动、操作系统和框架预留，GPU 总显存中通常有 1-2 GB 不可用；例如，RTX 5090 的 32 GB 显存中，实际可用显存约为 30-31 GB；该值需在 Batch_Size 公式中作为 GPU_Total_VRAM 的实际输入，以避免 OOM 风险。

## Evidence

先验知识/题面给定，逻辑校验通过
