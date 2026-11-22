# N39: Qwen3-27B 的实际参数量为 27.1B（非整数27B），在 BF16 下精确显存占用为 27.1 * 2 = 54.2 GB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的实际参数量为 27.1B（非整数27B），在 BF16 下精确显存占用为 27.1 * 2 = 54.2 GB

## Corrected Claim

Qwen3-27B 的参数量约为 27B，在 BF16 下显存占用约为 54 GB

## Evidence

[质询]具体参数量数值（27.1B）属于经验事实，且无来源支持，可能存在微小偏差（如实际为27.0B或27.2B），导致显存计算不精确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B exact parameter count HuggingFace config.json
