# N68: 本地推理边际成本 C_local(L) = (P_server_load * E_price * L / (T_throughput * 3600)) + C_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

本地推理边际成本 C_local(L) = (P_server_load * E_price * L / (T_throughput * 3600)) + C_fixed_depreciation，其中 P_server_load ≈ 300W (4xV100 idle+load), E_price = $0.15/kWh, T_throughput = 60 tok/s

## Corrected Claim

本地推理边际成本 C_local(L) = (P_server_load * E_price * L / (T_throughput * 3600)) + C_fixed_depreciation，其中 P_server_load ≈ 300W (4xV100 idle+load), E_price = $0.15/kWh, T_throughput = 60 tok/s

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 冗余性严重：两个子节点本质上是同一公式在不同参数（功率P、吞吐量T）下的特例，属于连续变量空间的离散采样，而非结构性分解。它们共享相同的逻辑结构，仅数值不同，应合并为一个带参数范围的描述或作为示例而非独立子节点。2. 非正交：子节点描述的是同一物理过程的不同工作点，存在概念上的重叠（都是计算边际成本），未体现不同维度的独立贡献。3. 不完备：父节点包含 'C_fixed_depreciation'（固定折旧），但子节点仅将其作为常数占位符 'C_fixed'，未分解其构成（如硬件寿命、资金成本等），也未解释为何在低负载下固定成本分摊逻辑可能变化（例如，若设备闲置，折旧是否仍计入该次推理的边际成本？）。此外，缺少对 'L'（长度）如何影响非线性因素（如内存带宽瓶颈导致P或T变化）的讨论。）
