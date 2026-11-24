# N276: 共享基础设施 P_Shared_Infra 量化：HDD+SSD 混合阵列的控制器需同时管理两种介质，功耗略高于纯 HDD，约为 40-50W；背板混合供电损耗

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

共享基础设施 P_Shared_Infra 量化：HDD+SSD 混合阵列的控制器需同时管理两种介质，功耗略高于纯 HDD，约为 40-50W；背板混合供电损耗约为 30W；散热风扇因总热量低（~200W IT 负载），P_fan ≈ 15-20W。合计 P_Shared_Infra ≈ 85-100W

## Corrected Claim

共享基础设施 P_Shared_Infra 量化：HDD+SSD 混合阵列的控制器需同时管理两种介质，功耗略高于纯 HDD，约为 40-50W；背板混合供电损耗约为 30W；散热风扇因总热量低（~200W IT 负载），P_fan ≈ 15-20W。合计 P_Shared_Infra ≈ 85-100W

## Evidence

父节点级核验未通过：非正交（子节点存在逻辑矛盾和不一致：1. 总功耗不一致：父节点估算为 85-100W，而子节点最终汇总值为 80W，且第4个子节点明确指出该值低于父节点下限，导致父节点描述与子节点推导结果冲突。2. 风扇功耗矛盾：子节点3将风扇功耗修正为 8-13W（中值10W），但子节点4在计算总和时虽使用了10W，却未明确说明这是基于修正后的值还是原估值的妥协，且父节点仍保留 15-20W 的高估描述，造成内部数据流断裂。3. 背板损耗定义模糊：子节点2计算的 30W 包含了“背板电子元件功耗”，这与通常将背板视为无源或低耗散部件的认知略有偏差，但未构成严重正交性破坏，主要问题在于总值的不匹配。）

## Search Query

hybrid hdd ssd storage array controller power consumption
