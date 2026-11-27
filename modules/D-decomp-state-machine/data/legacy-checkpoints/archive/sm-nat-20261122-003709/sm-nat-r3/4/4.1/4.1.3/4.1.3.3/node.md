# N180: 推导在固定总数据量约束下的有效缓存覆盖率修正：若实际平均大小 E[S_real] = 1MB（总数据量100TB），则缓存容量128GB覆盖的字节比例 P_co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

推导在固定总数据量约束下的有效缓存覆盖率修正：若实际平均大小 E[S_real] = 1MB（总数据量100TB），则缓存容量128GB覆盖的字节比例 P_cov_real = 128GB / 100TB ≈ 0.128%；对比理论模型下的 P_cov_theoretical = 128GB / 1TB ≈ 12.8%，量化模型假设错误导致的覆盖率低估倍数。

## Corrected Claim

推导在固定总数据量约束下的有效缓存覆盖率修正：若实际平均大小 E[S_real] = 1MB（总数据量100TB），则缓存容量128GB覆盖的字节比例 P_cov_real = 128GB / 100TB ≈ 0.128%；对比理论模型下的 P_cov_theoretical = 128GB / 1TB ≈ 12.8%，量化模型假设错误导致的覆盖率低估倍数。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/100TB = 0.128%，128GB/1TB = 12.8%，倍数关系100倍，计算无误
