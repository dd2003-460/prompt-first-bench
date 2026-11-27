# N124: 理论吞吐公式修正：实际吞吐 = 理论吞吐 × 效率系数 η，η 受 KV Cache 访问模式、Attention 计算开销、CUDA Kernel 启动延迟影

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

理论吞吐公式修正：实际吞吐 = 理论吞吐 × 效率系数 η，η 受 KV Cache 访问模式、Attention 计算开销、CUDA Kernel 启动延迟影响；RTX 4090 上 η ≈ 0.5-0.7，RTX 3090 上 η ≈ 0.4-0.6，L40S 上 η ≈ 0.5-0.65 [待核验：需实测不同硬件上 Qwen3-27B 的 tokens/s 与理论值比值]

## Corrected Claim

理论吞吐公式修正：实际吞吐 = 理论吞吐 × 效率系数 η，η 受 KV Cache 访问模式、Attention 计算开销、CUDA Kernel 启动延迟影响；具体数值需根据硬件型号、推理框架及量化策略实测确定，通常显著低于 1.0。

## Evidence

[质询]具体数值范围（如 RTX 4090 上 η ≈ 0.5-0.7）属于经验事实，且不同推理框架（vLLM vs Ollama）、量化精度及并发设置下效率系数波动极大，缺乏统一基准下的实测数据直接支持该特定区间。 | 逻辑自洽（实际吞吐必然低于理论峰值），但参考来源 [1][2][3] 仅提供了特定模型版本（Qwen3.6/3.8）在 RTX 4090 上的绝对吞吐或延迟数据，未直接提供与理论峰值对比得出的效率系数 η 的具体数值范围，且未覆盖 RTX 3090 和 L40S 的数据，属于经验事实缺直接来源支持。

## Search Query

RTX 4090 Qwen3-27B inference throughput benchmark

## Retrieval Sources

- {'url': 'https://radianvector.com/benchmarks/qwen3-8-27b-rtx-4090/&rut=951cf1149bc28dcdd087d7503178f013622bbbbd6d9b4980ef62ab19ee12e1fa', 'type': 'ddg', 'title': 'Qwen3.8-27B vLLM Benchmark on the RTX 4090 GPU family'}
- {'url': 'https://markaicode.com/benchmarks/cuda-qwen-3-rtx-4090-latency-benchmark/&rut=337e04a2274be1644b72cd854e5f47eef40f1c04c58012371d67a438ea888d54', 'type': 'ddg', 'title': 'Ollama Qwen3.6 27B on RTX 4090: Speed & VRAM Benchmark'}
- {'url': 'https://markaicode.com/benchmarks/ollama-qwen-3-rtx-4090-latency-benchmark/&rut=6254ceb30acb416fe027f6f2b2a8dc8394cc6cbf71569e5fbe9a73b64bd517df', 'type': 'ddg', 'title': 'Qwen3 on RTX 4090: Ollama Speed & VRAM Benchmarks (2026)'}
