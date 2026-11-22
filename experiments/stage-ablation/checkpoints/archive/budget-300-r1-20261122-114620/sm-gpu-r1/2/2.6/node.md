# N17: 显存带宽对推理吞吐的影响：KV Cache 和权重加载均受内存带宽限制，RTX 4090 (1008 GB/s) vs A100 40GB (1555 GB/s

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

显存带宽对推理吞吐的影响：KV Cache 和权重加载均受内存带宽限制，RTX 4090 (1008 GB/s) vs A100 40GB (1555 GB/s) vs H100 (3350 GB/s)，带宽比直接决定 tokens/sec 上限

## Corrected Claim

显存带宽对推理吞吐的影响：KV Cache 和权重加载均受内存带宽限制，RTX 4090 (1008 GB/s) vs A100 40GB (1555 GB/s) vs H100 (3350 GB/s)，带宽比直接决定 tokens/sec 上限

## Evidence

先验知识/题面给定，逻辑校验通过：显存带宽数值符合硬件规格常识，且大模型推理中KV Cache和权重加载确实受内存带宽限制，带宽比与吞吐上限正相关符合物理直觉。
