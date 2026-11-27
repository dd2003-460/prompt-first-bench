# N131: RTX 4090 24GB 在运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，剩余显存约 8.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

RTX 4090 24GB 在运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，剩余显存约 8.5GB 用于激活值和碎片，足以支持单卡推理，无需双卡；其 1008 GB/s 带宽决定了 decode 速度上限约为 1008 / (13.5+2.0) ≈ 65 tokens/s (理论值，实际受计算瓶颈限制)

## Corrected Claim

RTX 4090 24GB 在运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，剩余显存约 8.5GB 用于激活值和碎片，足以支持单卡推理，无需双卡；其 1008 GB/s 带宽决定了 decode 速度上限约为 1008 / (13.5+2.0) ≈ 65 tokens/s (理论值，实际受计算瓶颈限制)

## Evidence

先验知识/题面给定，逻辑校验通过：显存占用计算（24-13.5-2.0=8.5GB）及带宽理论上限推导（1008/15.5≈65 tokens/s）均符合物理与算术逻辑，且RTX 4090规格参数准确。
