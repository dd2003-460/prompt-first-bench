# N40: Qwen3-27B 实际架构配置：num_layers=64, num_kv_heads=8 (GQA 8:1), head_dim=128，验证 KV Cac

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 实际架构配置：num_layers=64, num_kv_heads=8 (GQA 8:1), head_dim=128，验证 KV Cache 公式输入参数

## Corrected Claim

Qwen3-27B 采用 GQA 架构，具体参数（num_layers=64, num_kv_heads=8, head_dim=128）需查阅官方模型配置文件（config.json）以最终确认。

## Evidence

[质询]参考来源均为通用项目主页或无关论文，未提供 Qwen3-27B 的具体架构参数（如 num_layers, num_kv_heads），无法通过给定来源直接验证具体数值。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2]仅确认模型存在，未覆盖具体参数；来源[3]无关）。

## Search Query

Qwen3-27B model config num_layers num_key_value_heads head_dim

## Retrieval Sources

- {'url': 'https://github.com/QwenLM/Qwen3', 'type': 'bing', 'title': 'GitHub - QwenLM/Qwen3: Qwen3 is the large language model series ...'}
- {'url': 'https://huggingface.co/collections/Qwen/qwen3', 'type': 'bing', 'title': 'Qwen3 - a Qwen Collection - Hugging Face'}
- {'url': 'http://arxiv.org/abs/2408.11104v3', 'type': 'arxiv', 'title': 'ConFIG: Towards Conflict-free Training of Physics Informed Neural Networks'}
