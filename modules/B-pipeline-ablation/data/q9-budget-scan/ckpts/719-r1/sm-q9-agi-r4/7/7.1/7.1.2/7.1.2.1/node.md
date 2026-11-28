# N734: Qwen3.8-27B 的架构参数具体值：num_layers=48, num_heads=32, num_kv_heads=8 (GQA), head_dim

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N272

## Claim

Qwen3.8-27B 的架构参数具体值：num_layers=48, num_heads=32, num_kv_heads=8 (GQA), head_dim=128, hidden_dim=5120, intermediate_dim=13824, dtype=NVFP4 (等效存储 4bits/weight, 激活 FP16/BF16)。

## Corrected Claim

Qwen3.8-27B 的架构参数具体值待官方技术报告确认，当前提供的数值（num_layers=48, num_heads=32, num_kv_heads=8, head_dim=128, hidden_dim=5120, intermediate_dim=13824）缺乏外部证据支持。

## Evidence

[质询]Qwen3.8-27B 并非公开已知的标准模型版本（截至当前知识库，Qwen 系列主要包含 Qwen2.5, Qwen3 等，且 27B 通常对应特定 MoE 或 Dense 配置，具体参数如 num_layers=48, hidden_dim=5120 需精确匹配官方技术报告，存在参数张冠李戴或虚构的风险） | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体架构参数值）

## Search Query

Qwen3 27B config.json num_layers num_kv_heads head_dim hidden_dim
