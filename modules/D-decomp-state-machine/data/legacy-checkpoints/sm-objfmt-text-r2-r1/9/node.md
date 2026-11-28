# N37: Intel Arc A770 16GB 因显存容量仅 16GB，无法在 BF16 下容纳 Qwen3-27B (54GB) 甚至 INT8 (28GB) 权重加

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Intel Arc A770 16GB 因显存容量仅 16GB，无法在 BF16 下容纳 Qwen3-27B (54GB) 甚至 INT8 (28GB) 权重加 KV Cache，必须依赖极端的量化 (INT4) 或 Offload 到系统内存，后者受限于 DDR5 带宽 (~50-80 GB/s) 导致推理速度降至 5-10 tokens/s，基本丧失本地实时交互能力，应排除出高性价比候选集。

## Corrected Claim

Intel Arc A770 16GB 因显存容量限制，无法在 BF16 或标准 INT8 下完整容纳 Qwen3-27B 权重及 KV Cache，必须依赖 INT4 量化或 Offload 技术。Offload 模式下的推理速度受限于系统内存带宽，通常显著低于全显存加载方案，可能无法满足高实时性交互需求，建议谨慎评估其作为高性价比本地部署方案的可行性。

## Evidence

[质询]陈述中关于“Offload 到系统内存导致推理速度降至 5-10 tokens/s”的具体数值缺乏来源支持，且该速度高度依赖于具体的 CPU 型号、内存通道数及量化方案，属于经验事实而非必然的物理极限；此外，来源 [1] 指出 A770 支持本地推理，但未直接证实“基本丧失本地实时交互能力”这一绝对化结论。 | 逻辑上，Qwen3-27B 在 BF16/INT8 下确实超出 16GB 显存，需依赖 Offload 或极端量化，此部分逻辑自洽且有常识支持；但具体的推理速度数值（5-10 tokens/s）为经验数据，参考来源 [1][2][3] 均未提供该特定场景下的性能基准，仅确认了硬件规格（16GB 显存），故依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://apxml.com/zh/hardware/intel-arc-a770-16gb&rut=30cee3cecd8ba6cb779826be517a6d65d1d6771595414807153fc72cc7e0c304', 'type': 'ddg', 'title': 'Arc A770 (16GB) 最佳适配与运行大模型 - 显存与速度评测'}
- {'url': 'https://www.intel.cn/content/www/cn/zh/products/sku/229151/intel-arc-a770-graphics-16gb/specifications.html&rut=993cb3f796f0f49bac2de2bb322f391a95a021ad728c0fb80c5e07e8abe94717', 'type': 'ddg', 'title': '英特尔锐炫™ A770 显卡 (16 Gb) - 产品规格 | 英特尔'}
- {'url': 'https://www.intel.cn/content/www/cn/zh/support/articles/000092674/graphics.html&rut=0d0ffa185fe6b3f006ca73529fbf8d7941544303a18bc93b760e8bb2494616ce', 'type': 'ddg', 'title': '测试软件，显示英特尔® Arc™ A770 显卡 （16GB） 不正确的内存速度'}
