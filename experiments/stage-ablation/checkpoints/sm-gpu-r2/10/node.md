# N35: Prefill 速度（Prompt Processing）主要受算力 (TFLOPS) 限制而非带宽。RTX 4090 (82.6 TFLOPS FP16) 处

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Prefill 速度（Prompt Processing）主要受算力 (TFLOPS) 限制而非带宽。RTX 4090 (82.6 TFLOPS FP16) 处理 32K tokens 的 prefill 时间约为 1.5-2.5 秒；而 A100 (312 TFLOPS FP16) 仅需 0.4-0.6 秒。对于长上下文场景，高算力卡能显著降低首字延迟 (TTFT)。

## Corrected Claim

Prefill 速度主要受算力 (TFLOPS) 限制。在相同模型规模下，RTX 4090 (82.6 TFLOPS) 处理 32K tokens 的 prefill 时间显著长于 A100 (312 TFLOPS)，后者能显著降低首字延迟 (TTFT)。

## Evidence

[质询]具体数值（1.5-2.5秒 vs 0.4-0.6秒）缺乏来源直接支持，且未指定具体模型规模（如7B/70B），不同模型下耗时差异巨大，属于经验事实而非第一性原理可推导的固定值。 | 来源[1]直接支持'Prefill是Compute-Bound（算力受限）'这一核心逻辑，但未提供RTX 4090和A100处理32K tokens的具体耗时数据；该耗时数据为经验事实，逻辑自洽（算力比约3.78倍，耗时比约3-4倍，符合线性关系）但缺来源直接支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2013203040564454281&rut=90c1b4f81c18bf0529d2e10a7aaedfa81e7dea3e417c22e0405d9c4e0a6e214a', 'type': 'ddg', 'title': 'LLM Prefill & Decode — 完整技术图谱 - 知乎'}
