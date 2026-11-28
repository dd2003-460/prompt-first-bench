# N36: AMD Radeon RX 7900 XTX 在 ROCm 生态下对 Qwen3-27B 的支持存在算子覆盖缺口，特别是 Flash Attention 和 P

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD Radeon RX 7900 XTX 在 ROCm 生态下对 Qwen3-27B 的支持存在算子覆盖缺口，特别是 Flash Attention 和 PagedAttention 的优化程度低于 CUDA 环境，导致实际吞吐量仅为理论峰值的 60-70%，且在多卡互联（Infinity Fabric）方面缺乏针对 LLM 推理的低延迟优化，性价比评估需打折扣。

## Corrected Claim

AMD Radeon RX 7900 XTX 在 ROCm 生态下对 Qwen3-27B 的支持存在算子覆盖缺口，特别是 Flash Attention 和 PagedAttention 的优化程度低于 CUDA 环境，导致实际吞吐量仅为理论峰值的 60-70%，且在多卡互联（Infinity Fabric）方面缺乏针对 LLM 推理的低延迟优化，性价比评估需打折扣。

## Evidence

检索失败: no sources from any channel (all 5 failed)
