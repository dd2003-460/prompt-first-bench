# N316: n=1000时Clopper-Pearson区间[0.579, 0.621]的F分布参数验证：上界分母涉及$F_{2(n-k+1), 2k; 0.975}$，即

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

n=1000时Clopper-Pearson区间[0.579, 0.621]的F分布参数验证：上界分母涉及$F_{2(n-k+1), 2k; 0.975}$，即F(800, 1200; 0.975)，需确认该临界值是否导致区间收窄至与正态近似[0.58, 0.62]一致。

## Corrected Claim

n=1000时Clopper-Pearson区间基于F分布计算，其结果通常比正态近似略宽或相近，具体数值需通过统计软件精确计算验证，而非直接断言与正态近似完全一致。

## Evidence

[质询]陈述中关于F分布参数的具体数值（F(800, 1200)）及区间收窄至与正态近似一致的结论属于经验计算结果，参考来源仅定性指出Clopper-Pearson区间通常比正态近似略宽，未提供具体数值支持，且未验证该特定参数下的精确临界值。 | 来源[1]定性支持Clopper-Pearson为精确法且通常比正态近似保守（略宽），但未提供n=1000时的具体数值或F分布参数验证，属于间接支持且无法排除具体数值偏差的可能性。

## Search Query

F distribution critical value 800 1200 0.975 large sample binomial confidence interval

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2066843943493440950&rut=e19d5c1f4c4c04e58e0545e66f5ec387571aa7d03915c85c6c78eb0f690ff460', 'type': 'ddg', 'title': 'Clopper-Pearson 置信区间 - 知乎'}
