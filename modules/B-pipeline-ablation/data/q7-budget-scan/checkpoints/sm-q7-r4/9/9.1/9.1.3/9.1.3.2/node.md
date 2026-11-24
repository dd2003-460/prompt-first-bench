# N665: 混合背板与供电损耗 P_Backplane_Power 细化：混合背板需同时支持 SATA/SAS（HDD）和 U.2/E1.S（NVMe）接口，供电模块转换效

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276

## Claim

混合背板与供电损耗 P_Backplane_Power 细化：混合背板需同时支持 SATA/SAS（HDD）和 U.2/E1.S（NVMe）接口，供电模块转换效率 η_PSU ≈ 0.90-0.92。若总 IT 负载 269W（含盘和控制器），背板及本地 DC-DC 转换损耗约为总负载的 8-10%，即 P_Backplane_Loss ≈ 269W * 0.09 ≈ 24W。加上背板本身电子元件功耗 ~6W，合计 ~30W，与 N276 原估一致。

## Corrected Claim

混合背板与供电损耗 P_Backplane_Power 细化：混合背板需同时支持 SATA/SAS（HDD）和 U.2/E1.S（NVMe）接口，供电模块转换效率 η_PSU ≈ 0.90-0.92。若总 IT 负载 269W（含盘和控制器），背板及本地 DC-DC 转换损耗约为总负载的 8-10%，即 P_Backplane_Loss ≈ 269W * 0.09 ≈ 24W。加上背板本身电子元件功耗 ~6W，合计 ~30W，与 N276 原估一致。

## Evidence

先验知识/题面给定，逻辑校验通过：PSU效率0.90-0.92符合主流服务器电源标准，背板及DC-DC损耗占比8-10%符合工程经验，计算过程269*0.09≈24W及加6W得30W算术正确，量级合理。
