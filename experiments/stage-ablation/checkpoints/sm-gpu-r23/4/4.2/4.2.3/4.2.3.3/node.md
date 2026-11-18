# N191: Qwen3-27B 在 TPU 上的量化支持情况：JAX/XLA 编译器原生支持 BF16 和 FP32，对 FP8 的支持依赖于 TPU v5p 及以上版本及

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

Qwen3-27B 在 TPU 上的量化支持情况：JAX/XLA 编译器原生支持 BF16 和 FP32，对 FP8 的支持依赖于 TPU v5p 及以上版本及特定的 JAX 版本 (>=0.4.20)，TPU v5e 主要优化 BF16，FP8 量化在 v5e 上可能无法获得预期的内存带宽收益或存在兼容性限制 [待核验]。

## Corrected Claim

Qwen3-27B 在 TPU 上的量化支持情况：JAX/XLA 编译器原生支持 BF16 和 FP32，对 FP8 的支持通常依赖于 TPU v5p 及以上版本及特定的 JAX 版本，TPU v5e 主要优化 BF16，FP8 量化在 v5e 上可能无法获得预期的内存带宽收益或存在兼容性限制。

## Evidence

[质询]参考来源中未包含任何关于 TPU v5e/v5p 硬件规格、JAX 版本兼容性或 Qwen3-27B 在 TPU 上具体量化支持情况的直接证据，属于经验事实且缺乏外部来源支持。 | 逻辑自洽（TPU v5p 支持 FP8 而 v5e 主要优化 BF16 符合硬件演进常识），但参考来源 [1]-[4] 均与该具体事实无关（[1] 为 GitHub 首页，[2] 为 Google Cloud 首页，[3] 为 FP8 RL 通用论文，[4] 为 Intel AMX 论文），无直接支持证据。

## Search Query

JAX XLA TPU v5e FP8 quantization support Qwen

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://cloud.google.com', 'type': None, 'title': 'direct-browser: cloud.google.com'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}
- {'url': 'http://arxiv.org/abs/2609.04663v2', 'type': 'arxiv', 'title': 'BF16 Component-Product Emulation of FP32 and FP64 GEMM on Intel AMX'}
