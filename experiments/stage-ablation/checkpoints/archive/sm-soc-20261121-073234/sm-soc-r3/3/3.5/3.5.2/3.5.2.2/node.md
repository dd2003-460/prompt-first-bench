# N238: 投诉率增量 ΔR 的预测模型：ΔR = f(ΔP%, ΔQ%, β_exposure)。若干预导致价格下降 10%，成交量上升 5%，预计 ΔR = 0.3% 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

投诉率增量 ΔR 的预测模型：ΔR = f(ΔP%, ΔQ%, β_exposure)。若干预导致价格下降 10%，成交量上升 5%，预计 ΔR = 0.3% - 0.8%。需监控干预后30天内的投诉数据，若 R_base + ΔR > 1%，则约束失效。

## Corrected Claim

投诉率增量 ΔR 的预测模型：ΔR = f(ΔP%, ΔQ%, β_exposure)。若干预导致价格下降 10%，成交量上升 5%，预计 ΔR = 0.3% - 0.8%。需监控干预后30天内的投诉数据，若 R_base + ΔR > 1%，则约束失效。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

complaint rate prediction model price intervention
