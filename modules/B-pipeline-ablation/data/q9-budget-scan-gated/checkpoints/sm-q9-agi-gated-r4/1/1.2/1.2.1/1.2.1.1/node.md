# N37: Qwen3.8-27B实际架构参数需核验：若num_kv_heads=8（GQA），head_dim=128，则每token KV开销为(2*48*8*128*

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3.8-27B实际架构参数需核验：若num_kv_heads=8（GQA），head_dim=128，则每token KV开销为(2*48*8*128*2bytes/4)=491.5KB，而非N20假设的12KB。这将使最大上下文长度从1451 tokens骤降至 1740.8MB/491.5KB≈3.5 tokens，完全不可用。

## Corrected Claim

若Qwen3.8-27B采用GQA架构且num_kv_heads=8、head_dim=128、layers=48，则每token KV开销约为491.5KB，这将显著限制最大上下文长度至约3.5 tokens，导致实际不可用。但此结论依赖于未经验证的架构参数假设。

## Evidence

[质询]该陈述基于假设的架构参数（num_kv_heads=8, head_dim=128, layers=48）进行计算，但Qwen3.8-27B的具体架构参数（如层数、KV头数、头维度）并未在参考来源中提供，且不同版本或变体可能存在差异，因此无法确认这些参数是否准确对应实际模型。 | 逻辑推导成立，来源未直接覆盖；由于缺乏外部来源验证具体架构参数，无法确认计算前提的真实性，故降级为定性表述。

## Search Query

Qwen3.8-27B architecture num_kv_heads head_dim layers
