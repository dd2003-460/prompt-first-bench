# N400: 匹配效率系数 k_match 的构成：k_match = k_signal_quality * k_algorithm_speed，其中 k_signal_qu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

匹配效率系数 k_match 的构成：k_match = k_signal_quality * k_algorithm_speed，其中 k_signal_quality 取决于平台信号强度 S_sig（参考 N130），k_algorithm_speed 取决于推荐算法的迭代频率 f_iter（次/天）。若 f_iter < 1，则 k_algorithm_speed < 0.5，导致公式失效，需引入时间滞后项 T_lag。

## Corrected Claim

匹配效率系数 k_match 的构成：k_match = k_signal_quality * k_algorithm_speed，其中 k_signal_quality 取决于平台信号强度 S_sig（参考 N130），k_algorithm_speed 取决于推荐算法的迭代频率 f_iter（次/天）。若 f_iter < 1，则 k_algorithm_speed < 0.5，导致公式失效，需引入时间滞后项 T_lag。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

recommendation algorithm iteration frequency impact on matching efficiency
