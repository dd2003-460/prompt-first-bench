# N621: Loki 查询 50MB 日志的耗时分解：I/O 读取时间 T_io = Data_Size / Bandwidth = 50MB / 500MB/s (SSD

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N221

## Claim

Loki 查询 50MB 日志的耗时分解：I/O 读取时间 T_io = Data_Size / Bandwidth = 50MB / 500MB/s (SSD随机读) = 0.1s；解析与过滤时间 T_parse ≈ 0.2-0.5s (基于 LogQL 复杂度)，网络传输 T_net = 50MB / 125MB/s (1GbE有效吞吐) = 0.4s，总自动化耗时 < 1s

## Corrected Claim

Loki 查询 50MB 日志的耗时分解：I/O 读取时间 T_io = Data_Size / Bandwidth = 50MB / 500MB/s (SSD随机读) = 0.1s；解析与过滤时间 T_parse ≈ 0.2-0.5s (基于 LogQL 复杂度)，网络传输 T_net = 50MB / 125MB/s (1GbE有效吞吐) = 0.4s，总自动化耗时 < 1s

## Evidence

先验知识/题面给定，逻辑校验通过：I/O计算(50/500=0.1s)、网络计算(50/125=0.4s)及解析时间估算符合常规系统性能量级，总和<1s逻辑自洽。
