# N173: RTX 4090 单卡配置下，系统总功耗 P_total 的计算公式为 P_total = P_gpu(450W) + P_cpu(65W) + P_platf

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

RTX 4090 单卡配置下，系统总功耗 P_total 的计算公式为 P_total = P_gpu(450W) + P_cpu(65W) + P_platform(30W) = 545W；应用 1.5 倍冗余系数后，电源额定功率下限为 817.5W，需向上取整至标准规格 850W。

## Corrected Claim

RTX 4090 单卡配置下，系统总功耗 P_total 的计算公式为 P_total = P_gpu(450W) + P_cpu(65W) + P_platform(30W) = 545W；应用 1.5 倍冗余系数后，电源额定功率下限为 817.5W，需向上取整至标准规格 850W。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W、CPU 65W、平台 30W 符合典型高配工作站功耗量级；545W * 1.5 = 817.5W，向上取整至 850W 符合电源选型工程惯例。
