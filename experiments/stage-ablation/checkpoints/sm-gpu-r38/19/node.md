# N316: 单卡 H100 80GB 在 BF16 精度下的显存占用为 61.85GB (权重 55.6GB + KV Cache 4.0GB + 激活 2.25GB)，剩

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

单卡 H100 80GB 在 BF16 精度下的显存占用为 61.85GB (权重 55.6GB + KV Cache 4.0GB + 激活 2.25GB)，剩余 18.15GB 显存支持的最大并发 Batch Size 为 3 (基于 KV Cache 每请求 4GB 估算)，而双卡 RTX 4090 在 FP8 下剩余显存支持的最大 Batch Size 为 2，单卡方案在并发容量上具有绝对优势。

## Corrected Claim

单卡 H100 80GB 在 BF16 精度下，若模型权重、KV Cache 及激活值总占用约为 61.85GB，则剩余显存约 18.15GB；在 KV Cache 每请求占用约 4GB 的假设下，支持的最大并发 Batch Size 约为 3。相比之下，双卡 RTX 4090 在 FP8 下因显存总量及精度差异，其支持的最大 Batch Size 可能较低（如 2），具体数值需依据实际模型规模与配置确定。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如权重55.6GB、KV Cache 4.0GB、激活2.25GB、剩余显存18.15GB等），这些数值高度依赖于具体的模型参数量、序列长度、推理框架配置及量化细节，并非通用硬件规格或第一性原理可推导的固定事实。参考来源中未提供针对特定模型在H100/4090上的具体显存占用数据，无法验证这些具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持。来源[1]仅涉及RTX 4060规格，与4090及具体显存计算无关；来源[2][4]涉及H100性能特征但未提供具体显存占用数值；来源[3]讨论FP8/BF16训练权衡但未提供推理显存具体数值。

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
- {'url': 'http://arxiv.org/abs/2411.08719v1', 'type': 'arxiv', 'title': 'Balancing Speed and Stability: The Trade-offs of FP8 vs. BF16 Training in LLMs'}
- {'url': 'http://arxiv.org/abs/2609.19657v1', 'type': 'arxiv', 'title': 'PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LL'}
