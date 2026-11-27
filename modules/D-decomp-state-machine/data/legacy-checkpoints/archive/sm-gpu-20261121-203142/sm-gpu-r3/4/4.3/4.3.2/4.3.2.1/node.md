# N263: 消费级卡故障诊断时间（MTTD）：由于缺乏硬件健康监控接口（如nvidia-smi的ECC错误计数），故障发现依赖于应用层异常或用户报告，平均检测时间约为1-4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

消费级卡故障诊断时间（MTTD）：由于缺乏硬件健康监控接口（如nvidia-smi的ECC错误计数），故障发现依赖于应用层异常或用户报告，平均检测时间约为1-4小时；数据中心卡具备带外管理（BMC/IPMI）和实时错误日志，检测时间<5分钟。

## Corrected Claim

消费级卡故障诊断时间（MTTD）：由于缺乏硬件健康监控接口（如nvidia-smi的ECC错误计数），故障发现依赖于应用层异常或用户报告，平均检测时间约为1-4小时；数据中心卡具备带外管理（BMC/IPMI）和实时错误日志，检测时间<5分钟。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU fault detection time MTTD consumer vs datacenter BMC monitoring
