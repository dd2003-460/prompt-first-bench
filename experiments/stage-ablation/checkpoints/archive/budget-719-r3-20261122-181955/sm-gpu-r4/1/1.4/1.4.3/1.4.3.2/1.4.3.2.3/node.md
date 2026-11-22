# N560: Intel Arc A770 在 BF16 精度下运行 Qwen3-27B 时，权重占用 54 GB，远超 16GB 显存，必须依赖 CPU 内存交换，此时 D

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N195

## Claim

Intel Arc A770 在 BF16 精度下运行 Qwen3-27B 时，权重占用 54 GB，远超 16GB 显存，必须依赖 CPU 内存交换，此时 Decode 吞吐量瓶颈转为 PCIe 4.0 x16 带宽（~32 GB/s 单向），理论上限约为 32 GB/s / (54GB 权重 + 8GB KV) ≈ 0.5 tokens/s，实测通常更低（0.2-0.3 tokens/s）。

## Corrected Claim

Intel Arc A770 在 BF16 精度下运行 Qwen3-27B 时，权重占用约 54 GB，远超 16GB 显存，需依赖 CPU 内存交换。Decode 吞吐量受 PCIe 4.0 x16 带宽（~32 GB/s）及内存调度策略限制，理论上限估算约为 0.5 tokens/s，实测通常更低（0.2-0.3 tokens/s）。

## Evidence

[质询]该陈述将 Decode 阶段的吞吐量瓶颈简单归结为 PCIe 带宽除以总权重大小，忽略了 LLM 推理中 KV Cache 的局部性、权重分块加载策略以及 CPU 内存带宽对预取的影响，导致理论上限计算过于简化且可能高估或低估实际瓶颈；此外，Qwen3-27B 在 BF16 下的权重占用 54GB 是经验事实，虽逻辑自洽但缺乏来源直接支持。 | 经验事实，逻辑自洽但缺来源支持；source=knowledge 节点，但反方质询指出理论模型简化可能影响准确性，故降级为定性表述。

## Search Query

llama.cpp Vulkan Intel Arc A770 CPU offload throughput tokens/s
