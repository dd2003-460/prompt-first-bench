# N222: 信号分离均衡的边界条件：当 C_signal > C_mimic 时，低质量卖家无法通过高价筛选机制，其模仿概率 P_mimic = 0；该不等式成立的前提是持

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

信号分离均衡的边界条件：当 C_signal > C_mimic 时，低质量卖家无法通过高价筛选机制，其模仿概率 P_mimic = 0；该不等式成立的前提是持有成本 C_wait 随时间 t 线性增长且斜率 r > 0。

## Corrected Claim

信号分离均衡的边界条件：当 C_signal > C_mimic 时，低质量卖家无法通过高价筛选机制，其模仿概率 P_mimic = 0；该不等式成立的前提是持有成本 C_wait 随时间 t 线性增长且斜率 r > 0。

## Evidence

先验知识/题面给定，逻辑校验通过：在信号分离均衡中，若高质量卖家通过高价筛选（如等待或高成本承诺）产生的信号成本 C_signal 高于低质量卖家模仿该信号的成本 C_mimic，则低质量卖家无利可图，模仿概率为0；持有成本随时间线性增长是确保信号成本随时间累积从而形成有效筛选机制的合理前提，逻辑自洽。
