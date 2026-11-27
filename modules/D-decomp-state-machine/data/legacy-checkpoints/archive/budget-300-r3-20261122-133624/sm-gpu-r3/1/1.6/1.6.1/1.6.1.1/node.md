# N218: Qwen3-27B 的 KV Head 数量确认：根据 Qwen3 技术报告，27B 模型采用 GQA (Grouped Query Attention)，GQ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Qwen3-27B 的 KV Head 数量确认：根据 Qwen3 技术报告，27B 模型采用 GQA (Grouped Query Attention)，GQA Group Size 为 4，即 32 个 Query Heads 对应 8 个 KV Heads。因此 TP=2 时，每卡承载 8/2 = 4 个 KV Heads，而非 claim 中声称的 2 个。

## Corrected Claim

Qwen3-27B 若采用 GQA 且 Group Size 为 4，则 32 个 Query Heads 对应 8 个 KV Heads，TP=2 时每卡承载 4 个 KV Heads；但具体 Group Size 需以官方技术报告为准。

## Evidence

[质询]该陈述包含具体的模型架构参数（Qwen3-27B 的 KV Head 数量及 GQA 配置），属于经验事实。由于检索通道失败，无法通过外部来源直接验证 Qwen3-27B 是否确实采用 GQA Group Size 为 4 的配置，存在参数记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体架构参数）

## Search Query

Qwen3 27B GQA group size KV heads count
