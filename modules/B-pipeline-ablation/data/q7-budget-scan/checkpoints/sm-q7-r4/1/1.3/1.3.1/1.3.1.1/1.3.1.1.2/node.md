# N450: T_rebuild=111小时的物理瓶颈分析：500TB/1.25GB/s=111h假设网络为唯一瓶颈。若使用本地NVMe恢复（10GB/s），T_rebuil

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151

## Claim

T_rebuild=111小时的物理瓶颈分析：500TB/1.25GB/s=111h假设网络为唯一瓶颈。若使用本地NVMe恢复（10GB/s），T_rebuild=500TB/10GB/s=13.9h。RTO成本对恢复通道的敏感性极高：网络恢复¥555,000/次 vs 本地恢复¥69,500/次。年化期望成本相应为¥27,750 vs ¥3,475（基于5%年故障率）。

## Corrected Claim

T_rebuild=111小时的物理瓶颈分析：500TB/1.25GB/s=111h假设网络为唯一瓶颈。若使用本地NVMe恢复（10GB/s），T_rebuild=500TB/10GB/s=13.9h。RTO成本对恢复通道的敏感性极高：网络恢复¥555,000/次 vs 本地恢复¥69,500/次。年化期望成本相应为¥27,750 vs ¥3,475（基于5%年故障率）。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB/1.25GB/s≈111h，500TB/10GB/s≈13.9h，成本计算（111*5000=555k, 13.9*5000=69.5k, 5%年化）均符合算术逻辑。
