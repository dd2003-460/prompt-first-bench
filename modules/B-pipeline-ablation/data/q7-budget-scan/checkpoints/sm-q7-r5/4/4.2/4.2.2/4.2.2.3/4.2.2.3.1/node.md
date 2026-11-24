# N452: 12TB SMR HDD (如 Seagate IronWolf Pro 12TB) 在 RAID6 重建期间的有效持续顺序写带宽为 95-110 MB/s/盘

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N201

## Claim

12TB SMR HDD (如 Seagate IronWolf Pro 12TB) 在 RAID6 重建期间的有效持续顺序写带宽为 95-110 MB/s/盘，显著低于 CMR 盘的 150-200 MB/s，这是由于 SMR 的 Zone 顺序写入约束导致随机读干扰下的写放大效应 [待核验]，需通过具体型号 datasheet 确认。

## Corrected Claim

12TB SMR HDD (如 Seagate IronWolf Pro 12TB) 在 RAID6 重建期间的有效持续顺序写带宽通常低于同容量 CMR 盘，具体数值受固件策略和负载模式影响较大，需查阅具体型号实测数据或厂商技术白皮书确认。

## Evidence

[质询]数值缺乏具体型号数据支撑，且将SMR性能瓶颈完全归因于'随机读干扰下的写放大'可能存在机制简化，实际RAID6重建中SMR的主要瓶颈往往源于Zone管理开销及固件策略导致的吞吐波动，而非单纯的随机读干扰。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值区间及归因准确性）

## Search Query

Seagate IronWolf Pro 12TB SMR RAID rebuild effective write bandwidth MB/s
