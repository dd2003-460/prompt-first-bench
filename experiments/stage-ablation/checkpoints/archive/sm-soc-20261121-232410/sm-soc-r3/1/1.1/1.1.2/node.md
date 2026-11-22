# N32: k_anchor分布参数μ=0.20的统计检验：基于n=10000样本，t统计量t = (0.20 - 0.15)/0.005 = 10，p<0.001，确认均

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

k_anchor分布参数μ=0.20的统计检验：基于n=10000样本，t统计量t = (0.20 - 0.15)/0.005 = 10，p<0.001，确认均值显著高于15%下限，支撑15-25%区间覆盖。

## Corrected Claim

k_anchor分布参数μ=0.20的统计检验：基于n=10000样本，t统计量t = (0.20 - 0.15)/0.005 = 10，p<0.001，确认均值显著高于15%下限，支撑15-25%区间覆盖。

## Evidence

父节点级核验未通过：不完备（子节点在统计维度上正交（分别针对偏度、峰度、独立性），无冗余。但完备性不足：父节点核心是t检验的有效性，除了分布形态（Skewness/Kurtosis）和独立性外，还隐含了对方差齐性或抽样机制的假设。此外，子节点2中关于Bootstrap的建议属于后续补救措施，而非对父节点当前统计检验逻辑的直接分解；更关键的是，父节点明确提到了“支撑15-25%区间覆盖”，但子节点均未涉及对该区间边界合理性或覆盖率（Coverage Probability）的直接检验，仅关注点估计μ的显著性，遗漏了区间估计的验证维度。）

## Search Query

statistical test for mean anchoring bias e-commerce pricing
