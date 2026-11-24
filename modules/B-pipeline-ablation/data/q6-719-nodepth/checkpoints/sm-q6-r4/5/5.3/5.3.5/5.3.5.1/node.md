# N302: 自建单 POP 有效缓存容量 C_cap_pop = N_servers * Disk_Capacity * Utilization_Rate，其中 Disk_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

自建单 POP 有效缓存容量 C_cap_pop = N_servers * Disk_Capacity * Utilization_Rate，其中 Disk_Capacity 为单服务器可用 NVMe 存储（通常 2-4TB），Utilization_Rate 为缓存利用率（80%-90%）；10 个 POP 总有效缓存容量 C_cap_total = 10 * C_cap_pop。

## Corrected Claim

自建单 POP 有效缓存容量 C_cap_pop = N_servers * Disk_Capacity * Utilization_Rate，其中 Disk_Capacity 为单服务器可用 NVMe 存储（通常 2-4TB），Utilization_Rate 为缓存利用率（80%-90%）；10 个 POP 总有效缓存容量 C_cap_total = 10 * C_cap_pop。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合线性叠加原理，NVMe单盘容量2-4TB及80-90%利用率属于当前数据中心常见工程参数，量级合理且无内部矛盾。
