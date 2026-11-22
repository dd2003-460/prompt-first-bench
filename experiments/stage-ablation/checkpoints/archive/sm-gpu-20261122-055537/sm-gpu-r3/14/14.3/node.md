# N399: Speculative 级别数据的误差量化标准：基于理论推导（如 Roofline 模型计算上限）或单一传闻，误差 > 20%；判定条件为无实测数据支持，或仅基

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

Speculative 级别数据的误差量化标准：基于理论推导（如 Roofline 模型计算上限）或单一传闻，误差 > 20%；判定条件为无实测数据支持，或仅基于单点推测，且理论模型未包含实际系统开销（如内核启动、内存拷贝、同步等待），导致预测值与实测值偏差通常超过 20%。

## Corrected Claim

Speculative 级别数据的误差量化标准：基于理论推导（如 Roofline 模型计算上限）或单一传闻，误差 > 20%；判定条件为无实测数据支持，或仅基于单点推测，且理论模型未包含实际系统开销（如内核启动、内存拷贝、同步等待），导致预测值与实测值偏差通常超过 20%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

theoretical roofline model vs actual performance gap LLM inference
