# N136: 回源服务器处理延迟（Origin Processing Time）：对于未命中缓存的请求，源站需从存储读取数据。若源站使用 NVMe SSD，读取 500KB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31, N32, N33

## Claim

回源服务器处理延迟（Origin Processing Time）：对于未命中缓存的请求，源站需从存储读取数据。若源站使用 NVMe SSD，读取 500KB 对象耗时 <1ms；但源站 CPU 负载高时（如视频转码或复杂鉴权），P99 处理时间可能飙升至 50-200ms。此为长尾 P99 300-500ms 的主要波动源。

## Corrected Claim

回源服务器处理延迟（Origin Processing Time）：对于未命中缓存的请求，源站需从存储读取数据。若源站使用 NVMe SSD，读取 500KB 对象耗时 <1ms；但源站 CPU 负载高时（如视频转码或复杂鉴权），P99 处理时间可能飙升至 50-200ms。此为长尾 P99 300-500ms 的主要波动源。

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD随机读取延迟通常在微秒级，500KB顺序读取<1ms符合物理极限；CPU密集型任务（转码/鉴权）导致P99飙升至50-200ms符合系统性能常识，且该延迟叠加网络开销后构成300-500ms长尾的主要来源，逻辑自洽。
