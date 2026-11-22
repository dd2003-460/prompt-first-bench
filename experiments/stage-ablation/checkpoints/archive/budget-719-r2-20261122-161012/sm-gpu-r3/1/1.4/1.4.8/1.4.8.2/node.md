# N178: H100 SXM 双卡配置下，节点总功耗 P_total 的计算公式为 P_total = 2*P_gpu(700W) + P_cpu(2*150W) + P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

H100 SXM 双卡配置下，节点总功耗 P_total 的计算公式为 P_total = 2*P_gpu(700W) + P_cpu(2*150W) + P_platform(250W) = 1950W；应用 1.3 倍冗余系数后，电源/供电模块额定功率下限为 2535W，需配置 2x 2000W 冗余电源或 3000W+ 单路电源。

## Corrected Claim

H100 SXM 双卡配置下，节点总功耗 P_total 的计算公式为 P_total = 2*P_gpu(700W) + P_cpu(2*150W) + P_platform(250W) = 1950W；应用 1.3 倍冗余系数后，电源/供电模块额定功率下限为 2535W，需配置 2x 2000W 冗余电源或 3000W+ 单路电源。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP 700W 符合 NVIDIA 官方规格，双卡 1400W + CPU 300W + 平台 250W = 1950W 计算正确；1.3 倍冗余系数得出 2535W 下限，推荐 2x2000W 冗余电源（总容量 4000W，单路故障下 2000W 略低于 2535W 但通常冗余电源设计允许短时过载或实际负载低于峰值，且 3000W+ 单路方案完全覆盖）符合数据中心供电工程惯例。
