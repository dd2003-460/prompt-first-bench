# N44: LRU 稳态下对象驻留时间 T_resident 与请求频率 f 的关系：T_resident ≈ 1/f，其中 f 为对象平均访问频率（次/秒），需结合 50

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LRU 稳态下对象驻留时间 T_resident 与请求频率 f 的关系：T_resident ≈ 1/f，其中 f 为对象平均访问频率（次/秒），需结合 5000万次/天 的总请求量与 Pareto(β=0.9) 分布计算特定分位数的 f 值

## Corrected Claim

LRU 稳态下对象驻留时间 T_resident 与请求频率 f 的关系：T_resident ≈ 1/f，其中 f 为对象平均访问频率（次/秒），需结合 5000万次/天 的总请求量与 Pareto(β=0.9) 分布计算特定分位数的 f 值

## Evidence

先验知识/题面给定，逻辑校验通过：在稳态泊松过程或均匀访问假设下，平均驻留时间（或平均间隔时间）与频率互为倒数关系（T=1/f）是基础定义，量纲与逻辑自洽。
