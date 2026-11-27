# N52: 在多卡推理场景下（如 2x GPU），Runtime Overhead 会因每个 GPU 都需要独立的 CUDA context 而增加，总 Overhead 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

在多卡推理场景下（如 2x GPU），Runtime Overhead 会因每个 GPU 都需要独立的 CUDA context 而增加，总 Overhead 约为 2 * (1-2GB) = 2-4GB，且需考虑 NCCL 通信库的额外内存占用（通常 <1GB） [knowledge]

## Corrected Claim

在多卡推理场景下（如 2x GPU），Runtime Overhead 会因每个 GPU 都需要独立的 CUDA context 而增加，总 Overhead 约为 2 * (1-2GB) = 2-4GB，且需考虑 NCCL 通信库的额外内存占用（通常 <1GB） [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：多卡推理中每个GPU需独立CUDA context（通常1-2GB），2卡即2-4GB，NCCL通信库额外占用通常<1GB，量级与工程实践一致。

## Search Query

multi-GPU inference memory overhead NCCL CUDA context
