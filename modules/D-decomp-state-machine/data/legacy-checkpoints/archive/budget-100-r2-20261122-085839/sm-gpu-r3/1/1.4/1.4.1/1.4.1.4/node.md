# N142: INT8 权重 + FP8 KV Cache 方案在 32K 上下文、Batch=1 时的总显存需求精确值 = 27.1 (权重) + N126 计算值 (KV

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

INT8 权重 + FP8 KV Cache 方案在 32K 上下文、Batch=1 时的总显存需求精确值 = 27.1 (权重) + N126 计算值 (KV) + N127 计算值 (激活) + N128 计算值 (开销)，需计算总和并判断是否低于 48GB (A6000 Ada) 或 80GB (A100)，以验证 N112 中'可能超出 48GB'的担忧是否成立

## Corrected Claim

INT8 权重 + FP8 KV Cache 方案在 32K 上下文、Batch=1 时的总显存需求 = 27.1 (权重) + N126 (KV) + N127 (激活) + N128 (开销)，需代入具体数值后判断是否低于 48GB 或 80GB。

## Evidence

[质询]该陈述依赖于 N126、N127、N128 的具体计算值，而这些值在当前上下文中未给出，且 27.1GB 的权重显存对应特定模型规模（如 7B-14B 参数），若模型规模不同，总显存需求将显著变化，无法仅凭此陈述验证是否低于 48GB 或 80GB。 | 逻辑自洽，但缺乏 N126-N128 的具体数值支持，无法完成最终判断，属于经验事实且缺来源支持。
