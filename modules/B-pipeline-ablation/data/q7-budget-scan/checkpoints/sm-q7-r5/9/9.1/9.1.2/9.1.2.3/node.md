# N663: SSD 缓存层总功耗 P_SSD_cache 最终值：基于 N247 的 17 块盘和 N248 的 8.1W/盘平均功耗，P_SSD_cache = 17 *

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

SSD 缓存层总功耗 P_SSD_cache 最终值：基于 N247 的 17 块盘和 N248 的 8.1W/盘平均功耗，P_SSD_cache = 17 * 8.1W ≈ 137.7W。若采用 N281 的 55 块 1.92TB 盘方案（假设单盘功耗较低，约 5W active/1W idle -> 3W avg），P_SSD_cache = 55 * 3W = 165W。两种拓扑下功耗均在 140-170W 区间，远高于 N275 原估的 62W，但远低于 N130 的 1.425kW。

## Corrected Claim

SSD 缓存层总功耗 P_SSD_cache 最终值：基于 N247 的 17 块盘和 N248 的 8.1W/盘平均功耗，P_SSD_cache = 17 * 8.1W ≈ 137.7W。若采用 N281 的 55 块 1.92TB 盘方案（假设单盘功耗较低，约 5W active/1W idle -> 3W avg），P_SSD_cache = 55 * 3W = 165W。两种拓扑下功耗均在 140-170W 区间，远高于 N275 原估的 62W，但远低于 N130 的 1.425kW。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（17*8.1=137.7, 55*3=165），功耗量级符合SSD缓存层工程常识，且与上下文节点（N247/N248/N281/N275/N130）数据自洽。
