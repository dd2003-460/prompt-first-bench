# N91: 硬件采购价 (Hardware_Capex) 的折旧模型采用直线法 (Straight-line) 或 MACRS 加速折旧，对于3年TCO计算，通常假设残值率

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21

## Claim

硬件采购价 (Hardware_Capex) 的折旧模型采用直线法 (Straight-line) 或 MACRS 加速折旧，对于3年TCO计算，通常假设残值率为 5%-10% (例如 RTX 4090 3年后二手残值约为原价的 30-40%，而 A100 约为 50-60%)，需明确折旧年限与残值率参数以计算年均折旧成本。

## Corrected Claim

硬件采购价的折旧模型通常采用直线法或MACRS加速折旧。在3年TCO计算中，需明确折旧年限与残值率参数；残值率通常根据硬件类型和市场行情假设（例如消费级显卡与数据中心GPU的残值率存在显著差异），具体数值需结合当期二手市场行情确定。

## Evidence

[质询]陈述中关于具体硬件（RTX 4090, A100）3年后二手残值的具体百分比（30-40% vs 50-60%）属于高度波动的市场经验数据，缺乏稳定的第一性原理支撑，且不同时期、不同供需状况下差异巨大，作为通用TCO计算假设的精确数值引用存在风险。 | source=knowledge，逻辑自洽（直线法/MACRS是标准折旧模型，残值率假设是TCO计算必要参数），但具体硬件残值率属于经验事实，无外部来源支持，且数值精确度存疑，故降级。

## Search Query

GPU residual value after 3 years straight line depreciation MACRS
