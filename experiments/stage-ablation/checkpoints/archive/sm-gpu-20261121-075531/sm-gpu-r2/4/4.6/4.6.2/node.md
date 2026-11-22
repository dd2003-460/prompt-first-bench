# N98: Qwen3-27B 在 32K 上下文长度下，W4/INT4 量化与 BF16 基线的困惑度差异 (ΔPPL_32K) 及长文本一致性得分（如 LongBenc

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

Qwen3-27B 在 32K 上下文长度下，W4/INT4 量化与 BF16 基线的困惑度差异 (ΔPPL_32K) 及长文本一致性得分（如 LongBench 子集）下降幅度，需对比 4K 短上下文下的 ΔPPL，以量化累积误差系数 k = ΔPPL_32K / ΔPPL_4K。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，W4/INT4 量化与 BF16 基线的困惑度差异 (ΔPPL_32K) 及长文本一致性得分下降幅度需通过实际基准测试获取，以量化累积误差系数 k = ΔPPL_32K / ΔPPL_4K；当前提供的参考来源未包含相关数据。

## Evidence

[质询]参考来源与事实主题严重不匹配：来源[1]指向的是 'Qwen3.8-27B'（一个不存在的版本号，且描述为 Image-Text-to-Text 多模态模型），而事实节点讨论的是 'Qwen3-27B' 的纯文本量化困惑度（PPL）及长文本一致性指标。来源既未提供 W4/INT4 量化数据，也未提供 32K/4K 上下文下的 PPL 对比或 LongBench 得分，属于完全无关的来源。 | 逻辑上，定义累积误差系数 k = ΔPPL_32K / ΔPPL_4K 在数学上是自洽的，用于量化长上下文下的误差累积是合理的工程方法。但根据经验事实排除条款，具体的量化性能差异（ΔPPL）和基准测试得分属于经验事实，无法从第一性原理推出。由于提供的参考来源 [1] 与事实主题（Qwen3-27B 文本量化性能）完全无关（来源指向错误的模型版本和模态），缺乏直接支持证据，故判定为 degraded。

## Search Query

Qwen3 27B INT4 W4 quantization LongBench score drop 32k context

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=3d7831a77a0759778bf5fe7ec23242f552eacd18fef689ac2e5e92ec3eccaa2a', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
