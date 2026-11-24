# N23: 恢复吞吐约束（TB/小时）：NVMe SSD阵列恢复吞吐 ≈ 30TB/h（单节点10GbE瓶颈），HDD分层恢复吞吐 ≈ 5TB/h（HDD机械瓶颈），S3恢

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

恢复吞吐约束（TB/小时）：NVMe SSD阵列恢复吞吐 ≈ 30TB/h（单节点10GbE瓶颈），HDD分层恢复吞吐 ≈ 5TB/h（HDD机械瓶颈），S3恢复吞吐 ≈ 15TB/h（网络带宽+限流）[待核验：需实测或厂商SLA]

## Corrected Claim

恢复吞吐约束（TB/小时）：NVMe SSD阵列恢复吞吐通常在10-50TB/h范围（取决于节点数与网络带宽，单节点10GbE受限于~4.5TB/h），HDD分层恢复吞吐通常在1-10TB/h范围（受机械寻道限制），S3恢复吞吐通常在5-20TB/h范围（受网络带宽与API限流影响）[具体数值需根据实际硬件配置与网络环境实测]

## Evidence

[质询]数值量级存在显著不确定性：单节点10GbE理论上限约1.25GB/s（≈4.5TB/h），声称30TB/h需多节点聚合或更高带宽，若指单节点则违背物理极限；HDD 5TB/h和S3 15TB/h亦缺乏具体硬件配置支撑，易受IOPS、并发数及网络拓扑影响，属于高度依赖具体部署环境的经验值而非通用常数。 | 先验知识/题面给定，逻辑校验通过（量纲正确，量级在合理工程范围内，但具体数值依赖未明确的硬件配置），无外部来源支持，依据经验事实排除条款降级。

## Search Query

NVMe SSD restore throughput TB/h S3 restore speed limit
