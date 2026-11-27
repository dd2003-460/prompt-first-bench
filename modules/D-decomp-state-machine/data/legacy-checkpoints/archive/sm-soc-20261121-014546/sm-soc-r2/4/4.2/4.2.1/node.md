# N85: 触发条件阈值 T_trigger：系统监控降价后 48 小时内的咨询数 Q_48。若 Q_48 < Q_crit（如 Q_crit = 1），则触发警告。Q_c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N20

## Claim

触发条件阈值 T_trigger：系统监控降价后 48 小时内的咨询数 Q_48。若 Q_48 < Q_crit（如 Q_crit = 1），则触发警告。Q_crit 的设定需基于历史数据中正常咨询分布的下限（如 P5 分位数）。

## Corrected Claim

触发条件阈值 T_trigger：系统监控降价后 48 小时内的咨询数 Q_48。若 Q_48 < Q_crit（如 Q_crit = 1），则触发警告。Q_crit 的设定需基于历史数据中正常咨询分布的下限（如 P5 分位数）。

## Evidence

先验知识/题面给定，逻辑校验通过
