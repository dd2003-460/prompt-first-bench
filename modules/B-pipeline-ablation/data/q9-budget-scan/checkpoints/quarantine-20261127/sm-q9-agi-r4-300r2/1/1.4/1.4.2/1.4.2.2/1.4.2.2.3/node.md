# N267: 实验设计阶段的 Schema 校验失败率：在 Qwen3-27B 生成实验协议时，若未使用 few-shot 示例，JSON Schema 校验失败率 P_fa

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

实验设计阶段的 Schema 校验失败率：在 Qwen3-27B 生成实验协议时，若未使用 few-shot 示例，JSON Schema 校验失败率 P_fail_schema ≈ 12%；引入 3 个 few-shot 示例后，P_fail_schema 降至 ≈ 3%；每次失败触发重试，增加平均延迟 ΔT_retry ≈ 5s，故优化 Schema 提示可降低端到端设计阶段 15% 的时间开销。

## Corrected Claim

在 Qwen3-27B 生成实验协议时，引入 few-shot 示例通常能显著降低 JSON Schema 校验失败率（例如从两位数百分比降至个位数百分比），从而减少因重试带来的额外延迟，优化端到端设计阶段的时间开销。

## Evidence

[质询]具体数值（12%、3%、5s、15%）缺乏公开基准测试支持，属于特定实验条件下的经验数据，不同实现细节下波动较大，易被质疑为过拟合或特定环境下的偶然结果。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LLM structured output JSON schema validation failure rate few-shot improvement
