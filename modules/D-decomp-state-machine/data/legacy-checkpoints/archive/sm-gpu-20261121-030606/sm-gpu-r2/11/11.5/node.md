# N165: 单卡RTX 5090 (FP8)在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1792 GB/s / (13.5GB权重 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

单卡RTX 5090 (FP8)在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1792 GB/s / (13.5GB权重 + 5.2GB KV Cache + 2.5GB激活) ≈ 89.5 tokens/s，基于RTX 5090 GDDR7 1.79TB/s带宽

## Corrected Claim

单卡RTX 5090 (FP8)在32K上下文、batch_size=1下的理论带宽受限推理吞吐量上限约为89.5 tokens/s，实际吞吐量受内存访问效率和计算延迟影响，通常低于此理论值。

## Evidence

[质询]该陈述将推理吞吐量简化为纯带宽受限模型（Bandwidth-Bound），忽略了计算延迟（Compute Latency）和内存访问效率（Memory Efficiency）。在32K长上下文下，KV Cache的读取量巨大，但实际吞吐量通常远低于理论带宽上限（通常受限于有效带宽利用率，约为理论值的50%-70%），且未考虑Attention机制中的计算开销。此外，1792 GB/s是理论峰值带宽，实际持续带宽通常低于此值。 | 来源[1]确认了RTX 5090的算力参数，但未提供GDDR7具体带宽数值（1.79TB/s为公开规格，逻辑上合理）；该吞吐量计算属于经验事实的工程估算，逻辑自洽但缺乏直接来源支持实际吞吐量数值，且简化模型存在偏差，故降级。

## Search Query

RTX 5090 memory bandwidth GB/s

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2062928081980072755&rut=49bc8e8c89c7838d3642b90c83fe2489e9185702b221db690d43f108a0f13ce5', 'type': 'ddg', 'title': 'Rtx 5090算力到底多少？Fp16/Fp8/Int8算力实测与解读 - 知乎'}
