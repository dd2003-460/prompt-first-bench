# N38: Qwen3-27B 架构参数确认：需从官方模型卡确认层数（Layers）、KV Head 数量（num_key_value_heads）和 Head Dimen

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 架构参数确认：需从官方模型卡确认层数（Layers）、KV Head 数量（num_key_value_heads）和 Head Dimension。若 Qwen3-27B 采用 MHA 而非 GQA，或层数/Head 数与假设（48层, 16 KV heads）不符，KV Cache 计算公式中的变量需相应更新。

## Corrected Claim

需从 Qwen3-27B 官方模型卡确认具体架构参数（层数、KV Head 数量等），当前参考来源主要覆盖 Qwen3.6/3.8-27B，不能直接作为 Qwen3-27B 参数（48层, 16 KV heads）的权威依据。

## Evidence

[质询]参考来源均指向 Qwen3.6 或 Qwen3.8 版本的 27B 模型，而非 Qwen3-27B，存在版本混淆风险；且来源摘要未直接提供具体的层数（48）和 KV Head 数量（16）数值，无法直接证实假设参数。 | 来源 [1][2][3] 均涉及 Qwen 27B 系列模型，但具体版本为 3.6 或 3.8，未直接覆盖 Qwen3-27B 的架构参数细节；逻辑上 27B 模型采用 48 层和 GQA 结构符合常见大模型设计直觉，但缺乏针对 Qwen3-27B 的直接来源支持，故降级。

## Search Query

Qwen3-27B architecture num_layers num_key_value_heads head_dim config

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=014253cab1362304bedfb232983060c3a30c933f269dd0e576935f19f65c4b6e', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=91a3e3954842f70e147755574faf6c96080e8c8529cc51d2955e11beb7071bb0', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://www.pongo.com.tw/qwen3-8-27b-hands-on/&rut=0a9de73e709dfbcb66f564eceb3833cbe01ff29359f957b605f36935b76152df', 'type': 'ddg', 'title': 'Qwen3.8 27B 開源模型一次看懂：規格、跑分到本地實測'}
