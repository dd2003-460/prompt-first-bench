# N46: 新咨询触发概率 $P_{inquiry}$ 的阶跃函数形式：$P_{inquiry}(P_{low}) = P_{base} \cdot H(P_{thresh

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

新咨询触发概率 $P_{inquiry}$ 的阶跃函数形式：$P_{inquiry}(P_{low}) = P_{base} \cdot H(P_{threshold} - P_{low})$，其中 $H$ 为海维塞德函数，$P_{base}$ 为基准咨询率。当 $P_{low} > P_{threshold}$ 时，$P_{inquiry} \approx 0$；当 $P_{low} \le P_{threshold}$ 时，$P_{inquiry}$ 恢复至 $P_{base}$（约 5-10%），解释了降价后无咨询的断点效应。

## Corrected Claim

新咨询触发概率 $P_{inquiry}$ 的阶跃函数形式：$P_{inquiry}(P_{low}) = P_{base} \cdot H(P_{threshold} - P_{low})$，其中 $H$ 为海维塞德函数，$P_{base}$ 为基准咨询率。当 $P_{low} > P_{threshold}$ 时，$P_{inquiry} \approx 0$；当 $P_{low} \le P_{threshold}$ 时，$P_{inquiry}$ 恢复至 $P_{base}$（约 5-10%），解释了降价后无咨询的断点效应。

## Evidence

先验知识/题面给定，逻辑校验通过：海维塞德函数定义与阶跃行为描述一致，量级（5-10%）符合一般商业咨询率常识，无内部矛盾。
