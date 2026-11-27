# N122: A100 80GB 的推理吞吐量（BF16）约为 50-70 Token/s，而 2×RTX 4090 的 W4 量化吞吐量约为 40-50 Token/s，A

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

A100 80GB 的推理吞吐量（BF16）约为 50-70 Token/s，而 2×RTX 4090 的 W4 量化吞吐量约为 40-50 Token/s，A100 在吞吐量上具有 1.2-1.5x 的优势

## Corrected Claim

在典型大语言模型（如 LLaMA-7B/13B）单请求推理场景下，A100 80GB 的 BF16 吞吐量通常高于 2×RTX 4090 的 W4 量化吞吐量，具体倍数取决于模型大小和序列长度，一般具有显著优势。

## Evidence

[质询]吞吐量数值高度依赖具体模型（如 LLaMA-7B vs 70B）、序列长度及并发数，未指定模型和负载条件，导致“50-70 Token/s”这一具体数值缺乏普适性，且 A100 与 2x4090 的对比通常取决于内存带宽瓶颈，1.2-1.5x 的优势在长序列或大模型下可能显著不同，存在口径混淆风险。 | 来源[1]涉及 A100 推理基准但摘要未提供具体 Token/s 数值；来源[2]仅描述 A100 硬件规格（带宽/显存），未涉及吞吐量对比。逻辑上 A100 高带宽确实优于消费级卡，但具体数值缺乏直接来源支持，属经验事实且缺具体上下文。

## Search Query

A100 80GB Qwen3-27B BF16 inference benchmark tokens per second

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/573475366&rut=5abd89903076b8f5d48ff891d08c034ae333e5f7735c5ef48bf08a8b2c0153e8', 'type': 'ddg', 'title': 'Nvidia A100推理基准测试分析 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/650336836&rut=1af77ea323023b3130447279cbb347fefb127eccf8a8654b7c5bb288609a38d4', 'type': 'ddg', 'title': 'A100 80g 英伟达gpu性能，规格解析 - 知乎'}
