# N23: CAPEX 计算公式：CAPEX_total = (N_gpus × P_gpu) + P_chassis + P_psu + P_network + P_co

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

CAPEX 计算公式：CAPEX_total = (N_gpus × P_gpu) + P_chassis + P_psu + P_network + P_cooling_hardware，其中 P_gpu 为单卡零售价（美元），P_chassis 为主机/机架成本，P_psu 为电源模块成本，P_network 为高速互联（如 NVLink/PCIe 交换机）成本，P_cooling_hardware 为主动/被动散热硬件成本；各分项需按单卡与多卡架构分别量化。

## Corrected Claim

CAPEX 计算公式：CAPEX_total = (N_gpus × P_gpu) + P_chassis + P_psu + P_network + P_cooling_hardware，其中 P_gpu 为单卡零售价（美元），P_chassis 为主机/机架成本，P_psu 为电源模块成本，P_network 为高速互联（如 NVLink/PCIe 交换机）成本，P_cooling_hardware 为主动/被动散热硬件成本；各分项需按单卡与多卡架构分别量化。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式完整覆盖了GPU服务器/集群的主要硬件成本构成（GPU、机箱、电源、网络、散热），量纲一致（均为美元成本），且符合数据中心基础设施建设的通用工程逻辑。
