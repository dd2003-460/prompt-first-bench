# N110: RX 7900 XTX 的 TDP 为 355W，低于 RTX 4090 (450W) 和 RTX 5090 (575W)；在 $0.15/kWh 电价下，每小

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

RX 7900 XTX 的 TDP 为 355W，低于 RTX 4090 (450W) 和 RTX 5090 (575W)；在 $0.15/kWh 电价下，每小时电力成本比 4090 低 $0.01425，3 年 (6000 小时) 节省 $85.5；若 TPS 仅比 4090 低 10%，则 TCO 仍可能优于 4090 单卡方案。

## Corrected Claim

RX 7900 XTX 的 TDP 为 355W，低于 RTX 4090 (450W) 和 RTX 5090 (575W)；在 $0.15/kWh 电价下，每小时电力成本比 4090 低 $0.01425，3 年 (6000 小时) 节省 $85.5；若 TPS 仅比 4090 低 10%，则 TCO 仍可能优于 4090 单卡方案。

## Evidence

先验知识/题面给定，逻辑校验通过：TDP数值符合公开规格，电力成本计算（0.15 * (450-355)/1000 = $0.01425）及3年节省金额（$0.01425 * 6000 = $85.5）数学推导正确，TCO逻辑自洽。

## Search Query

RX 7900 XTX TDP power consumption watts
