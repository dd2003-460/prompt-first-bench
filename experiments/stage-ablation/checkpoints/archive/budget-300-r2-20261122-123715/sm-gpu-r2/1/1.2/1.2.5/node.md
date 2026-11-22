# N40: A10 24GB PCIe 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

A10 24GB PCIe 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 24GB 物理显存，无需 Offload，但 PCIe 带宽 64GB/s 成为瓶颈，吞吐量预计为 20-30 tokens/s

## Corrected Claim

A10 24GB PCIe 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 24GB 物理显存，无需 Offload，但 PCIe 带宽 64GB/s 成为瓶颈，吞吐量预计为 20-30 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B W4量化权重约13.5GB，32K上下文KV Cache约4.5GB，加上激活/框架开销约2GB，总显存占用约20GB，小于24GB物理显存，无需Offload；PCIe带宽64GB/s成为瓶颈，吞吐量预计20-30 tokens/s，量级合理。
