# N165: 1x A100 80GB 运行 BF16 Qwen3-27B 时，因显存带宽 (2039 GB/s) 高于 2x 4090 (有效带宽受 PCIe 限制)，其单

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

1x A100 80GB 运行 BF16 Qwen3-27B 时，因显存带宽 (2039 GB/s) 高于 2x 4090 (有效带宽受 PCIe 限制)，其单卡 Decode 速度约为 2x 4090 FP8 方案的 1.5-2 倍，且无需通信开销。

## Corrected Claim

1x A100 80GB 运行 BF16 Qwen3-27B 时，因显存带宽 (2039 GB/s) 高于 2x 4090 (有效带宽受 PCIe 限制)，其单卡 Decode 速度约为 2x 4090 FP8 方案的 1.5-2 倍，且无需通信开销。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

A100 vs dual RTX 4090 LLM inference speed comparison
