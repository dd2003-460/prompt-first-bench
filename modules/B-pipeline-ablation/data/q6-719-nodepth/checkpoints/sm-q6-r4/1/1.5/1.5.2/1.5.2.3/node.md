# N188: 存储 I/O 延迟 T_storage_io 的并发影响：源站 SSD 随机读 IOPS 通常为 50k-100k；若并发回源请求 QPS 为 1k，则平均 I

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

存储 I/O 延迟 T_storage_io 的并发影响：源站 SSD 随机读 IOPS 通常为 50k-100k；若并发回源请求 QPS 为 1k，则平均 I/O 等待时间 = QPS / IOPS = 1000 / 50000 = 20ms；若 QPS 升至 5k，等待时间升至 100ms，显著影响 P99 延迟，需引入队列论（M/M/1）修正 T_storage_io = 1 / (Service_Rate - Arrival_Rate)。

## Corrected Claim

存储 I/O 延迟 T_storage_io 的并发影响：源站 SSD 随机读 IOPS 通常为 50k-100k；若并发回源请求 QPS 为 1k，则平均 I/O 等待时间 = QPS / IOPS = 1000 / 50000 = 20ms；若 QPS 升至 5k，等待时间升至 100ms，显著影响 P99 延迟，需引入队列论（M/M/1）修正 T_storage_io = 1 / (Service_Rate - Arrival_Rate)。

## Evidence

父节点级核验未通过：不完备（子节点分别描述了低负载和高负载两种极端场景，内容不重复且无矛盾（正交性合格）。但是，父节点中明确提到的核心计算逻辑“QPS=1k时等待20ms”和“QPS=5k时等待100ms”这两个中间负载状态在子节点中完全缺失，导致对父节点关键数值范围的覆盖不完整。此外，两个子节点本质上是同一M/M/1模型在不同利用率参数下的实例化，虽然作为不同工作点（低/高）可以接受，但缺乏对中间典型工况的覆盖使得分解在工程指导意义上不完备。）
