# N333: T_detect优化因子：监控覆盖率k_cov影响检测时间，T_detect = T_base / k_cov，其中T_base=10min，k_cov∈[0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

T_detect优化因子：监控覆盖率k_cov影响检测时间，T_detect = T_base / k_cov，其中T_base=10min，k_cov∈[0.5, 1.0]（取决于告警规则覆盖率），高覆盖率可将T_detect降至5min

## Corrected Claim

T_detect优化因子：监控覆盖率k_cov影响检测时间，T_detect = T_base / k_cov，其中T_base=10min，k_cov∈[0.5, 1.0]（取决于告警规则覆盖率），高覆盖率可将T_detect降至5min

## Search Query

monitoring coverage impact on detection time MTTR
