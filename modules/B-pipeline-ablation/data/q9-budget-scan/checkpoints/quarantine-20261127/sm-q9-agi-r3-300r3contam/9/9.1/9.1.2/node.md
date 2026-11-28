# N241: 投机解码盈亏平衡点 (Break-even Point)：当接受率 α 低于临界值 α_crit 时，投机解码反而变慢。α_crit 取决于草稿模型生成成本与验

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

投机解码盈亏平衡点 (Break-even Point)：当接受率 α 低于临界值 α_crit 时，投机解码反而变慢。α_crit 取决于草稿模型生成成本与验证成本之比。对于 MTP (无独立草稿模型，仅额外头)，α_crit 通常高于独立草稿模型。若 α(L) < α_crit，则 T_speculative > T_standard，此时应禁用 MTP 或降低 MTP 步数 K。

## Corrected Claim

投机解码盈亏平衡点 (Break-even Point)：当接受率 α 低于临界值 α_crit 时，投机解码反而变慢。α_crit 取决于草稿模型生成成本与验证成本之比。对于 MTP (无独立草稿模型，仅额外头)，α_crit 通常高于独立草稿模型。若 α(L) < α_crit，则 T_speculative > T_standard，此时应禁用 MTP 或降低 MTP 步数 K。

## Evidence

先验知识/题面给定，逻辑校验通过：投机解码加速比公式表明当接受率低于由计算开销决定的临界值时，额外验证步骤导致总延迟增加，MTP因共享主干网络验证成本略高或结构差异，其临界点特性符合逻辑推导。

## Search Query

speculative decoding break even point acceptance rate multi-token prediction overhead
