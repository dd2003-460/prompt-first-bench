# N99: 全自建策略 P99 延迟 L_p99_self = L_edge_self + L_backhaul_self * (1 - H_self) + L_proce

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

全自建策略 P99 延迟 L_p99_self = L_edge_self + L_backhaul_self * (1 - H_self) + L_processing，其中 L_edge_self ≈ 5-10ms，H_self 为自建节点缓存命中率（受容量限制，通常 70-85%），需验证 L_p99_self ≤ 200ms。

## Corrected Claim

全自建策略 P99 延迟 L_p99_self = L_edge_self + L_backhaul_self * (1 - H_self) + L_processing，其中 L_edge_self ≈ 5-10ms，H_self 为自建节点缓存命中率（受容量限制，通常 70-85%），需验证 L_p99_self ≤ 200ms。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性/冗余问题：子节点5 (K_base) 和 子节点8 (K_base峰值) 高度重叠，子节点8本质上是子节点5的一个派生统计指标，应合并。2. 完整性缺失：父节点公式中的 L_processing 未在任何子节点中明确定义或分解（子节点3仅定义了源站处理，子节点4仅定义了边缘读取，缺少通用的计算/处理延迟项）。3. 逻辑断层：子节点7提到蒙特卡洛模拟，但未说明输入参数（如L_mean, sigma_L）如何从其他子节点（如负载模型、延迟模型）推导得出，导致分解链条断裂。）
