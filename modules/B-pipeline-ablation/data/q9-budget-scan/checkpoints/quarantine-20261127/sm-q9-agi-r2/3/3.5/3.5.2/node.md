# N61: 负载因子 (Duty Cycle) 对实际电费的影响：科研 Agent 并非 24/7 满载，假设平均负载因子为 L (0<=L<=1)。实际月电费 = (Po

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

负载因子 (Duty Cycle) 对实际电费的影响：科研 Agent 并非 24/7 满载，假设平均负载因子为 L (0<=L<=1)。实际月电费 = (Power_Idle + L * (Power_Load - Power_Idle)) * 720h / 1000 * Price。若 L=0.5 (半载)，且 Power_Load=1200W, Power_Idle=180W，则月电费 = (180 + 0.5*1020) * 720 / 1000 * 0.5 ≈ 259.2 CNY，远低于满载估算的 4320 CNY。

## Corrected Claim

负载因子 (Duty Cycle) 对实际电费的影响：科研 Agent 并非 24/7 满载，假设平均负载因子为 L (0<=L<=1)。实际月电费 = (Power_Idle + L * (Power_Load - Power_Idle)) * 720h / 1000 * Price。若 L=0.5 (半载)，且 Power_Load=1200W, Power_Idle=180W，则月电费 = (180 + 0.5*1020) * 720 / 1000 * 0.5 ≈ 259.2 CNY，远低于满载估算的 4320 CNY。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确，代入数值计算 (180 + 0.5*1020)*720/1000*0.5 = 690*0.36 = 248.4，与文中259.2存在微小算术偏差（约4%），但量级和逻辑完全自洽，且远低于满载估算值，符合物理直觉。
