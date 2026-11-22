# N336: 硬件故障更换的实际停机时间分解：更换显卡的总停机时间 T_downtime = T_diagnosis (诊断) + T_replacement (物理更换) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

硬件故障更换的实际停机时间分解：更换显卡的总停机时间 T_downtime = T_diagnosis (诊断) + T_replacement (物理更换) + T_driver (驱动重装) + T_verify (模型加载与验证)；典型值为 T_diagnosis=1h, T_replacement=0.5h, T_driver=1h, T_verify=0.5h，总计 3 小时；N111 中 4-8 小时的估计偏高，主要因为未考虑预配置驱动镜像和自动化脚本的优化。

## Corrected Claim

硬件故障更换的实际停机时间分解：更换显卡的总停机时间 T_downtime = T_diagnosis (诊断) + T_replacement (物理更换) + T_driver (驱动重装) + T_verify (模型加载与验证)；典型值为 T_diagnosis=1h, T_replacement=0.5h, T_driver=1h, T_verify=0.5h，总计 3 小时；N111 中 4-8 小时的估计偏高，主要因为未考虑预配置驱动镜像和自动化脚本的优化。

## Evidence

先验知识/题面给定，逻辑校验通过
