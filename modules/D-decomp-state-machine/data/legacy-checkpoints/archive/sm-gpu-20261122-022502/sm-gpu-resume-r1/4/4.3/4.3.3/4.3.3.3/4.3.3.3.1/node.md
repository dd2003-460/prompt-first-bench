# N837: Qwen3-27B 在 BF16 精度下的 KV Cache 大小计算：每 token 的 KV Cache 大小为 2 * num_layers * hidd

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N261

## Claim

Qwen3-27B 在 BF16 精度下的 KV Cache 大小计算：每 token 的 KV Cache 大小为 2 * num_layers * hidden_size * dtype_size = 2 * 64 * 4096 * 2 bytes = 1,048,576 bytes ≈ 1MB（基于 Qwen3-27B 架构参数 [search]），而非 12.58GB/32 tokens 的假设值。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 KV Cache 大小计算依赖于其具体架构参数（层数、隐藏层维度等）。若假设 num_layers=64 且 hidden_size=4096，则每 token 的 KV Cache 大小为 2 * 64 * 4096 * 2 bytes = 1,048,576 bytes ≈ 1MB。需核实 Qwen3-27B 的实际架构参数以确认该数值。

## Evidence

[质询]Qwen3-27B 的具体架构参数（如 num_layers=64, hidden_size=4096）属于经验事实，且不同版本或变体可能存在差异，若无确切来源支持，存在参数错误导致计算结果偏差的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B architecture parameters num_layers hidden_size kv cache size
