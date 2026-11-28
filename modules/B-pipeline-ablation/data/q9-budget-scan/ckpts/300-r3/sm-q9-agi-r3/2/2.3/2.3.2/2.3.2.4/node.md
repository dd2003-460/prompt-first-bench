# N209: 敏感性分析指标：定义 ΔMRR = MRR(w_opt) - MRR(0.7, 0.3)，若 |ΔMRR| < 0.05 (即 5%)，则判定当前权重组合处于平

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

敏感性分析指标：定义 ΔMRR = MRR(w_opt) - MRR(0.7, 0.3)，若 |ΔMRR| < 0.05 (即 5%)，则判定当前权重组合处于平坦区，无需动态调整；否则记录最优权重 (w*_sem, w*_kw) 及对应提升幅度

## Corrected Claim

敏感性分析指标：定义 ΔMRR = MRR(w_opt) - MRR(0.7, 0.3)，若 |ΔMRR| < 0.05 (即 5%)，则判定当前权重组合处于平坦区，无需动态调整；否则记录最优权重 (w*_sem, w*_kw) 及对应提升幅度

## Evidence

先验知识/题面给定，逻辑校验通过
