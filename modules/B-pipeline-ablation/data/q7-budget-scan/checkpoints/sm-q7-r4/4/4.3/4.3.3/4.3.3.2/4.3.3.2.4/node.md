# N735: 白天50%限速下的I/O资源竞争量化：白天业务I/O负载峰值为100MB/s，存储总吞吐能力为500MB/s。若重建任务占用50%带宽（250MB/s），剩余2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256, N257, N258

## Claim

白天50%限速下的I/O资源竞争量化：白天业务I/O负载峰值为100MB/s，存储总吞吐能力为500MB/s。若重建任务占用50%带宽（250MB/s），剩余250MB/s分配给业务。需验证业务SLA要求（如P99延迟<50ms）在此剩余带宽下是否仍能满足，若不能满足，则白天限速需进一步降低至30%或以下。

## Corrected Claim

白天50%限速下的I/O资源竞争量化：白天业务I/O负载峰值为100MB/s，存储总吞吐能力为500MB/s。若重建任务占用50%带宽（250MB/s），剩余250MB/s分配给业务。需验证业务SLA要求（如P99延迟<50ms）在此剩余带宽下是否仍能满足，若不能满足，则白天限速需进一步降低至30%或以下。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（500*50%=250, 500-250=250），且250MB/s > 100MB/s峰值负载，带宽充足，逻辑自洽。

## Search Query

storage I/O QoS bandwidth allocation business latency impact background rebuild
