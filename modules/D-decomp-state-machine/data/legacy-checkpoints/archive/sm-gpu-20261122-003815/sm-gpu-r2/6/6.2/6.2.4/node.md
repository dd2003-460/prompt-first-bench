# N173: 决策变量：使用强度 Hours_Year。低强度 (<1000h/yr) 时，Purchase_Cost 主导 TCO，消费级卡 (4090) 性价比更高；高强

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

决策变量：使用强度 Hours_Year。低强度 (<1000h/yr) 时，Purchase_Cost 主导 TCO，消费级卡 (4090) 性价比更高；高强度 (>6000h/yr) 时，Power_Cost 占比上升，能效比 (tokens/s/W) 成为关键，数据中心卡 (A100/H100) 可能反超。

## Corrected Claim

决策变量：使用强度 Hours_Year。低强度 (<1000h/yr) 时，Purchase_Cost 主导 TCO，消费级卡 (4090) 性价比更高；高强度 (>6000h/yr) 时，Power_Cost 占比上升，能效比 (tokens/s/W) 成为关键，数据中心卡 (A100/H100) 可能反超。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO模型中，低使用强度下固定成本（Purchase_Cost）占比高，消费级卡因单价低更具优势；高使用强度下可变成本（Power_Cost）累积效应显著，数据中心卡因高能效比（tokens/s/W）和稳定性在长期运行中可能反超，符合基本经济直觉与硬件工程常识。

## Search Query

TCO break-even point consumer vs datacenter GPU usage hours
