# N34: 缓存容量占比 p_cache = C / S_total 的具体数值：若 S_total 由 N31 修正后计算得出（假设 E[S] ≈ 10KB 作为合理估计

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

缓存容量占比 p_cache = C / S_total 的具体数值：若 S_total 由 N31 修正后计算得出（假设 E[S] ≈ 10KB 作为合理估计），则 S_total = 100,000 * 10KB = 1GB，p_cache = 128GB / 1GB = 128。这表明缓存容量远超总数据量，命中率理论上限为 100%，与题设“边缘节点”场景不符，需重新审视 s_min/s_max 假设或 N 值。

## Corrected Claim

缓存容量占比 p_cache = C / S_total 的具体数值：若 S_total 由 N31 修正后计算得出（假设 E[S] ≈ 10KB 作为合理估计），则 S_total = 100,000 * 10KB = 1GB，p_cache = 128GB / 1GB = 128。这表明缓存容量远超总数据量，命中率理论上限为 100%，与题设“边缘节点”场景不符，需重新审视 s_min/s_max 假设或 N 值。

## Evidence

先验知识/题面给定，逻辑校验通过：基于假设参数（N=100,000, E[S]=10KB, C=128GB）计算 S_total=1GB，p_cache=128，数值量级与逻辑推导自洽，且正确指出了该结果与边缘节点场景的矛盾。
