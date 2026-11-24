# N650: 故障时刻分布 P(t) 的先验假设：若无特定历史数据，通常假设故障在一天内均匀分布 P(t)=1/24；但若业务存在明显高峰（如凌晨批处理写入高峰），则 P(i

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N225

## Claim

故障时刻分布 P(t) 的先验假设：若无特定历史数据，通常假设故障在一天内均匀分布 P(t)=1/24；但若业务存在明显高峰（如凌晨批处理写入高峰），则 P(incremental) 需在低峰期（增量小）更高，P(full) 在高峰后（累积变更大）更高；需定义“高峰”阈值 V_peak_change。

## Corrected Claim

故障时刻分布 P(t) 的先验假设：若无特定历史数据，通常假设故障在一天内均匀分布 P(t)=1/24；但若业务存在明显高峰（如凌晨批处理写入高峰），则 P(incremental) 需在低峰期（增量小）更高，P(full) 在高峰后（累积变更大）更高；需定义“高峰”阈值 V_peak_change。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud failure time distribution assumption uniform peak load
