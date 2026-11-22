# N44: LRU 稳态下对象驻留时间 T_resident 与请求频率 f 的关系：T_resident ≈ 1/f，其中 f 为对象平均访问频率（次/秒），需结合 50

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LRU 稳态下对象驻留时间 T_resident 与请求频率 f 的关系：T_resident ≈ 1/f，其中 f 为对象平均访问频率（次/秒），需结合 5000万次/天 的总请求量与 Pareto(β=0.9) 分布计算特定分位数的 f 值

## Corrected Claim

LRU 稳态下对象驻留时间 T_resident 与请求频率 f 的关系：T_resident ≈ 1/f，其中 f 为对象平均访问频率（次/秒），需结合 5000万次/天 的总请求量与 Pareto(β=0.9) 分布计算特定分位数的 f 值

## Evidence

父节点级核验失败（LLM 错误）：Expecting value: line 9 column 133 (char 851)
