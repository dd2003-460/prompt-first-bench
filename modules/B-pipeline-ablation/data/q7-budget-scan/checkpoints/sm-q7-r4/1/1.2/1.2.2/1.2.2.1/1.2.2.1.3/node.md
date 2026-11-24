# N453: EC(8+3) 重建期间业务性能退化阈值：若 CPU 占用率增量 > 10% 且磁盘 I/O 队列深度 > 50，则业务 IOPS 下降 > 20%，需通过 Q

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

EC(8+3) 重建期间业务性能退化阈值：若 CPU 占用率增量 > 10% 且磁盘 I/O 队列深度 > 50，则业务 IOPS 下降 > 20%，需通过 QoS 策略将重建带宽限制在 5% 以下或暂停重建直至业务低峰期

## Corrected Claim

EC(8+3) 重建期间业务性能退化阈值：若 CPU 占用率增量 > 10% 且磁盘 I/O 队列深度 > 50，则业务 IOPS 下降 > 20%，需通过 QoS 策略将重建带宽限制在 5% 以下或暂停重建直至业务低峰期

## Evidence

先验知识/题面给定，逻辑校验通过
