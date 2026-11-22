# N57: 逆向选择风险降低量 ΔRisk 的量化表达为：ΔRisk = E[Loss|Buy]_pre - E[Loss|Buy]_post，其中 E[Loss|Buy]

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

逆向选择风险降低量 ΔRisk 的量化表达为：ΔRisk = E[Loss|Buy]_pre - E[Loss|Buy]_post，其中 E[Loss|Buy]_pre = (V_max - P) * P(V < P)，E[Loss|Buy]_post 需结合 T 的信号强度进行条件期望计算。

## Corrected Claim

逆向选择风险降低量 ΔRisk 的量化表达为：ΔRisk = E[Loss|Buy]_pre - E[Loss|Buy]_post，其中 E[Loss|Buy]_pre = (V_max - P) * P(V < P)，E[Loss|Buy]_post 需结合 T 的信号强度进行条件期望计算。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3（ΔRisk的符号与量级）在内容上严重依赖于子节点1和2的定义，且其给出的近似公式存在逻辑漏洞，导致子节点间存在包含与重复关系，非正交。）
