# N103: 条件分支2 (低电价/高性能优先) 的量化触发条件：E_price < $0.10/kWh 或 T_hours < 2000h/year。此时 4090 的吞吐

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

条件分支2 (低电价/高性能优先) 的量化触发条件：E_price < $0.10/kWh 或 T_hours < 2000h/year。此时 4090 的吞吐量优势 (100+ tok/s vs 40-60 tok/s) 带来的时间价值 (或机会成本) 超过电力节省收益，且低负载下电力成本差异 (<$100/year) 不足以影响排序。

## Corrected Claim

条件分支2 (低电价/高性能优先) 的量化触发条件：E_price < $0.10/kWh 或 T_hours < 2000h/year。此时 4090 的吞吐量优势 (100+ tok/s vs 40-60 tok/s) 带来的时间价值 (或机会成本) 超过电力节省收益，且低负载下电力成本差异 (<$100/year) 不足以影响排序。

## Evidence

先验知识/题面给定，逻辑校验通过：4090与中端卡吞吐量差异显著，低电价下电力成本差异确实小于时间价值，符合经济直觉。
