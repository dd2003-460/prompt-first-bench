# N97: Throughput_tokens_per_sec 的量化定义：在特定精度（如FP8）和上下文长度（32K）下，单卡或集群每秒生成的Token数。需分别列出 R

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Throughput_tokens_per_sec 的量化定义：在特定精度（如FP8）和上下文长度（32K）下，单卡或集群每秒生成的Token数。需分别列出 RTX 4090 (FP8), H100 (FP8/BF16), MI300X (FP8) 的实测或理论峰值吞吐数据，公式：Throughput = 1 / T_decode_avg

## Corrected Claim

Throughput_tokens_per_sec 定义为在特定精度和上下文长度下，单卡或集群每秒生成的Token数，公式为 Throughput = 1 / T_decode_avg。具体硬件（如 RTX 4090, H100, MI300X）的实测或理论峰值吞吐数据需查阅具体基准测试报告，当前来源未提供具体数值。

## Evidence

[质询]该陈述要求列出特定硬件（RTX 4090, H100, MI300X）在特定精度和上下文长度下的具体实测或理论峰值吞吐数据，但参考来源仅提供了 Token/sec 的通用定义，未包含任何具体硬件的性能数值，属于经验事实缺失来源支持。 | 来源[1]和[2]直接支持了 Throughput_tokens_per_sec 的定义（每秒生成的Token数），但作为经验事实（具体硬件性能参数），缺乏具体数值来源支持，故降级。

## Search Query

Qwen3-27B inference throughput tokens per second RTX 4090 H100 MI300X FP8 32K context

## Retrieval Sources

- {'url': 'https://aionely.com/posts/20260729-tokens-per-second-llm-throughput-explainer/&rut=79fa31be243b73270ab4d6945f629ecf8a2b3c32541abfcd8768ad89c73a7e16', 'type': 'ddg', 'title': 'Token/sec 是什麼？它不是模型跑分，而是 LLM 服務真正吐字的速度'}
- {'url': 'https://inferensys.com/glossary/inference-optimization-and-latency-reduction/inference-performance-benchmarking/tokens-per-second-tps&rut=1074af979e382e3687b1de9e7edda23f46a07c079220fdf0e4c33f9447e58585', 'type': 'ddg', 'title': 'Tokens Per Second (TPS): Definition & AI Inference Metric'}
