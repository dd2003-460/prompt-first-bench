# N126: AMD MI300X 的 BF16 原生推理吞吐量基准：在 32K 上下文下，单用户 tokens/s 约为 100-150 tokens/s [待核验]。MI

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

AMD MI300X 的 BF16 原生推理吞吐量基准：在 32K 上下文下，单用户 tokens/s 约为 100-150 tokens/s [待核验]。MI300X 的 5.3 TB/s 带宽理论上优于 H100，但受限于 ROCm 优化程度，实际性能需单独检索确认。

## Corrected Claim

AMD MI300X 在 32K 上下文下，启用 FP8 量化后的单用户推理吞吐量约为 110-155 tokens/s；BF16 原生吞吐量通常低于此数值，具体需单独基准测试确认。

## Evidence

[质询]来源[3]明确指出的 110-155 tokens/s 性能提升是基于启用 FP8 量化后的结果，而非 BF16 原生精度；将 FP8 的性能数据直接归因为 BF16 原生吞吐量存在精度口径混淆，且未提供 BF16 单独基准测试的直接证据。 | 来源[3]提供了 MI300X 在 32K 上下文下 110-155 tokens/s 的数据，但明确标注为 FP8 量化场景，与 claim 中的 BF16 原生精度不完全匹配，属于间接支持且存在精度差异，故降级。

## Search Query

AMD MI300X Qwen3 27B BF16 inference throughput tokens per second 32k context

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2600_96323235/article/details/162293039&rut=eb5b1d3cb45e63fbe55c31f5dc85e410d8ab823dcf0f99e51b62775e4ebfc1d5', 'type': 'ddg', 'title': 'AMD Instinct MI300 系列显卡的 BF16 加速特性应用 - CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162293039&rut=3e8bee5abb5ce61e53eae4cfc9adab470d1dd05696d494e93654ff9c38dacd4e', 'type': 'ddg', 'title': 'AMD Instinct MI300 系列显卡的 BF16 加速特性应用_2600_96323235-AMD开发者中国社区'}
- {'url': 'https://blog.csdn.net/2600_96323165/article/details/162043244&rut=2b3613f5ea18ab54c8c82e4e4a859f9718abd407bbf66f083ee33ed23506c1b4', 'type': 'ddg', 'title': '从 110 到 155 tokens/s，我的 MI300X 推理加速实录 - CSDN博客'}
