# N311: 单POP点有效缓存容量 C_eff 的计算：C_eff = C_physical × U_cache，其中 C_physical = 2TB (N123)，U_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100, N101, N102

## Claim

单POP点有效缓存容量 C_eff 的计算：C_eff = C_physical × U_cache，其中 C_physical = 2TB (N123)，U_cache = 0.7 (文件系统/元数据开销)，故 C_eff = 1.4TB；此值替代 N100 中假设的 1TB 作为 CHR 计算分母

## Corrected Claim

单POP点有效缓存容量 C_eff 的计算：C_eff = C_physical × U_cache，其中 C_physical = 2TB (N123)，U_cache = 0.7 (文件系统/元数据开销)，故 C_eff = 1.4TB；此值替代 N100 中假设的 1TB 作为 CHR 计算分母

## Evidence

先验知识/题面给定，逻辑校验通过：2TB * 0.7 = 1.4TB，计算无误，且符合缓存有效容量扣除元数据开销的工程惯例。

## Search Query

NVMe SSD file system overhead metadata ratio 2TB
