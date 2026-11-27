# N291: 中国居民阶梯电价第一档（0-200 kWh/月）价格为 $0.014/kWh，第二档（201-400 kWh/月）为 $0.018/kWh，第三档（>400 k

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111, N112, N113

## Claim

中国居民阶梯电价第一档（0-200 kWh/月）价格为 $0.014/kWh，第二档（201-400 kWh/月）为 $0.018/kWh，第三档（>400 kWh/月）为 $0.025/kWh；高负载推理（如24/7运行2×RTX4090）月均用电约 620 kWh，加权平均电价约为 $0.021/kWh

## Corrected Claim

中国居民阶梯电价通常分为三档，第一档价格最低，第三档最高；高负载推理（如24/7运行2×RTX4090）月均用电约 620 kWh，加权平均电价高于第一档基础电价。

## Evidence

[质询]具体电价数值（$0.014, $0.018, $0.025）及加权平均值属于经验事实，且不同地区/时期电价存在差异，缺乏来源支持无法确认具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

China residential tiered electricity price 2024 kWh threshold
