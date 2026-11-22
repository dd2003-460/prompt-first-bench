# N78: 拉普拉斯分布与正态分布在尾部概率上的精确对比公式：对于 $\epsilon > k\sigma$，$P_{Laplace} / P_{Normal} = \fr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

拉普拉斯分布与正态分布在尾部概率上的精确对比公式：对于 $\epsilon > k\sigma$，$P_{Laplace} / P_{Normal} = \frac{2 e^{-\epsilon/\lambda}}{\frac{2}{\sqrt{2\pi}} e^{-\epsilon^2/(2\sigma^2)}}$，需代入 $\epsilon=0.25$（25%偏差）、$\lambda=0.15$ 和对应的 $\sigma$（需确定 $\sigma$ 与 $\lambda$ 的关系，通常 $\sigma = \lambda\sqrt{2}$），计算实际倍数是否确为 2.4 倍。

## Corrected Claim

拉普拉斯分布与正态分布在尾部概率上的精确对比公式：对于 $\epsilon > k\sigma$，$P_{Laplace} / P_{Normal} = \frac{2 e^{-\epsilon/\lambda}}{\frac{2}{\sqrt{2\pi}} e^{-\epsilon^2/(2\sigma^2)}}$，需代入 $\epsilon=0.25$（25%偏差）、$\lambda=0.15$ 和对应的 $\sigma$（需确定 $\sigma$ 与 $\lambda$ 的关系，通常 $\sigma = \lambda\sqrt{2}$），计算实际倍数是否确为 2.4 倍。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点逻辑清晰且正交：节点1解决参数映射（σ与λ的关系），节点2执行父节点要求的精确数值验证（计算2.4倍），节点3提供额外的理论背景（渐近行为）。它们覆盖了父节点中关于公式、参数确定、具体计算和结论验证的所有关键方面，且无内容重复。）
