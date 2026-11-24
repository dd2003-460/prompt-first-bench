# N118: 云存储扫描隐性成本 C_idle_cloud：若集群在云存储扫描期间空闲，且T_net=111小时，SLA=2小时，则 C_idle_cloud_daily =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

云存储扫描隐性成本 C_idle_cloud：若集群在云存储扫描期间空闲，且T_net=111小时，SLA=2小时，则 C_idle_cloud_daily = (111 - 2) * 2 * 5000 = ¥1,090,000/天；表明对于大文件顺序扫描，云存储的网络延迟惩罚可能高于本地HDD，除非采用预取或本地缓存策略。

## Corrected Claim

云存储扫描隐性成本 C_idle_cloud：若集群在云存储扫描期间空闲，且T_net=111小时，SLA=2小时，则 C_idle_cloud_daily = (111 - 2) * 2 * 5000 = ¥1,090,000/天；表明对于大文件顺序扫描，云存储的网络延迟惩罚可能高于本地HDD，除非采用预取或本地缓存策略。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (111-2)*2*5000=1,090,000 正确，且符合云存储高延迟导致空闲等待成本高的工程常识。
