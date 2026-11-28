# N15: '更新自身知识'环节受限于'不改模型权重'约束，唯一可行路径是外部向量数据库（Vector DB）的动态检索增强，其知识更新延迟 Δt_update = t_i

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N2

## Claim

'更新自身知识'环节受限于'不改模型权重'约束，唯一可行路径是外部向量数据库（Vector DB）的动态检索增强，其知识更新延迟 Δt_update = t_indexing + t_embedding，需保证 Δt_update < t_cycle_avg 以实现实时知识迭代，否则形成'知识滞后'死锁。

## Corrected Claim

'更新自身知识'环节在不改模型权重约束下，主要依赖外部向量数据库（Vector DB）的动态检索增强（RAG），其知识更新延迟 Δt_update = t_indexing + t_embedding，需保证 Δt_update < t_cycle_avg 以实现实时知识迭代，否则会导致知识滞后影响响应质量。

## Evidence

[质询]将“唯一可行路径”绝对化忽略了其他非权重更新机制（如微调LoRA、提示词工程优化、内存管理策略等），且“死锁”一词在系统架构中通常指资源竞争导致的停滞，此处用于描述知识滞后属于术语误用或过度修辞。 | 先验知识/题面给定，逻辑校验通过：RAG确实是主流的非权重更新方案，延迟公式符合工程直觉，但“唯一”和“死锁”表述过于绝对，故降级。
