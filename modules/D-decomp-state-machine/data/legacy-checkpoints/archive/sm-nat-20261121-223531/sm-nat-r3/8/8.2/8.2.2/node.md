# N213: N_eff=10,000 对应的热度阈值 h_th：求解 D_i = 10,000 时的 h_i。10,000 = 100,000 * (h_min/h_th)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

N_eff=10,000 对应的热度阈值 h_th：求解 D_i = 10,000 时的 h_i。10,000 = 100,000 * (h_min/h_th)^{0.1} => (h_min/h_th)^{0.1} = 0.1 => h_min/h_th = 0.1^{10} = 10^{-10}。这意味着只有热度极高（h_i > 10^{10} * h_min）的对象才能保持在堆栈前 10,000 位。若 h_min 归一化为 1，则 h_th = 10^{10}。

## Corrected Claim

N_eff=10,000 对应的热度阈值 h_th：求解 D_i = 10,000 时的 h_i。10,000 = 100,000 * (h_min/h_th)^{0.1} => (h_min/h_th)^{0.1} = 0.1 => h_min/h_th = 0.1^{10} = 10^{-10}。这意味着只有热度极高（h_i > 10^{10} * h_min）的对象才能保持在堆栈前 10,000 位。若 h_min 归一化为 1，则 h_th = 10^{10}。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 10000 = 100000 * (h_min/h_th)^0.1 正确解得 h_th = 10^10 * h_min，量纲与数值逻辑自洽。
