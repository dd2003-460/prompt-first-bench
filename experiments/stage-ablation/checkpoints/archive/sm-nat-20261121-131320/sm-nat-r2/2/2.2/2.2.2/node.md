# N33: β=0.9 时头部对象流量集中度 C_head：C_head = (Σ_{i=1}^{K} f_i) / (Σ_{all} f_i)；利用 Pareto(β=0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

β=0.9 时头部对象流量集中度 C_head：C_head = (Σ_{i=1}^{K} f_i) / (Σ_{all} f_i)；利用 Pareto(β=0.9) 的 CDF，计算前 K 个对象（K 由 N21 得出）占据的总请求比例；该值直接决定 LFU 的理论命中率上限 H_LFU_max ≈ C_head * (1 - Size_Penalty)。

## Corrected Claim

β=0.9 时头部对象流量集中度 C_head：C_head = (Σ_{i=1}^{K} f_i) / (Σ_{all} f_i)；利用 Pareto(β=0.9) 的 CDF，计算前 K 个对象（K 由 N21 得出）占据的总请求比例；该值直接决定 LFU 的理论命中率上限 H_LFU_max ≈ C_head * (1 - Size_Penalty)。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 命中率上限由头部对象流量集中度决定符合缓存理论第一性原理，公式定义自洽。
