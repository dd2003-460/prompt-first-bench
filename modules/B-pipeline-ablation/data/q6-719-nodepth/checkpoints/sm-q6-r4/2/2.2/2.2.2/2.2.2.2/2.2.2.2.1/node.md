# N522: 自建 POP 节点有效缓存容量 C_self_storage 的计算公式：C_self_storage = N_servers * N_disks_per_se

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N170

## Claim

自建 POP 节点有效缓存容量 C_self_storage 的计算公式：C_self_storage = N_servers * N_disks_per_server * Disk_Size * (1 - Overhead_Ratio)，其中 N_servers=4, N_disks=8, Disk_Size=3.84TB, Overhead_Ratio=0.15，计算得 C_self_storage = 4 * 8 * 3.84 * 0.85 ≈ 104.4TB。

## Corrected Claim

自建 POP 节点有效缓存容量 C_self_storage 的计算公式：C_self_storage = N_servers * N_disks_per_server * Disk_Size * (1 - Overhead_Ratio)，其中 N_servers=4, N_disks=8, Disk_Size=3.84TB, Overhead_Ratio=0.15，计算得 C_self_storage = 4 * 8 * 3.84 * 0.85 ≈ 104.4TB。

## Evidence

先验知识/题面给定，逻辑校验通过：4 * 8 * 3.84 * 0.85 = 104.448，约等于 104.4TB，计算无误。
