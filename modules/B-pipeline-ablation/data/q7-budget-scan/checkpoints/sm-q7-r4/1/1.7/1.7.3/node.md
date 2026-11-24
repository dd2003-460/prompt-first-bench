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

父节点级核验未通过：不完备（子节点1侧重于功耗的内部物理构成（静态/动态占比），子节点2侧重于外部负载条件（队列深度）对总功耗的影响，两者维度不同，具有正交性。但存在两个主要问题：1. 数值矛盾：子节点2指出QD=1时功耗为12-15W，这与父节点定义的“典型值18-22W”（通常指标准测试如FIO randread QD32+的场景）存在显著偏差，未明确区分“空闲/低负载”与“典型/满载”状态，导致逻辑上的不一致。2. 完备性缺失：父节点仅关注Random Read，但实际SSD功耗模型中，Write操作（涉及擦除和编程）的功耗远高于Read，且Idle（空闲）状态的功耗也是数据中心计算的关键部分，当前分解未涵盖这些关键状态，导致无法用于全面的功耗建模。）

## Search Query

enterprise nvme ssd 7.68tb random read power consumption watts
