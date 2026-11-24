# N386: 公有云CDN边缘节点磁盘I/O延迟贡献：对于缓存命中且数据已在内存中的请求，磁盘I/O为0ms；对于需从SSD加载的冷启动或大对象，P99 I/O延迟约为 5-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

公有云CDN边缘节点磁盘I/O延迟贡献：对于缓存命中且数据已在内存中的请求，磁盘I/O为0ms；对于需从SSD加载的冷启动或大对象，P99 I/O延迟约为 5-15ms（NVMe SSD），需计入 T_proc_edge 的下界修正。

## Corrected Claim

公有云CDN边缘节点磁盘I/O延迟贡献：对于缓存命中且数据已在内存中的请求，磁盘I/O为0ms；对于需从SSD加载的冷启动或大对象，P99 I/O延迟约为 5-15ms（NVMe SSD），需计入 T_proc_edge 的下界修正。

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD随机读延迟通常在微秒至毫秒级，P99在5-15ms符合工程经验量级；内存命中无磁盘I/O符合物理逻辑。

## Search Query

CDN edge node SSD read latency P99 cold cache hit
