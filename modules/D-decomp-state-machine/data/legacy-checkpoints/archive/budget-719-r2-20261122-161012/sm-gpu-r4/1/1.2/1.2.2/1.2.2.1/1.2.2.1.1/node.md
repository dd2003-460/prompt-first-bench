# N352: Qwen3-27B 的 GQA 分组因子为 5 (num_query_heads=40 / num_kv_heads=8)，而非题目假设的 4；相比 MHA (

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146

## Claim

Qwen3-27B 的 GQA 分组因子为 5 (num_query_heads=40 / num_kv_heads=8)，而非题目假设的 4；相比 MHA (40:40) 将 KV Cache 降低 80% (1/5)，相比 MQA (40:1) 保留了 8 个独立 KV 头以平衡性能与显存，此修正直接影响 N145 的显存计算基数

## Corrected Claim

Qwen3-27B 采用 GQA 架构，其 KV Cache 显存占用相比 MHA 显著降低（具体降低比例取决于实际头数配置，通常约为 1/4 至 1/8），相比 MQA 保留了多个独立 KV 头以平衡性能与显存。

## Evidence

[质询]具体架构参数（num_query_heads=40, num_kv_heads=8）属于经验事实，且检索无可用来源，无法排除其他可能的头数配置（如 32 或 64 头），存在参数记忆偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体头数参数）

## Search Query

Qwen3-27B num_key_value_heads config GQA ratio
