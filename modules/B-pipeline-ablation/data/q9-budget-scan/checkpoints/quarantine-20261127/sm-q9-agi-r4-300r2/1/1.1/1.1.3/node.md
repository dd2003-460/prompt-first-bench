# N36: V100-SXM2 的 NVLink 3.0 双向聚合带宽为 300 GB/s，但在 TP=4 环形 AllReduce 算法中，有效单向带宽利用率通常仅为理论

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

V100-SXM2 的 NVLink 3.0 双向聚合带宽为 300 GB/s，但在 TP=4 环形 AllReduce 算法中，有效单向带宽利用率通常仅为理论值的 60-70%（约 180-210 GB/s），受限于 PCIe/NVLink 拓扑路由开销。

## Corrected Claim

V100-SXM2 的 NVLink 3.0 双向聚合带宽为 300 GB/s，在 TP=4 环形 AllReduce 算法中，受限于网络拓扑和通信协议开销，有效单向带宽利用率通常低于理论峰值，具体数值取决于集群配置和软件栈优化。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性违背：父节点核心论点包含‘60-70%利用率’及‘拓扑路由开销’，但子节点1仅描述物理带宽构成（且存在计算逻辑混乱），子节点2仅描述数据量公式。两个子节点均未解释为何利用率低（即未覆盖‘拓扑路由开销’这一关键因果机制），且子节点1对带宽的计算方式（150*2）表述不清，容易与AllReduce的有效带宽概念混淆，导致概念重叠而非正交分解。2. 完备性缺失：父节点明确指出的‘有效单向带宽利用率受限’这一核心性能瓶颈原因（拓扑路由开销）在子节点中完全缺失。子节点只提供了静态参数（物理带宽、数据量公式），未涵盖动态行为（算法效率损失）。）

## Search Query

NVLink 3.0 effective bandwidth utilization AllReduce ring algorithm
