# N59: NVMe SSD 在 Idle 状态下的典型功耗（W/drive），基于 7.68TB 企业级 PCIe Gen4 SSD 规格书，典型值约为 5-6W。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

NVMe SSD 在 Idle 状态下的典型功耗（W/drive），基于 7.68TB 企业级 PCIe Gen4 SSD 规格书，典型值约为 5-6W。

## Corrected Claim

NVMe SSD 在 Idle 状态下的典型功耗（W/drive），基于 7.68TB 企业级 PCIe Gen4 SSD 规格书，典型值约为 5-6W。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点1直接反驳了父节点给定的数值范围（2.5-3.5W vs 5-6W），导致逻辑矛盾；子节点2讨论的是动态唤醒和平均功耗修正，偏离了父节点关于‘Idle状态下典型瞬时功耗’的核心定义，且引入了未经验证的工程假设。）

## Search Query

enterprise nvme ssd 7.68tb idle power consumption watts
