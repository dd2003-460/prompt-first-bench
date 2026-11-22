# N130: AMD RX 7900 XTX ($900) 运行 Qwen3-27B 的软件栈兼容性风险量化：ROCm 对 PyTorch 2.1+ 支持完整，但对 vLLM

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

AMD RX 7900 XTX ($900) 运行 Qwen3-27B 的软件栈兼容性风险量化：ROCm 对 PyTorch 2.1+ 支持完整，但对 vLLM 的 FlashAttention 支持存在性能回退（比 CUDA 慢 20-40%）[待核验：需查 ROCm 7.0 发布说明]，且 Qwen3 官方未提供 ROCm 优化 kernel，实际吞吐可能仅为理论值的 30-50%

## Corrected Claim

AMD RX 7900 XTX 运行 Qwen3-27B 存在软件栈兼容性风险：ROCm 对 PyTorch 支持较好，但 vLLM 的 FlashAttention 在 ROCm 上可能存在性能回退，且 Qwen3 官方未提供 ROCm 优化 kernel，实际吞吐可能显著低于理论值。

## Evidence

[质询]陈述中关于 vLLM FlashAttention 在 ROCm 上具体性能回退 20-40% 以及 Qwen3 实际吞吐仅为理论值 30-50% 的具体数值缺乏权威来源支持，且 ROCm 版本（7.0）与当前主流稳定版（6.x）存在时效性风险，具体性能指标高度依赖具体硬件配置和软件版本，属于难以从第一性原理推导的经验事实。 | 来源 [1] 仅证实了 ROCm 6.2 在 RX 7900 XTX 上支持 PyTorch 的基础构建，未提供 vLLM FlashAttention 性能回退或 Qwen3 吞吐率的具体量化数据，属于间接支持基础兼容性但无法支持具体性能数值。

## Search Query

ROCm vLLM FlashAttention performance regression RTX 7900 XTX Qwen3 throughput

## Retrieval Sources

- {'url': 'https://github.com/sbeierle/rocm-6.2-build-qwen&rut=4f7dfa16b71bc658454f38b5782242fa252668d92bebe9cdebfee68e05c82281', 'type': 'ddg', 'title': 'GitHub - sbeierle/rocm-6.2-build-qwen: rocm 6.2 Build for Qwen7B ...'}
