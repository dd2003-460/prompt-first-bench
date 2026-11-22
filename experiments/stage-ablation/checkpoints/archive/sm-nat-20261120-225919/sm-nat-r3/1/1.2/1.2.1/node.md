# N31: 请求热度分布的最小频率 r_min 需通过归一化条件 ∫_{r_min}^{∞} r * f(r) dr = 5×10^7 确定，其中 f(r) = β * r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

请求热度分布的最小频率 r_min 需通过归一化条件 ∫_{r_min}^{∞} r * f(r) dr = 5×10^7 确定，其中 f(r) = β * r_min^β / r^(β+1)，解得 r_min = (5×10^7 / (N * E[R]))，N=100000，E[R] 为单对象平均请求频率

## Corrected Claim

请求热度分布的最小频率 r_min 需通过归一化条件 ∫_{r_min}^{∞} r * f(r) dr = 5×10^7 确定，其中 f(r) = β * r_min^β / r^(β+1)，解得 r_min = (5×10^7 / (N * E[R]))，N=100000，E[R] 为单对象平均请求频率

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点逻辑链条清晰且互斥：子节点1指出父节点公式的理论缺陷（期望发散），子节点2提出修正后的数学模型（离散求和），子节点3执行具体数值计算并指出符号歧义。三者分别对应‘诊断’、‘建模’、‘求解’三个不同阶段，无重复或矛盾，且共同覆盖了从理论纠错到数值落地的完整过程。）

## Search Query

Pareto distribution normalization condition total requests
