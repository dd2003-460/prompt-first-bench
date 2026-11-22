# N871: RTX 4090 的可用显存并非标称的 24GB，由于 CUDA Context、驱动开销及 PyTorch 框架碎片，实际可用显存约为 23.2GB-23.5

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N272

## Claim

RTX 4090 的可用显存并非标称的 24GB，由于 CUDA Context、驱动开销及 PyTorch 框架碎片，实际可用显存约为 23.2GB-23.5GB。在计算剩余显存时，应从 23.2GB 开始扣除，而非 24GB，这将导致最大 batch_size 进一步受限或不变（取决于其他开销）。

## Corrected Claim

RTX 4090 的可用显存并非标称的 24GB，由于 CUDA Context、驱动开销及 PyTorch 框架碎片，实际可用显存约为 23.2GB-23.5GB。在计算剩余显存时，应从 23.2GB 开始扣除，而非 24GB，这将导致最大 batch_size 进一步受限或不变（取决于其他开销）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 available VRAM vs total VRAM PyTorch overhead
