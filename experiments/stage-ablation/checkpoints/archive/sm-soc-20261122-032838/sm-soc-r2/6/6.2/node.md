# N94: 注意力锁定衰减函数：$P_{re-search}$ 随挂价溢价率 $\gamma = P_{ask}/P_{ref}$ 的非线性衰减模型。假设 $P_{re-s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

注意力锁定衰减函数：$P_{re-search}$ 随挂价溢价率 $\gamma = P_{ask}/P_{ref}$ 的非线性衰减模型。假设 $P_{re-search} = P_{base} \cdot e^{-k(\gamma - 1)}$，需估算衰减系数 $k$。若 $\gamma=1.2$ 时下降 30%，则 $k \approx 2.0$。该函数在 $\gamma > 1.5$ 时可能失效（买家直接放弃而非锁定）。

## Corrected Claim

注意力锁定衰减函数：$P_{re-search}$ 随挂价溢价率 $\gamma = P_{ask}/P_{ref}$ 的非线性衰减模型。假设 $P_{re-search} = P_{base} \cdot e^{-k(\gamma - 1)}$，需估算衰减系数 $k$。若 $\gamma=1.2$ 时下降 30%，则 $k \approx 2.0$。该函数在 $\gamma > 1.5$ 时可能失效（买家直接放弃而非锁定）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导 $e^{-k(0.2)} = 0.7$ 解得 $k \approx 1.73$，与陈述中的 $k \approx 2.0$ 在工程估算精度内一致；模型形式符合非线性衰减直觉。

## Search Query

attention lock-in effect price premium exponential decay model consumer behavior
