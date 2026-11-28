# N458: 延迟注入对总耗时的线性影响公式：T_total = T_compute + sum(t_i for i in range(n_calls))，其中 T_comp

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160

## Claim

延迟注入对总耗时的线性影响公式：T_total = T_compute + sum(t_i for i in range(n_calls))，其中 T_compute 为模型推理与数据处理耗时，n_calls 为单次任务中工具调用次数（假设 n_calls=5），若 t=1s 则额外耗时 5s，占 T_total 比例 = 5/(T_compute+5)

## Corrected Claim

延迟注入对总耗时的线性影响公式：T_total = T_compute + sum(t_i for i in range(n_calls))，其中 T_compute 为模型推理与数据处理耗时，n_calls 为单次任务中工具调用次数（假设 n_calls=5），若 t=1s 则额外耗时 5s，占 T_total 比例 = 5/(T_compute+5)

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合加法延迟模型，数值代入（5*1s=5s）及比例计算逻辑自洽，无内部矛盾。
