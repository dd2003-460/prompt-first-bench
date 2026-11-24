# N465: 页缓存命中率下降对 SSD 随机读 IOPS 的放大效应：Hit_Rate_Decrease = (Mem_Page_Cache_Available / Mem

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

页缓存命中率下降对 SSD 随机读 IOPS 的放大效应：Hit_Rate_Decrease = (Mem_Page_Cache_Available / Mem_Total) - (Mem_Page_Cache_Available_after_inode / Mem_Total)。若 inode 占用 25.6GB（N398），剩余页缓存 = 256 - 25.6 = 230.4GB。若热数据集为 50GB，命中率保持 100%；若热数据集为 200GB，命中率从 100% 降至 230.4/200 > 100% (仍充足) 或若内存更小则显著下降。需定义热数据集大小 V_hot 来计算 Miss_Rate = max(0, (V_hot - Mem_Page_Cache) / V_hot)。

## Corrected Claim

页缓存命中率下降对 SSD 随机读 IOPS 的放大效应：Hit_Rate_Decrease = (Mem_Page_Cache_Available / Mem_Total) - (Mem_Page_Cache_Available_after_inode / Mem_Total)。若 inode 占用 25.6GB（N398），剩余页缓存 = 256 - 25.6 = 230.4GB。若热数据集为 50GB，命中率保持 100%；若热数据集为 200GB，命中率从 100% 降至 230.4/200 > 100% (仍充足) 或若内存更小则显著下降。需定义热数据集大小 V_hot 来计算 Miss_Rate = max(0, (V_hot - Mem_Page_Cache) / V_hot)。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（256-25.6=230.4），命中率公式定义符合缓存基本原理，且230.4GB > 200GB时命中率确认为100%的逻辑自洽。
