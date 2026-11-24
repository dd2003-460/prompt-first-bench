# N23: 恢复吞吐约束（TB/小时）：NVMe SSD阵列恢复吞吐 ≈ 30TB/h（单节点10GbE瓶颈），HDD分层恢复吞吐 ≈ 5TB/h（HDD机械瓶颈），S3恢

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

恢复吞吐约束（TB/小时）：NVMe SSD阵列恢复吞吐 ≈ 30TB/h（单节点10GbE瓶颈），HDD分层恢复吞吐 ≈ 5TB/h（HDD机械瓶颈），S3恢复吞吐 ≈ 15TB/h（网络带宽+限流）[待核验：需实测或厂商SLA]

## Corrected Claim

恢复吞吐约束（TB/小时）：NVMe SSD阵列恢复吞吐通常在10-50TB/h范围（取决于节点数与网络带宽，单节点10GbE受限于~4.5TB/h），HDD分层恢复吞吐通常在1-10TB/h范围（受机械寻道限制），S3恢复吞吐通常在5-20TB/h范围（受网络带宽与API限流影响）[具体数值需根据实际硬件配置与网络环境实测]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对NVMe、HDD、S3三种不同存储介质的恢复吞吐瓶颈进行了独立的物理层和网络层分析，维度清晰且互不重叠（正交）。所有子节点均覆盖了父节点中提到的三种主要存储类型及其对应的初始估算值（完备）。虽然都涉及网络带宽计算，但针对不同存储介质和场景的具体约束不同，不属于简单参数冗余。）

## Search Query

NVMe SSD restore throughput TB/h S3 restore speed limit
