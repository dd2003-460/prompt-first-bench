# N292: 存储硬件成本细化 Cost_SSD_Storage = N_ssd * P_ssd_unit，假设单节点配置4条 2TB NVMe SSD (RAID 10或J

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

存储硬件成本细化 Cost_SSD_Storage = N_ssd * P_ssd_unit，假设单节点配置4条 2TB NVMe SSD (RAID 10或JBOD)，N_ssd=4，P_ssd_unit (2TB Enterprise NVMe) ≈ ¥2,500-¥3,500/条，则 Cost_SSD_Storage ≈ ¥10,000-¥14,000。

## Corrected Claim

存储硬件成本细化 Cost_SSD_Storage = N_ssd * P_ssd_unit，假设单节点配置4条 2TB NVMe SSD (RAID 10或JBOD)，N_ssd=4，P_ssd_unit (2TB Enterprise NVMe) ≈ ¥2,500-¥3,500/条，则 Cost_SSD_Storage ≈ ¥10,000-¥14,000。

## Evidence

先验知识/题面给定，逻辑校验通过：4条 * (2500-3500元) = 10000-14000元，计算无误且符合企业级NVMe SSD市场量级。

## Search Query

2TB NVMe SSD enterprise price Samsung Intel China
