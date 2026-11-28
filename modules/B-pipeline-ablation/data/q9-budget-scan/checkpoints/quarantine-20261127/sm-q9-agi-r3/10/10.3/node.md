# N297: JSON Schema 约束增加的 Token 开销 ΔTokens = (Schema_Length + FewShot_Examples_Length) *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105, N106, N107

## Claim

JSON Schema 约束增加的 Token 开销 ΔTokens = (Schema_Length + FewShot_Examples_Length) * Frequency；若 Schema 为 500 tokens，Few-shot 为 200 tokens，每步调用频率为 1，则每步增加 700 tokens；对比原 Prompt 5000 tokens，增加比例为 700/5000 = 14%，与声称的 15% 一致，需评估这 14% 增量对首字延迟 (TTFT) 的影响约为 +200ms (按 50 tokens/s 计算)。

## Corrected Claim

JSON Schema 约束增加的 Token 开销 ΔTokens = (Schema_Length + FewShot_Examples_Length) * Frequency；若 Schema 为 500 tokens，Few-shot 为 200 tokens，每步调用频率为 1，则每步增加 700 tokens；对比原 Prompt 5000 tokens，增加比例为 700/5000 = 14%，与声称的 15% 一致，需评估这 14% 增量对首字延迟 (TTFT) 的影响约为 +200ms (按 50 tokens/s 计算)。

## Search Query

structured output token overhead latency impact LLM
