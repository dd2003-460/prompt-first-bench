# N125: RTX 4090 推理 Qwen3-27B (W4) 的实测校准系数 (Efficiency_Factor) 量化：在 vLLM 0.6+ 及 FlashAtt

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N38

## Claim

RTX 4090 推理 Qwen3-27B (W4) 的实测校准系数 (Efficiency_Factor) 量化：在 vLLM 0.6+ 及 FlashAttention-2 环境下，Decode 阶段实际吞吐通常为理论带宽上限 (1008 GB/s / 13.5 GB ≈ 74.6 tokens/s) 的 55-65%；主要损耗来源为 PCIe 内存控制器开销 (~10%)、Attention 计算瓶颈 (~20%) 及调度开销 (~10-15%)；取中值 60% 估算，单序列实际吞吐 ≈ 44-47 tokens/s。

## Corrected Claim

RTX 4090 推理 Qwen3-27B (W4) 的理论带宽上限约为 74.6 tokens/s。在典型 vLLM 及 FlashAttention-2 环境下，受内存控制器、Attention 计算及调度开销影响，实际 Decode 吞吐通常显著低于理论值，具体数值需根据实际部署环境实测确定，一般估计在理论值的 50-70% 区间内。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（RTX 4090 带宽利用率、具体损耗百分比、最终吞吐数值），属于经验事实。在缺乏外部来源支持的情况下，无法验证这些具体数值（如 55-65% 的效率因子、44-47 tokens/s 的吞吐）的准确性，且不同软件栈版本（vLLM 0.6+）和具体实现细节可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持。理论带宽计算 (1008/13.5≈74.6) 正确，应用 60% 效率因子得到 ~44.7 tokens/s 在数学上自洽，但具体效率因子和损耗分布为经验估计，无来源佐证。

## Search Query

RTX 4090 vLLM Qwen3 27B W4 decode tokens per second benchmark efficiency factor
