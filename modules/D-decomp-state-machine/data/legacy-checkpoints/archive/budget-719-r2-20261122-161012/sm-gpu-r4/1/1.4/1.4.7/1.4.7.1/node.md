# N173: RTX 4090 单卡配置下，系统总功耗 P_total 的计算公式为 P_total = P_gpu(450W) + P_cpu(65W) + P_platf

- **status**: pending
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

父节点级核验未通过：不完备（子节点未覆盖父节点中关于'电源额定功率需向上取整至标准规格'这一关键逻辑步骤，仅提供了修正后的功率数值和结论，缺失了从计算值到标准规格映射的推导过程。）
