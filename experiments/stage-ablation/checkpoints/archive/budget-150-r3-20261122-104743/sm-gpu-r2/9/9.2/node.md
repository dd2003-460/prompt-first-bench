# N187: H100 SXM5 在 Qwen3-27B 上的 Decode 速度基准：BF16 模式下理论带宽瓶颈速度 ≈ 2039 GB/s (HBM3) / 54 GB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

H100 SXM5 在 Qwen3-27B 上的 Decode 速度基准：BF16 模式下理论带宽瓶颈速度 ≈ 2039 GB/s (HBM3) / 54 GB ≈ 37.7 tokens/s，但实测 50-80 tokens/s 表明存在计算优化或 FP8 加速；[待核验] 需区分 FP8 与 BF16 的实测差异，FP8 下速度可能接近 60-80 tokens/s，而 BF16 下更接近 40-50 tokens/s

## Corrected Claim

H100 SXM5 在 27B 级别模型（如 Qwen3.5-27B）上的 Decode 速度：FP8 模式下实测可达 50-80 tokens/s；BF16 模式下受带宽限制，理论上限约 60 tokens/s，实测通常低于此值。

## Evidence

[质询]模型版本混淆：参考来源均为 Qwen3.5-27B 或 Qwen3.6-27B，而非 Qwen3-27B；且来源主要提供 FP8 数据，缺乏 BF16 实测数据以直接验证 40-50 tokens/s 的断言。 | 逻辑推导成立（H100 SXM5 带宽 3.35TB/s，27B 模型权重约 54GB，理论上限 ~62 tokens/s，实测 50-80 需考虑 FP8 减半权重或计算优化，量级合理）；来源 [1][2] 提供了 Qwen3.5-27B FP8 在 H100 上的基准，间接支持 FP8 下的高吞吐，但无法直接证实 Qwen3-27B BF16 的具体数值，属经验事实且来源版本不匹配。

## Search Query

H100 Qwen3-27B decode speed benchmark FP8 vs BF16

## Retrieval Sources

- {'url': 'https://www.millstoneai.com/inference-benchmark/qwen3-5-27b-fp8-1x-h100-sxm&rut=e6eb652ccf1ce6f6d037b73c2c09d6666e58d96bea706b6e6c1921c213938669', 'type': 'ddg', 'title': 'Qwen3.5-27B on 1x H100 SXM Benchmark — FP8 | Millstone AI'}
- {'url': 'https://cdn.millstoneai.cloud/benchmarks/qwen3-5-27b-fp8-1x-h100-sxm/qwen3-5-27b-fp8-1x-h100-sxm.pdf&rut=6f053805ce58a80c87489b6729fdfa622c258b48574c3ff5a6d31b4717ba3cd3', 'type': 'ddg', 'title': 'PDF Inference Benchmark - qwen3-5-27b-fp8 on 1x H100 SXM'}
- {'url': 'https://markaicode.com/benchmarks/hugging-face-qwen-3-h100-latency-benchmark/&rut=d857d7481688dac6483d5951e8752b3c0c604eae68acd593d28731aefcaf6bf8', 'type': 'ddg', 'title': 'Qwen3.6-27B H100 Benchmark: Latency, Throughput & VRAM'}
