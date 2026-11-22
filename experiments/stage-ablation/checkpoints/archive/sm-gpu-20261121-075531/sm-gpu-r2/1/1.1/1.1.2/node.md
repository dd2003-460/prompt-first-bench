# N36: FP8 精度下显存占用修正项：FP8 通常采用 E4M3 或 E5M2 格式，且框架（如 vLLM）可能为 KV Cache 或特定层保留 FP16/BF16 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

FP8 精度下显存占用修正项：FP8 通常采用 E4M3 或 E5M2 格式，且框架（如 vLLM）可能为 KV Cache 或特定层保留 FP16/BF16 副本，需确认 Qwen3-27B 在 FP8 量化下是否所有权重层均为 1 byte/param，还是存在混合精度导致的额外开销（预计偏差 <5%）。

## Corrected Claim

FP8 精度下显存占用修正项：FP8 通常采用 E4M3 或 E5M2 格式（1 byte/param）。需注意框架（如 vLLM）可能为 KV Cache 或特定层保留 FP16/BF16 副本，导致实际显存占用高于纯 FP8 理论值，具体偏差需根据 Qwen3-27B 的量化实现确认。

## Evidence

[质询]该陈述包含具体的经验性预测（Qwen3-27B在FP8量化下的具体偏差<5%）以及特定框架（vLLM）的实现细节（是否保留FP16副本），这些属于经验事实，无法仅从第一性原理推导，且参考来源未提供Qwen3-27B的具体量化实现细节或vLLM的具体内存管理策略。 | 来源[1]和[2]直接支持FP8采用E4M3/E5M2格式（1 byte/param）这一基础事实，但缺乏关于Qwen3-27B具体混合精度开销及vLLM实现细节的直接证据，属于经验事实缺来源支持。

## Search Query

vLLM Qwen3 FP8 quantization weight storage overhead mixed precision

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/574825662&rut=c87a269dfa4d9955dab7d3ae40d9324695e60fe4431c8c6910afaaf110d7b824', 'type': 'ddg', 'title': 'Fp8 量化-原理、实现与误差分析 - 知乎'}
- {'url': 'https://arxiv.org/abs/2209.05433&rut=751ced8ea16ff055fbf137a6a42e4b8a870835e518c0be5a5005136f28825878', 'type': 'ddg', 'title': '[2209.05433] FP8 Formats for Deep Learning - arXiv.org'}
