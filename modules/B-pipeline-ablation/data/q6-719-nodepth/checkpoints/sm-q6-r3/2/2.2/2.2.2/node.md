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

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应公式中的三个核心变量（P_Servers, PUE, Energy_Rate），彼此独立且无逻辑重叠；共同覆盖了公式的所有关键参数维度，无冗余。）
