# N177: H100 SXM 单卡配置下，节点总功耗 P_total 的计算公式为 P_total = P_gpu(700W) + P_cpu(2*150W) + P_pl

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

H100 SXM 单卡配置下，节点总功耗 P_total 的计算公式为 P_total = P_gpu(700W) + P_cpu(2*150W) + P_platform(200W) = 1200W；应用 1.3 倍冗余系数后，电源/供电模块额定功率下限为 1560W，通常采用冗余双电源（2x 2000W）或服务器专用电源模块。

## Corrected Claim

H100 SXM 单卡配置下，节点总功耗 P_total 的计算公式为 P_total = P_gpu(700W) + P_cpu(2*150W) + P_platform(200W) = 1200W；应用 1.3 倍冗余系数后，电源/供电模块额定功率下限为 1560W，通常采用冗余双电源（2x 2000W）或服务器专用电源模块。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP为700W，双路CPU及平台功耗估算合理，1.3倍冗余系数计算正确（1200*1.3=1560W），符合数据中心服务器供电设计规范。
