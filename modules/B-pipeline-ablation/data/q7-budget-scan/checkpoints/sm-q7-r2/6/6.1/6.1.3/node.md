# N80: 容量扩展边际成本：本地方案扩容需购买新磁盘/节点，存在最小购买单元（如整节点或整盘组）导致的阶梯成本；云方案扩容成本线性增加，无最小单元限制。本地方案第 t 年

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

容量扩展边际成本：本地方案扩容需购买新磁盘/节点，存在最小购买单元（如整节点或整盘组）导致的阶梯成本；云方案扩容成本线性增加，无最小单元限制。本地方案第 t 年新增成本 = (Data_Size(t) - Data_Size(t-1)) / R_raid × Unit_Price_per_TB + Node_Overhead（若需新节点）。

## Corrected Claim

容量扩展边际成本：本地方案扩容需购买新磁盘/节点，存在最小购买单元（如整节点或整盘组）导致的阶梯成本；云方案扩容成本线性增加，无最小单元限制。本地方案第 t 年新增成本 = (Data_Size(t) - Data_Size(t-1)) / R_raid × Unit_Price_per_TB + Node_Overhead（若需新节点）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

local storage expansion marginal cost vs cloud linear scaling
