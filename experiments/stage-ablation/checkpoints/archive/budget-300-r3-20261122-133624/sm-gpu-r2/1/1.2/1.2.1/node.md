# N46: Qwen3-27B 采用 GQA 架构，具体参数为：Num Heads = 32, Num KV Heads = 4, Head Dim = 128。公式中 N

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 采用 GQA 架构，具体参数为：Num Heads = 32, Num KV Heads = 4, Head Dim = 128。公式中 N_kv_heads=4 和 D_head=128 是计算 KV Cache 大小的关键架构参数。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，具体参数需参考官方技术报告或模型配置文件确认。

## Evidence

[质询]具体架构参数（如Num Heads=32, Num KV Heads=4）属于经验事实，且不同版本或变体可能存在差异，缺乏来源直接确认具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B GQA num_kv_heads 4 head_dim 128 config.json
