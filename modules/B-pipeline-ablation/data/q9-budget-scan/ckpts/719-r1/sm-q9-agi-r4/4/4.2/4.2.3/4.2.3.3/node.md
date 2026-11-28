# N218: ΔFCR显著性检验：采用配对样本t检验，假设FCR_0.7 - FCR_0.1 = Δ，若p-value < 0.05则认为差异显著；同时计算效应量Cohen'

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

ΔFCR显著性检验：采用配对样本t检验，假设FCR_0.7 - FCR_0.1 = Δ，若p-value < 0.05则认为差异显著；同时计算效应量Cohen's d = Δ / pooled_std，若d > 0.2则认定低温设置具有实际工程价值，否则维持默认temperature。

## Corrected Claim

ΔFCR显著性检验：采用配对样本t检验，假设FCR_0.7 - FCR_0.1 = Δ，若p-value < 0.05则认为差异显著；同时计算效应量Cohen's d = Δ / pooled_std，若d > 0.2则认定低温设置具有实际工程价值，否则维持默认temperature。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应统计检验的三个独立维度：前提假设验证（正态性）、效应量计算方法的修正（分母选择）、以及样本量与检验力的可行性分析。它们互不重叠且逻辑上相互支撑，共同构成了对父节点中‘显著性检验’和‘效应量判断’的完整方法论闭环。没有发现冗余或矛盾。）
