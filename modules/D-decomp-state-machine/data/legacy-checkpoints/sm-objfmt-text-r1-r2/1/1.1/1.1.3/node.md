# N27: Qwen3-27B 的单个注意力头维度 (head_dim) 确切值为 128，计算公式为 hidden_size / n_heads

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 的单个注意力头维度 (head_dim) 确切值为 128，计算公式为 hidden_size / n_heads

## Corrected Claim

Qwen 系列模型（包括 Qwen3 系列）通常采用 head_dim=128 的设计，具体数值需以 Qwen3-27B 官方发布的 config.json 为准。

## Evidence

[质询]参考来源主要涉及 Qwen3.6/3.8 版本或泛指的 Qwen 系列，未提供 Qwen3-27B 具体版本的官方 config 文件直接证据；虽然 head_dim=128 是 Qwen 系列的常见配置，但不同版本（如 Qwen2 vs Qwen3）可能存在差异，且来源 [1] 和 [3] 提到的模型版本号（3.6/3.8）与待核验的 Qwen3-27B 不完全匹配，存在版本混淆风险。 | 来源 [2] 间接支持 Qwen 系列 head_dim 通常为 128，但缺乏 Qwen3-27B 特定版本的直接配置数据；逻辑上 hidden_size/n_heads=128 符合常见 Transformer 架构设计，但作为经验事实需更精确的来源支持。

## Search Query

Qwen3-27B head_dim hidden dimension size

## Retrieval Sources

- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=dc8a166013362d6a9cce3dbf8a5f64fd158b3f2b0f51dc21a9ad7520fb478aa4', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://blog.csdn.net/yuzhou164/article/details/149415802&rut=54bde5719ac75279f709d2cc1e9020cb4a16dcfa64af3d808429223254186466', 'type': 'ddg', 'title': 'Qwen系列的模型 config 参数理解_qwen3config-CSDN博客'}
- {'url': 'https://blog.csdn.net/liu8485/article/details/164724304&rut=b99d644d79237b0a582cd896a1f3887baddb8412332d8f9dd3af25626e470bbb', 'type': 'ddg', 'title': 'Qwen3.8-27B 混合注意力拆解：48 层线性 + 16 层全注意力，75 万 token KV 显存打到 1/4'}
