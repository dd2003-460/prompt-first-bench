# N119: 平均带宽利用率 U_avg 受流量日内波动模式影响，计算公式为 U_avg = (Daily_Traffic_TB / (Peak_Bandwidth_Gbps

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

平均带宽利用率 U_avg 受流量日内波动模式影响，计算公式为 U_avg = (Daily_Traffic_TB / (Peak_Bandwidth_Gbps × 86400 / 8))，若流量遵循典型双峰分布（早晚高峰），U_avg 通常低于时间平均利用率，需通过蒙特卡洛模拟或历史流量曲线积分计算实际有效利用率。

## Corrected Claim

平均带宽利用率 U_avg 受流量日内波动模式影响，计算公式为 U_avg = (Daily_Traffic_TB / (Peak_Bandwidth_Gbps × 86400 / 8))，若流量遵循典型双峰分布（早晚高峰），U_avg 通常低于时间平均利用率，需通过蒙特卡洛模拟或历史流量曲线积分计算实际有效利用率。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（TB/Gbps换算系数86400/8合理），双峰分布导致平均利用率低于峰值或时间平均值的逻辑符合网络流量工程常识。
