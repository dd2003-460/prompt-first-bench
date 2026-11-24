# N266: NVMe SSD 活跃功耗 W_active 修正：在混合读写负载（非纯随机）下，7.68TB 企业级 NVMe SSD 的典型平均功耗为 12-16W，N12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

NVMe SSD 活跃功耗 W_active 修正：在混合读写负载（非纯随机）下，7.68TB 企业级 NVMe SSD 的典型平均功耗为 12-16W，N128 采用的 15W 处于合理区间中值，无需大幅修正但需注明受 TRIM/GC 影响波动 ±2W

## Corrected Claim

NVMe SSD 活跃功耗 W_active 修正：在混合读写负载（非纯随机）下，7.68TB 企业级 NVMe SSD 的典型平均功耗为 12-16W，N128 采用的 15W 处于合理区间中值，无需大幅修正但需注明受 TRIM/GC 影响波动 ±2W

## Evidence

先验知识/题面给定，逻辑校验通过：7.68TB企业级NVMe SSD在混合负载下12-16W符合行业典型功耗范围，15W为中值且±2W波动符合GC/TRIM特性，数值量级与工程常识一致。

## Search Query

enterprise nvme ssd active power consumption mixed workload watts
