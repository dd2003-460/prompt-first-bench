# N11: 多卡方案（如 2× 消费卡）的总显存容量必须满足：单卡显存 ≥ (54GB + 4.09GB + 2GB) / 2 = 30GB，且需额外预留 2-5GB 用于

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

多卡方案（如 2× 消费卡）的总显存容量必须满足：单卡显存 ≥ (54GB + 4.09GB + 2GB) / 2 = 30GB，且需额外预留 2-5GB 用于 NCCL 通信缓冲，因此单卡显存下限提升至 32-35GB

## Corrected Claim

多卡方案（如 2× 消费卡）的总显存容量必须满足：单卡显存 ≥ (54GB + 4.09GB + 2GB) / 2 = 30GB，且需额外预留 2-5GB 用于 NCCL 通信缓冲，因此单卡显存下限提升至 32-35GB

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (54+4.09+2)/2 ≈ 30.045GB 正确，加上 2-5GB 缓冲后下限为 32-35GB，符合多卡显存分配的工程逻辑。

## Search Query

NCCL buffer memory overhead multi-gpu inference
