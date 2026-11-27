# N58: Qwen3-27B 的 Key/Value 头数 (Num_KV_Heads) 确切值为 8，采用 Grouped Query Attention (GQA) 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3-27B 的 Key/Value 头数 (Num_KV_Heads) 确切值为 8，采用 Grouped Query Attention (GQA) 架构，来源于模型配置文件中 num_key_value_heads 字段，该值直接决定 KV Cache 大小。

## Corrected Claim

Qwen3-27B 采用 Grouped Query Attention (GQA) 架构，其 Key/Value 头数 (Num_KV_Heads) 通常为 8（需以具体模型配置文件为准，参考来源主要覆盖 Qwen3.6/3.8 版本）。

## Evidence

[质询]参考来源均指向 Qwen3.6/3.8 版本，未直接覆盖 Qwen3-27B 的具体配置；且 Qwen3 系列不同版本（如 3.0 vs 3.5/3.6）架构可能存在差异，直接套用其他版本的参数存在版本混淆风险。 | 来源 [1][2][3] 均讨论 Qwen3.6/3.8-27B 的 KV Cache 与注意力机制，虽未直接列出 Qwen3-27B 的 num_key_value_heads=8，但逻辑上 GQA 架构下 KV 头数少于 Q 头数符合常理，且 27B 模型采用 8 个 KV 头是常见配置，但缺乏针对 'Qwen3-27B' 这一特定版本的直接来源支持，属于经验事实且来源版本不匹配。

## Search Query

Qwen3-27B num_key_value_heads GQA

## Retrieval Sources

- {'url': 'https://blog.csdn.net/liu8485/article/details/164338425&rut=4bc854ca6ec356ff2a2c6e012ea542769f5ea266399968c9ec9b5fd267c0679a', 'type': 'ddg', 'title': 'Qwen3.8-27B 长上下文部署实战：一条 vLLM 命令吃下 75 万 token（含 NUMA 拓扑实测）'}
- {'url': 'https://blog.csdn.net/liu8485/article/details/164724304&rut=6143faec21e24e807e8d0e2eeb0020e9f95da667b5d523357c23d9c331a36495', 'type': 'ddg', 'title': 'Qwen3.8-27B 混合注意力拆解：48 层线性 + 16 层全注意力，75 万 token KV 显存打到 1/4'}
- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=91a3e3954842f70e147755574faf6c96080e8c8529cc51d2955e11beb7071bb0', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
