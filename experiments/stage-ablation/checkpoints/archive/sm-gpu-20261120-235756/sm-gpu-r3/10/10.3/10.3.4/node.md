# N352: Apple M3 Ultra 运行 Qwen3-27B BF16 时，内存带宽瓶颈导致理论最大吞吐量为 29.4 tokens/s（计算式: 800 GB/s 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N132, N133, N134

## Claim

Apple M3 Ultra 运行 Qwen3-27B BF16 时，内存带宽瓶颈导致理论最大吞吐量为 29.4 tokens/s（计算式: 800 GB/s / (27.18B * 2 bytes)），实际吞吐量受内存控制器效率和缓存命中率影响，预计为 20-25 tokens/s，而非 10-20 tokens/s 的低估范围。

## Corrected Claim

Apple M3 Ultra 运行 Qwen3-27B BF16 时，内存带宽瓶颈导致理论最大吞吐量为 29.4 tokens/s（计算式: 800 GB/s / (27.18B * 2 bytes)），实际吞吐量受内存控制器效率和缓存命中率影响，预计为 20-25 tokens/s，而非 10-20 tokens/s 的低估范围。
