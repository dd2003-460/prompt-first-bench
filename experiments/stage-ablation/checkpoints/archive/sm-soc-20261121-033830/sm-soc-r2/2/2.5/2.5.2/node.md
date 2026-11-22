# N57: 逆向选择风险降低量 ΔRisk 的量化表达为：ΔRisk = E[Loss|Buy]_pre - E[Loss|Buy]_post，其中 E[Loss|Buy]

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

逆向选择风险降低量 ΔRisk 的量化表达为：ΔRisk = E[Loss|Buy]_pre - E[Loss|Buy]_post，其中 E[Loss|Buy]_pre = (V_max - P) * P(V < P)，E[Loss|Buy]_post 需结合 T 的信号强度进行条件期望计算。

## Corrected Claim

逆向选择风险降低量 ΔRisk 的量化表达为：ΔRisk = E[Loss|Buy]_pre - E[Loss|Buy]_post，其中 E[Loss|Buy]_pre = (V_max - P) * P(V < P)，E[Loss|Buy]_post 需结合 T 的信号强度进行条件期望计算。

## Evidence

先验知识/题面给定，逻辑校验通过
