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

父节点级核验未通过：不完备（子节点1关注内部组件功耗构成（空间/结构维度），子节点2关注队列深度对总功耗的影响（负载/动态维度），两者维度不同且无逻辑矛盾，具备正交性。但父节点明确限定为“Random Read”状态，而子节点2引入了“数据湖扫描场景”及“高并发批量读”，这通常对应Sequential Read或混合负载，偏离了父节点定义的纯Random Read工况，导致范围不完全匹配。此外，缺少对温度、写入占比等环境/历史因素对功耗影响的描述，完备性稍显不足。）

## Search Query

enterprise nvme ssd 7.68tb random read power consumption watts
