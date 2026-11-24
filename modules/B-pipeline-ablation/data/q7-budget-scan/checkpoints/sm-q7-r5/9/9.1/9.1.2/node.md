# N275: SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD_cache = 14 * 4.45W (N92 修正值) ≈ 62W。N130 原估 1.425kW 严重高估，因误用了 95 块盘和 15W 单盘功耗

## Corrected Claim

SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD_cache = 14 * 4.45W (N92 修正值) ≈ 62W。N130 原估 1.425kW 严重高估，因误用了 95 块盘和 15W 单盘功耗

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 存在逻辑矛盾与依赖错误：子节点3引用了子节点1（N247）的17块盘结论，但父节点明确定义为14块盘且子节点1指出14块是错误的，导致子节点3的计算基础与父节点及子节点1的‘修正’意图不一致；2. 存在冗余：子节点3中的‘55块1.92TB盘’方案在子节点1中仅作为对比提及，但在子节点3中展开详细功耗计算，导致同一替代方案在不同节点重复论述，破坏了各子节点独立聚焦单一核心参数的正交性。）

## Search Query

ssd cache layer power consumption small capacity tier
