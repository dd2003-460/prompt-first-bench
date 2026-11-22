# N209: Mac Studio M2 Ultra MLX 框架 INT8 吞吐量矛盾解析：N95 声称 3-5 tokens/s，但 N163 基于带宽计算得出 45.9

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Mac Studio M2 Ultra MLX 框架 INT8 吞吐量矛盾解析：N95 声称 3-5 tokens/s，但 N163 基于带宽计算得出 45.9 tokens/s，两者相差 10 倍；差异根源在于 N95 可能基于早期 MLX 版本未启用 Metal GPU 加速或使用了 CPU 回退路径，而 N163 假设理想带宽利用；需核验 MLX 在 M2 Ultra 上对 27B 模型 INT8 的实测基准，当前 MLX 官方文档未提供 Qwen3-27B 具体吞吐数据 [待核验]。

## Corrected Claim

N209: Mac Studio M2 Ultra MLX 框架 INT8 吞吐量存在显著差异：理论带宽计算（N163）约为 45.9 tokens/s，而早期或特定配置下的实测报告（N95）可能低至 3-5 tokens/s。这种 10 倍以上的差异可能源于软件版本、GPU 加速启用状态或计算路径（CPU vs GPU）的不同。当前公开来源未提供统一的 MLX 官方基准数据以确证具体数值，需以实际环境测试为准。

## Evidence

[质询]N95声称的3-5 tokens/s吞吐量极低，对于M2 Ultra（80GB统一内存，带宽约800GB/s）运行27B INT8模型（约27GB权重）而言，即使考虑CPU回退或早期软件瓶颈，该数值也远低于理论下限（通常CPU回退也能达到10+ tokens/s），且参考来源中未提供MLX在Mac Studio上的具体实测数据来直接证实这一特定低值，存在将极端异常值或错误配置当作典型情况的风险。 | 参考来源[1][2][3]主要关注Qwen3.8-27B的规格、通用基准测试（如单GPU BF16/FP8）及内存需求，未直接提供Mac Studio M2 Ultra上MLX框架INT8的具体吞吐量实测数据，无法直接验证N95与N163的具体数值矛盾及根源，但逻辑上带宽计算（N163）与软件瓶颈（N95）的差异解释在原理上自洽，属于经验事实且缺乏直接来源支持。

## Search Query

MLX framework Qwen3-27B INT8 throughput M2 Ultra tokens per second benchmark

## Retrieval Sources

- {'url': 'https://ai-on-mac.com/articles/qwen3-8-27b-en/&rut=a7cfe245a3313c6b4a201d6f9503ef768b8e385d59a3056a70d4ae3914503cd0', 'type': 'ddg', 'title': 'Qwen3.8-27B: specs, MLX builds, Mac memory and launch-day facts'}
- {'url': 'https://local-ai-zone.github.io/blog/qwen3-8-27b-comprehensive-analysis.html&rut=7c3045d5392e98e4ba7afd243ad9337bb696fa0b8aef9358026a1b70e5e6299b', 'type': 'ddg', 'title': 'Qwen3.8-27B: A Comprehensive Technical Analysis - Local AI Zone'}
- {'url': 'https://www.aieev.com/post/qwen3-8-27b-benchmark&rut=ee5e2835f9836b39b5671863bca21eaaf38278dd174dd93c66c0a5f111d0afc0', 'type': 'ddg', 'title': 'Qwen3.8-27B Benchmarks: Throughput, Latency and KV Cache'}
