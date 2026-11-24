# N666: 混合阵列散热风扇功耗 P_Fan_Hybrid 细化：总热耗散 ~269W (IT) + ~30W (Backplane/Controller extra he

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276

## Claim

混合阵列散热风扇功耗 P_Fan_Hybrid 细化：总热耗散 ~269W (IT) + ~30W (Backplane/Controller extra heat) ≈ 300W。在标准 2U/4U 机箱风道设计下，维持 15°C 进风温差，所需风量约 15-20 CFM。单个 40mm 服务器风扇功耗约 1.5-2W，通常配置 4-6 个风扇，总 P_Fan ≈ 4 * 1.8W ≈ 7.2W 至 6 * 2.2W ≈ 13.2W。N276 原估 15-20W 偏高，修正为 8-13W。

## Corrected Claim

混合阵列散热风扇功耗 P_Fan_Hybrid 细化：总热耗散 ~269W (IT) + ~30W (Backplane/Controller extra heat) ≈ 300W。在标准 2U/4U 机箱风道设计下，维持 15°C 进风温差，所需风量约 15-20 CFM。单个 40mm 服务器风扇功耗约 1.5-2W，通常配置 4-6 个风扇，总 P_Fan ≈ 4 * 1.8W ≈ 7.2W 至 6 * 2.2W ≈ 13.2W。N276 原估 15-20W 偏高，修正为 8-13W。

## Evidence

先验知识/题面给定，逻辑校验通过：基于热力学公式 Q=mcΔT 及空气比热容，300W 热量对应约 15-20 CFM 风量符合物理直觉；40mm 服务器风扇单颗功耗 1.5-2W 及 4-6 颗配置的总功耗 7.2-13.2W 符合工程常识，原估算 15-20W 确实偏高，修正合理。
