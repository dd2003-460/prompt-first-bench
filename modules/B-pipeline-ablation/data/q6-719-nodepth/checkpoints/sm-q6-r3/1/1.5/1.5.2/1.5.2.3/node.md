# N188: 存储 I/O 延迟 T_storage_io 的并发影响：源站 SSD 随机读 IOPS 通常为 50k-100k；若并发回源请求 QPS 为 1k，则平均 I

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

存储 I/O 延迟 T_storage_io 的并发影响：源站 SSD 随机读 IOPS 通常为 50k-100k；若并发回源请求 QPS 为 1k，则平均 I/O 等待时间 = QPS / IOPS = 1000 / 50000 = 20ms；若 QPS 升至 5k，等待时间升至 100ms，显著影响 P99 延迟，需引入队列论（M/M/1）修正 T_storage_io = 1 / (Service_Rate - Arrival_Rate)。

## Corrected Claim

存储 I/O 延迟 T_storage_io 的并发影响：源站 SSD 随机读 IOPS 通常为 50k-100k；若并发回源请求 QPS 为 1k，则平均 I/O 等待时间 = QPS / IOPS = 1000 / 50000 = 20ms；若 QPS 升至 5k，等待时间升至 100ms，显著影响 P99 延迟，需引入队列论（M/M/1）修正 T_storage_io = 1 / (Service_Rate - Arrival_Rate)。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（1000/50000=0.02s=20ms），M/M/1队列论公式应用符合排队论基本原理，SSD IOPS量级符合工程常识。
