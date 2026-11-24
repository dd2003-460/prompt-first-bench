# N102: 隐性运维成本修正项：Total_Ops_Cost = 105k + (Failure_Rate × MTTR_Hours × Hourly_Ops_Cost) 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

隐性运维成本修正项：Total_Ops_Cost = 105k + (Failure_Rate × MTTR_Hours × Hourly_Ops_Cost) + (Patch_Frequency × Patch_Validation_Hours × Hourly_Ops_Cost)，其中 Failure_Rate 由硬件/软件故障率决定，MTTR 由 10 POP 分布及备件库存决定。

## Corrected Claim

隐性运维成本修正项：Total_Ops_Cost = 105k + (Failure_Rate × MTTR_Hours × Hourly_Ops_Cost) + (Patch_Frequency × Patch_Validation_Hours × Hourly_Ops_Cost)，其中 Failure_Rate 由硬件/软件故障率决定，MTTR 由 10 POP 分布及备件库存决定。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点之间存在逻辑重叠和分类维度混乱。1. 正交性问题：Hardware_Failure_Cost 中包含了 Spare_Part_Replacement_Cost（消耗品成本），而 Spare_Part_Inventory_CapEx 是库存持有成本，两者虽不同但紧密耦合，且 Hardware_Failure_Cost 的公式结构隐含了故障导致的停机成本，这与父节点中 Failure_Rate × MTTR × Hourly_Cost 对应，但父节点未明确区分‘消耗’与‘持有’。2. 冗余/压缩问题：Spare_Part_Inventory_CapEx 本质上是一个固定资本支出或持有成本，而 Hardware_Failure_Cost 中的备件替换是变动成本。更严重的是，父节点公式仅包含运行时的直接人力/停机成本，未包含 CapEx 摊销或库存资金成本，导致子节点3引入了父节点公式中不存在的维度（CapEx），造成层级不一致。3. 完备性虽基本覆盖，但父节点定义的是 Total_Ops_Cost（通常指 OpEx），而子节点3是 CapEx，分类不纯。）

## Search Query

Operational cost correction failure rate MTTR patch validation hours
