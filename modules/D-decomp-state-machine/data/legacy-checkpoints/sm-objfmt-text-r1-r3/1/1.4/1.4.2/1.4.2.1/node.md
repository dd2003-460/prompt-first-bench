# N109: Qwen3-27B 架构参数确认：层数 (L)=64, 注意力头数 (H)=8 (GQA), 每头维度 (D_head)=128, 总维度 D_model=10

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33, N34, N35

## Claim

Qwen3-27B 架构参数确认：层数 (L)=64, 注意力头数 (H)=8 (GQA), 每头维度 (D_head)=128, 总维度 D_model=1024 (8*128), 该参数组合决定了 KV Cache 的基础计算因子。

## Corrected Claim

Qwen3-27B 的架构参数需以官方技术报告为准，当前陈述中的具体数值（L=64, H=8, D_head=128）未经外部来源验证，建议核实官方文档。

## Evidence

[质询]Qwen3-27B 的具体架构参数（如层数、头数、维度）属于经验事实，且不同版本或配置可能存在差异，缺乏权威来源直接确认该特定组合（L=64, H=8, D_head=128）是否为官方标准配置。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B architecture parameters num_hidden_layers num_key_value_heads head_dim config.json
