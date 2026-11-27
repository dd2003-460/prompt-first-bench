# N220: C_wait（等待高价值买家的持有成本）的时间衰减模型：C_wait(t) = r*P_ref*t + D(t)，其中 r 为资金占用率（如年化 5%/365）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

C_wait（等待高价值买家的持有成本）的时间衰减模型：C_wait(t) = r*P_ref*t + D(t)，其中 r 为资金占用率（如年化 5%/365），D(t) 为商品折旧或过时风险成本，t 为等待时间（小时）。

## Corrected Claim

C_wait（等待高价值买家的持有成本）的时间衰减模型：C_wait(t) = r*P_ref*t + D(t)，其中 r 为资金占用率（如年化 5%/365），D(t) 为商品折旧或过时风险成本，t 为等待时间（小时）。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合经济学中持有成本（Holding Cost）的基本构成（资金时间价值+折旧/风险），量纲与逻辑自洽。
