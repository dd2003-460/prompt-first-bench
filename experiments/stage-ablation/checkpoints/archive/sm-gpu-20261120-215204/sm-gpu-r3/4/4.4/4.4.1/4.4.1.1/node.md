# N294: Qwen3-27B 的 GQA 架构参数：Query Heads=40, KV Heads=10, Head Dim=128, Layers=64 (基于 Qw

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

Qwen3-27B 的 GQA 架构参数：Query Heads=40, KV Heads=10, Head Dim=128, Layers=64 (基于 Qwen3 系列公开配置，需核验具体版本)

## Corrected Claim

Qwen3-27B 采用 GQA 架构，具体参数（Query Heads, KV Heads, Head Dim, Layers）需查阅官方技术报告或配置文件确认。

## Evidence

[质询]具体数值（Query Heads=40, KV Heads=10, Layers=64）属于特定模型版本的经验事实，且不同版本（如 Qwen2.5 与 Qwen3）或不同尺寸（27B 可能对应不同配置）可能存在差异，缺乏来源支持无法确认具体数值准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B architecture config num_key_value_heads num_attention_heads head_dim
