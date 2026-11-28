# N580: 在科研 AGI 自动化流程中，执行 n=196 次独立实验的总耗时 T_total = n * T_single_experiment；若单次实验耗时 T_si

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

在科研 AGI 自动化流程中，执行 n=196 次独立实验的总耗时 T_total = n * T_single_experiment；若单次实验耗时 T_single=10min（含数据采集与分析），则 T_total = 196 * 10 = 1960 min ≈ 32.7 小时，需评估是否超出单日算力预算上限（基于 N339 的日均 57-86 次循环能力）

## Corrected Claim

在科研 AGI 自动化流程中，执行 n=196 次独立实验的总耗时 T_total = n * T_single_experiment；若单次实验耗时 T_single=10min（含数据采集与分析），则 T_total = 196 * 10 = 1960 min ≈ 32.7 小时，需评估是否超出单日算力预算上限（基于 N339 的日均 57-86 次循环能力）

## Evidence

先验知识/题面给定，逻辑校验通过：196 * 10 = 1960 min，1960 / 60 ≈ 32.67 小时，计算无误且量级合理。
