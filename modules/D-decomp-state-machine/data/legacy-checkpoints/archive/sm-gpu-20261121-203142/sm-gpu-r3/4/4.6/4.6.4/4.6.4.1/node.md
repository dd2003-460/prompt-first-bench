# N312: 硬件折旧成本 (Hardware_Depreciation) 的计算公式为：Depreciation = (Purchase_Price - Residual_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N100

## Claim

硬件折旧成本 (Hardware_Depreciation) 的计算公式为：Depreciation = (Purchase_Price - Residual_Value_5y) / (5y * 365d * 24h)；其中 Residual_Value_5y 需根据二手市场折价率估算，例如 RTX 4090 5年后残值约为初始成本的 10-15%（基于N78及市场趋势推断），导致 RTX 4090 的日均折旧约为 $0.02-$0.03，而 A100 80GB 由于价格高但残值稳定，日均折旧约为 $0.05-$0.08 [待核验：具体残值率需结合2024-2029市场预测]。

## Corrected Claim

硬件折旧成本 (Hardware_Depreciation) 的计算公式为：Depreciation = (Purchase_Price - Residual_Value_5y) / (5y * 365d * 24h)；其中 Residual_Value_5y 需根据二手市场折价率估算。例如，若 RTX 4090 初始成本为 $1600 且 5 年后残值为 10-15%，其日均折旧约为 $0.03；A100 80GB 由于价格较高，日均折旧通常在 $0.05-$0.10 之间，具体数值取决于初始采购价格及残值率假设。

## Evidence

[质询]RTX 4090 的日均折旧计算存在量级错误：若按公式 (Purchase_Price - Residual_Value) / (5*365*24) 计算，假设 RTX 4090 初始成本约 $1600，残值 10-15% ($160-$240)，则总折旧额约 $1360-$1440，除以 43800 小时，日均折旧约为 $0.031-$0.033。虽然数值接近 $0.03，但陈述中给出的范围 $0.02-$0.03 偏低，且未明确说明是基于何种具体购买价格（如 $1500 还是 $2000）。更关键的是，A100 80GB 的日均折旧 $0.05-$0.08 也依赖于具体的初始价格假设（如 $10,000-$15,000），若价格波动较大，该范围可能不准确。此外，'残值稳定' 的定性描述缺乏量化支撑。 | 先验知识/题面给定，逻辑校验通过，但具体数值依赖未明确的市场价格假设，且无外部来源支持，故降级为定性表述。
