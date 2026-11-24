# N11: 本地NVMe SSD阵列的CapEx构成：服务器硬件成本(含CPU/内存/网卡) + NVMe SSD采购成本(¥/TB×500TB) + RAID控制器/HB

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

本地NVMe SSD阵列的CapEx构成：服务器硬件成本(含CPU/内存/网卡) + NVMe SSD采购成本(¥/TB×500TB) + RAID控制器/HBA卡成本 + 机架空间与供电改造成本；典型企业级NVMe SSD价格区间为¥150-300/TB(2026年预估)，需结合具体型号和批量折扣计算

## Corrected Claim

本地NVMe SSD阵列的CapEx构成：服务器硬件成本(含CPU/内存/网卡) + NVMe SSD采购成本(¥/TB×500TB) + RAID控制器/HBA卡成本 + 机架空间与供电改造成本；典型企业级NVMe SSD价格区间为¥150-300/TB(2026年预估)，需结合具体型号和批量折扣计算

## Evidence

[质询]2026年NVMe SSD价格预测存在不确定性，且¥150-300/TB的价格区间可能随市场波动较大，但作为规划预估范围在逻辑上是合理的。 | 先验知识/题面给定，逻辑校验通过：CapEx构成项完整符合数据中心建设常识，NVMe SSD价格区间处于当前及未来预期的合理量级（企业级SSD通常高于消费级，但低于HDD+机械结构复杂度的存储方案，且随着技术成熟价格呈下降趋势，该区间符合2024-2026年的市场趋势预期）。
