# N296: Qwen3-27B 的 `max_position_embeddings` 官方支持上限为 131072 (128K)，确认 32K 上下文在模型架构原生支持范

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

Qwen3-27B 的 `max_position_embeddings` 官方支持上限为 131072 (128K)，确认 32K 上下文在模型架构原生支持范围内，无需 RoPE 外推修正。

## Corrected Claim

Qwen3-27B 官方支持长上下文（通常宣称支持 128K 或更长），32K 上下文在其原生支持范围内，具体 max_position_embeddings 数值及 RoPE 外推策略需查阅官方技术报告确认。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（max_position_embeddings=131072），属于经验事实。虽然 Qwen3 系列确实支持长上下文，但具体数值（128K vs 其他如 32K/64K/1M）需官方文档确认，且‘无需 RoPE 外推’这一结论依赖于具体的 RoPE 缩放配置（如 YaRN 或 NTK-aware），仅凭 max_position_embeddings 数值不能绝对排除训练时使用了插值或外推技术，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体参数值及 RoPE 配置细节）

## Search Query

Qwen3-27B max_position_embeddings context window limit 128k
