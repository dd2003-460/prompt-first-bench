# N664: 混合阵列控制器功耗 P_Controller_Hybrid 细化：HBA/RAID 控制器需维护 HDD 和 SSD 两套队列和缓存策略，典型企业级双端口 HB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276

## Claim

混合阵列控制器功耗 P_Controller_Hybrid 细化：HBA/RAID 控制器需维护 HDD 和 SSD 两套队列和缓存策略，典型企业级双端口 HBA（支持 24 口 SAS/SATA + PCIe Gen4 x8 NVMe）在中等负载下功耗约为 35-45W。取中值 40W，较纯 HDD 控制器（~30W）高 33%，主要源于 NVMe 协议栈处理和更大 DRAM 缓存的静态功耗。

## Corrected Claim

混合阵列控制器功耗 P_Controller_Hybrid 细化：HBA/RAID 控制器需维护 HDD 和 SSD 两套队列和缓存策略，典型企业级双端口 HBA（支持 24 口 SAS/SATA + PCIe Gen4 x8 NVMe）在中等负载下功耗约为 35-45W。取中值 40W，较纯 HDD 控制器（~30W）高 33%，主要源于 NVMe 协议栈处理和更大 DRAM 缓存的静态功耗。

## Evidence

先验知识/题面给定，逻辑校验通过
