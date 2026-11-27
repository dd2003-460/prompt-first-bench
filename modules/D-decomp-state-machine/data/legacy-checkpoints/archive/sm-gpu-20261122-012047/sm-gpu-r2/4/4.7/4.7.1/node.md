# N132: 2×RTX 4090 运行 Qwen3-27B (INT8量化, 32K ctx) 的实测吞吐量约为 18-22 tokens/s/user，首字延迟 (TTF

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

2×RTX 4090 运行 Qwen3-27B (INT8量化, 32K ctx) 的实测吞吐量约为 18-22 tokens/s/user，首字延迟 (TTFT) 约为 2.5-4.0 秒，该数值基于 PCIe 瓶颈下的并行效率衰减估算。

## Corrected Claim

2×RTX 4090 运行 Qwen3.8-27B (128K ctx) 的部署方案可行，但具体吞吐量与TTFT需依据该特定配置实测，原陈述中关于 Qwen3-27B (32K ctx) 的 18-22 tokens/s 及 2.5-4.0s TTFT 缺乏直接来源支持。

## Evidence

[质询]来源[1]标题及摘要明确提及的是 'Qwen3.8-27B' 且配置为 '128K 上下文'，而待核验事实声称是 'Qwen3-27B' 且配置为 '32K ctx'。模型版本（Qwen3 vs Qwen3.8）和上下文长度（32K vs 128K）均存在显著差异，导致性能指标（吞吐量、TTFT）不可直接迁移。此外，来源摘要未提供具体的吞吐量数值（18-22 tokens/s）或TTFT数值（2.5-4.0s），无法直接支持具体数值。 | 来源[1]主题相关（双4090部署Qwen系列27B模型），但模型版本（Qwen3.8 vs Qwen3）和上下文长度（128K vs 32K）不匹配，且摘要未提供具体性能数值，仅能间接参考其可行性，无法直接支持具体数值，故降级。

## Search Query

2x RTX 4090 Qwen3 27B INT8 inference throughput tokens per second benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2095101571461920165&rut=8b6e4860e5f4ef6788a43f9abb14a8f7b8e0d44134f6bf7ffca7b6f599095f73', 'type': 'ddg', 'title': '双 RTX 4090 本地部署 Qwen3.8-27B：从零搭建 vLLM，到 128K 上下文、10 路并发与工具调用'}
