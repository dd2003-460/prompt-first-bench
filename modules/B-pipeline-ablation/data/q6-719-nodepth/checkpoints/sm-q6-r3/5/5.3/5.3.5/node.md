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

父节点级核验未通过：非正交, 不完备（1. 正交性差：子节点5、6、7、8均围绕请求率系数 K(t) 展开，其中5（基线）和8（峰值识别）高度重叠，且6（事件）和7（噪声）本质上是对 K(t) 不同组成部分的统计描述，逻辑上应合并为“请求率模型 K(t) 的构建与统计特性”。2. 完备性不足：父节点公式明确包含 L_processing（处理延迟），但子节点仅定义了边缘侧的 L_edge_self（含读取和排队），未单独定义或说明中心/边缘的计算处理延迟 L_processing 的具体构成及约束，导致公式右侧变量在子节点中无对应分解。）
