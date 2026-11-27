# N37: Qwen3-27B 的 Transformer 层数 (num_layers) 为 64 层，这是计算 KV Cache 大小的关键乘数，直接线性影响显存占用。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 的 Transformer 层数 (num_layers) 为 64 层，这是计算 KV Cache 大小的关键乘数，直接线性影响显存占用。

## Corrected Claim

Qwen3-32B 的 Transformer 层数为 64 层；Qwen3-27B 的具体层数需查阅其官方配置，但通常同系列相近规模模型层数可能一致，此处暂无法确认为64层。

## Evidence

[质询]参考来源中明确提到的64层Transformer结构属于Qwen3-32B（来源[2]）或Qwen3.8-27B（来源[3]，且为混合架构），而非Qwen3-27B。Qwen3-27B的具体层数在提供的来源中未直接证实，存在将不同型号（32B vs 27B）或不同版本（3.8 vs 3）的架构参数混淆的风险。 | 来源[2]证实Qwen3-32B为64层，来源[3]提及Qwen3.8-27B总层数为64（混合架构），但均非Qwen3-27B的直接证据；逻辑上64层对于27B-32B量级模型是合理的，但缺乏针对Qwen3-27B的直接来源支持，且存在型号混淆风险。

## Search Query

Qwen3-27B model architecture num_layers 64 hidden_size config

## Retrieval Sources

- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=0b10fe0d815af316e8374ea97a2024ed873765fdf7691a90951d7aedc81374a1', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://blog.csdn.net/gitblog_00033/article/details/151733507&rut=846674eec5e651f1be84ea0c521eb32dd20754549d6280297fcf5139d2f43350', 'type': 'ddg', 'title': 'Qwen3-32B模型结构解析：64层Transformer与GQA注意力机制详解-CSDN博客'}
- {'url': 'https://happyrock.cloud/zh/blog/2026-08-16_qwen3.8-27b/&rut=ff5963c6a54a58b1b0014eabdeb929f279a0d8deb38fd28e90bcec34cc78fd66', 'type': 'ddg', 'title': 'Qwen3.8-27B混合注意力架构深度解析：48层Gated DeltaNet + 16层Attention如何让270亿参数模型跑在消费级 ...'}
