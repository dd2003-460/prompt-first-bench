# N35: 自主假设生成最大迭代深度N_max由任务容错率ε决定，N_max = ln(1-ε)/ln(p_step)，若要求ε<0.1（即90%正确率），则N_max约为

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N8

## Claim

自主假设生成最大迭代深度N_max由任务容错率ε决定，N_max = ln(1-ε)/ln(p_step)，若要求ε<0.1（即90%正确率），则N_max约为4-8步，超过此深度需引入人工校验节点。

## Corrected Claim

自主假设生成最大迭代深度N_max由任务容错率ε和单步成功率p_step决定，公式为 N_max = ln(1-ε)/ln(p_step)。在典型的单步高成功率场景下（例如 p_step > 0.9），若要求ε<0.1，N_max通常落在4-8步区间；超过此深度建议引入人工校验节点。

## Evidence

[质询]该公式 N_max = ln(1-ε)/ln(p_step) 隐含了 p_step < 1 且通常接近 1 的假设，但未定义 p_step 的具体取值范围或典型值。若 p_step 较小（如 0.5），N_max 会远大于 4-8；若 p_step 极接近 1，N_max 会非常大。因此，从公式直接得出“4-8步”这一具体数值区间缺乏对 p_step 的约束说明，存在参数依赖导致的结论不确定性。 | source=knowledge，逻辑结构自洽（对数关系符合累积概率模型），但“4-8步”这一具体经验数值依赖于未给出的 p_step 假设，属于经验事实且缺乏来源支持，故降级。
