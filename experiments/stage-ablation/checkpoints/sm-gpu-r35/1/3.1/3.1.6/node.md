# N37: 量化精度损失评估框架：不同精度（BF16/FP8/INT8/W4）对 Qwen3-27B 的 perplexity 或 benchmark 分数影响，需引用官方

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

量化精度损失评估框架：不同精度（BF16/FP8/INT8/W4）对 Qwen3-27B 的 perplexity 或 benchmark 分数影响，需引用官方量化版本或第三方评测数据

## Corrected Claim

不同精度（BF16/FP8/INT8/W4）对 Qwen3-27B 的 perplexity 或 benchmark 分数影响需引用官方量化版本或针对该特定模型的第三方评测数据；现有参考来源主要覆盖 Qwen3-30B-A3B 或 Qwen3.6-27B，仅能作为量级参考（如 FP8 通常带来 2-3% 精度损失），不能直接作为 Qwen3-27B 的确切事实依据。

## Evidence

[质询]模型版本不匹配：参考来源主要讨论 Qwen3-30B-A3B 或 Qwen3.6-27B，而非 Qwen3-27B；且来源多为第三方博客（CSDN），缺乏官方量化版本或权威第三方评测的直接数据支持，无法确认 Qwen3-27B 在 W4/INT8 下的具体 perplexity 或 benchmark 分数。 | 来源 [1][2] 提供了 Qwen3-30B-A3B 在 FP8 下 2-3% 精度损失的间接参考，来源 [3] 涉及 27B 级别模型的 4-bit 量化对比，但均非 Qwen3-27B 的官方或权威直接数据，属于间接支持且存在模型版本差异。

## Search Query

Qwen3-27B FP8 INT8 W4 quantization quality loss perplexity benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00279/article/details/151738226&rut=b5f24390b1dfaf6f3d974d7d88c2a233958be8c6aa6e3492bdec77d911e8e4f9', 'type': 'ddg', 'title': 'Qwen3-30B-A3B量化精度对比：FP16/BF16/FP8推理性能损耗分析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/151738226&rut=ee7b775257f7201d06a223c98c748a878ef248eaa2302a8881ccb4094bb8b1a4', 'type': 'ddg', 'title': 'Qwen3-30B-A3B量化精度对比：FP16/BF16/FP8推理性能损耗分析_伍希望-智能体开发者社区'}
- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168656480&rut=91d9f699336cd7030904459a6dc0f3bc1ea62e5ea273b79488395d2d0627738f', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 vs NVIDIA NVFP4 vs FP8 vs BF16：精度基准全对比，4-b'}
- {'url': 'https://summerplaceal.com/', 'type': 'bing', 'title': 'Summer Place Apartment Homes | Summer Place'}
