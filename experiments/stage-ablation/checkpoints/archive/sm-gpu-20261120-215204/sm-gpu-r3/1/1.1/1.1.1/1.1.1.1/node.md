# N157: Qwen3-27B 的 GQA (Grouped Query Attention) 架构中，KV Cache 的头部数量 (Num_KV_Heads) 为 4，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N39

## Claim

Qwen3-27B 的 GQA (Grouped Query Attention) 架构中，KV Cache 的头部数量 (Num_KV_Heads) 为 4，而非 N39 公式中使用的 8（N39 可能混淆了 Q-Head 数量或使用了错误的架构假设，Qwen3-27B 通常采用 8 组 KV，每组 1 个头，或者具体配置需核实，但主流 27B 级别如 Qwen2.5-32B 为 8 KV heads，若 Qwen3-27B 结构不同需修正）。注：经查证 Qwen3 系列 27B 模型通常继承 Qwen2.5 架构，KV Heads 为 8，但需确认 Qwen3 是否有变更。若 KV Heads 确为 8，则 N39 公式中 8 正确，但需确认是否为 MQA/GQA 的分组数。此处暂按 N39 的 8 进行后续计算，但标记架构参数需 [待核验]。

## Corrected Claim

Qwen3-27B 的 GQA 架构中，KV Cache 的头部数量 (Num_KV_Heads) 具体数值需查阅官方模型配置卡确认，不能简单断言为 4 或 8；N39 公式中使用的 8 可能基于 Qwen2.5 系列架构假设，若 Qwen3-27B 架构有变则需修正。

## Evidence

[质询]该陈述本身是一个关于架构参数的经验事实断言，且内部存在逻辑矛盾：一方面声称 Num_KV_Heads 为 4，另一方面又引用 Qwen2.5-32B 为 8 并推测 Qwen3 可能继承该架构，导致结论自相矛盾（既说 4 又说可能 8）。此外，Qwen3-27B 的具体 KV Heads 数量属于硬件/模型配置经验事实，无法从第一性原理推导，且当前无可用来源支持其具体数值（是 4 还是 8 或其他）。 | 经验事实，逻辑自洽但缺来源支持；且陈述内部对 KV Heads 数量（4 vs 8）存在不确定性及潜在矛盾，无法确定具体数值。

## Search Query

Qwen3-27B architecture num_key_value_heads config.json
