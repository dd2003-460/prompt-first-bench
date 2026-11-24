# N63: 单 POP 电力成本 Power_Cost = P_Servers × P_Efficiency × Energy_Rate × 720h，其中 P_Serve

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

单 POP 电力成本 Power_Cost = P_Servers × P_Efficiency × Energy_Rate × 720h，其中 P_Servers 为 2 台服务器总功耗约 500W（含散热冗余），P_Efficiency 取 PUE=1.5，Energy_Rate 为商业电价 ¥0.8/kWh，计算得 Power_Cost ≈ 500W × 1.5 × 0.8 ¥/kWh × 720h ≈ ¥4,320/月/POP [时效待核]。

## Corrected Claim

单 POP 电力成本 Power_Cost = P_Servers × P_Efficiency × Energy_Rate × 720h，其中 P_Servers 为 2 台服务器总功耗约 500W（含散热冗余），P_Efficiency 取 PUE=1.5，Energy_Rate 为商业电价 ¥0.8/kWh，计算得 Power_Cost ≈ 500W × 1.5 × 0.8 ¥/kWh × 720h ≈ ¥4,320/月/POP [时效待核]。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对公式中的三个独立变量（P_Servers, PUE, Energy_Rate）进行敏感性分析和取值讨论，维度互斥且无重叠。父节点公式包含的四个核心参数中，720h为固定时间常数无需分解，其余三个变量均已覆盖，逻辑完备且无冗余。）
