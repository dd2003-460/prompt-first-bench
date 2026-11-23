# N229: Zipf参数敏感性分析：在N_total=10,000,000固定时，α=0.8（长尾重）对应N_unique_hot ≈ 3,000,000；α=1.0（标准

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Zipf参数敏感性分析：在N_total=10,000,000固定时，α=0.8（长尾重）对应N_unique_hot ≈ 3,000,000；α=1.0（标准幂律）对应N_unique_hot ≈ 1,000,000；α=1.2（头部集中）对应N_unique_hot ≈ 300,000。α值直接决定缓存容量需求的一个数量级差异，需通过实际日志拟合确定。

## Corrected Claim

Zipf参数敏感性分析：在N_total=10,000,000固定时，α=0.8（长尾重）对应N_unique_hot ≈ 3,000,000；α=1.0（标准幂律）对应N_unique_hot ≈ 1,000,000；α=1.2（头部集中）对应N_unique_hot ≈ 300,000。α值直接决定缓存容量需求的一个数量级差异，需通过实际日志拟合确定。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf分布下，α越大头部越集中，唯一热点数量随α增大而显著减少，量级变化符合幂律分布特性。
