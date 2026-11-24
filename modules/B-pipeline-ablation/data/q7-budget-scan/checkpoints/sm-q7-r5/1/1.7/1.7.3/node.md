# N60: NVMe SSD 在 Random Read 状态下的典型功耗（W/drive），基于 7.68TB 企业级 PCIe Gen4 SSD 规格书，典型值约为 1

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

NVMe SSD 在 Random Read 状态下的典型功耗（W/drive），基于 7.68TB 企业级 PCIe Gen4 SSD 规格书，典型值约为 18-22W。

## Corrected Claim

NVMe SSD 在 Random Read 状态下的典型功耗（W/drive），基于 7.68TB 企业级 PCIe Gen4 SSD 规格书，典型值约为 18-22W。

## Evidence

父节点级核验未通过：不完备（子节点之间存在轻微的概念重叠（子节点1解释功耗构成，子节点2解释QD对总功耗的影响，两者均涉及功耗数值），但角度不同（静态结构 vs 动态负载），可视为正交。主要问题在于完备性不足：父节点仅要求给出‘典型功耗’，而子节点2引入了‘数据湖扫描场景’和‘驱动层优化’等父节点未提及的具体应用场景假设，且该场景下的功耗（16-18W）低于父节点定义的典型范围（18-22W），导致逻辑上未能完全支撑父节点的结论，反而引入了新的变量（QD和工作负载类型）使得分解偏离了‘基于规格书的典型值’这一核心约束。）

## Search Query

enterprise nvme ssd 7.68tb random read power consumption watts
