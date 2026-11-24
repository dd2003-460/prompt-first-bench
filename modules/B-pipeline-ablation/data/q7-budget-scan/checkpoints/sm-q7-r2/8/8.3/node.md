# N129: NVMe SSD 阵列基础设施开销 P_infra 的量化估算：通常控制器/背板功耗约为总盘数的 5-10%，散热风扇功耗与总发热量成正比（P_fan ≈ 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

NVMe SSD 阵列基础设施开销 P_infra 的量化估算：通常控制器/背板功耗约为总盘数的 5-10%，散热风扇功耗与总发热量成正比（P_fan ≈ 0.1 * P_total），PDU 转换效率 η≈0.95，故 P_infra ≈ (P_drives * 0.1) + (P_total * 0.1) + (P_total * 0.05)。

## Corrected Claim

NVMe SSD 阵列基础设施开销 P_infra 的量化估算：通常控制器/背板功耗约为总盘数的 5-10%，散热风扇功耗与总发热量成正比（P_fan ≈ 0.1 * P_total），PDU 转换效率 η≈0.95，故 P_infra ≈ (P_drives * 0.1) + (P_total * 0.1) + (P_total * 0.05)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

storage array controller backplane fan power consumption percentage of drive power
