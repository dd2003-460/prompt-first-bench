# N179: H100 SXM 四卡配置下，节点总功耗 P_total 的计算公式为 P_total = 4*P_gpu(700W) + P_cpu(2*150W) + P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

H100 SXM 四卡配置下，节点总功耗 P_total 的计算公式为 P_total = 4*P_gpu(700W) + P_cpu(2*150W) + P_platform(300W) = 3400W；应用 1.3 倍冗余系数后，电源/供电模块额定功率下限为 4420W，标准 HGX 8-GPU 节点电源配置通常为 4x 2000W 或 6x 2000W 冗余模块。

## Corrected Claim

H100 SXM 四卡配置下，节点总功耗 P_total 的计算公式为 P_total = 4*P_gpu(700W) + P_cpu(2*150W) + P_platform(300W) = 3400W；应用 1.3 倍冗余系数后，电源/供电模块额定功率下限为 4420W，标准 HGX 8-GPU 节点电源配置通常为 4x 2000W 或 6x 2000W 冗余模块。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP 700W，4卡功耗2800W，加上CPU及平台功耗约600W，总功耗3400W符合工程常识；1.3倍冗余系数计算正确（3400*1.3=4420W）；HGX 8-GPU节点通常配置4x 2000W或6x 2000W电源模块以提供冗余，符合NVIDIA HGX参考设计标准。
