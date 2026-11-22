# N413: Apple M4 Ultra 在 BF16 精度下运行 Qwen3-27B 的实际吞吐受限于 MLX 框架的内存带宽利用率，若效率因子为 0.6，则实际速度为 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N156

## Claim

Apple M4 Ultra 在 BF16 精度下运行 Qwen3-27B 的实际吞吐受限于 MLX 框架的内存带宽利用率，若效率因子为 0.6，则实际速度为 819 GB/s / 54 GB * 0.6 ≈ 9.1 Tokens/s，低于 RTX 5090 W4 的 100+ Tokens/s，性能差距超过 10 倍，仅适用于低负载或离线批处理场景。

## Corrected Claim

Apple M4 Ultra 在 BF16 精度下运行 Qwen3-27B 的实际吞吐受限于 MLX 框架的内存带宽利用率，若效率因子为 0.6，则理论估算速度约为 9.1 Tokens/s，显著低于 RTX 5090 W4 的 100+ Tokens/s，性能差距超过 10 倍，仅适用于低负载或离线批处理场景。

## Evidence

[质询]效率因子0.6为假设值而非实测数据，且未考虑MLX框架在M4 Ultra上的实际优化程度及Qwen3-27B的具体量化格式（如是否使用MLX原生量化），导致计算结果可能偏离真实场景。 | 先验知识/题面给定，逻辑校验通过，但效率因子为假设值，缺乏实测数据支持，故降级为定性表述。

## Search Query

Apple M4 Ultra MLX LLM inference throughput Qwen3 27B BF16
