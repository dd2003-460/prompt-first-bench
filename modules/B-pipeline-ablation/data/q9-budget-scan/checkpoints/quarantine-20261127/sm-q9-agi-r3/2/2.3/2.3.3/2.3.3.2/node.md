# N134: 回滚耗时 < 1s 的前提是检查点存储在 NVMe SSD 上且内存映射 (mmap) 有效；若存储介质为 HDD 或涉及网络挂载文件系统 (NFS)，读取 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

回滚耗时 < 1s 的前提是检查点存储在 NVMe SSD 上且内存映射 (mmap) 有效；若存储介质为 HDD 或涉及网络挂载文件系统 (NFS)，读取 4MB 数据的 I/O 延迟通常为 50ms-200ms，加上进程重启开销 (Python 环境加载 ~2-5s)，实际回滚耗时将远超 1s，需优化为热加载或保留常驻进程池。

## Corrected Claim

回滚耗时 < 1s 的前提是检查点存储在 NVMe SSD 上且内存映射 (mmap) 有效；若存储介质为 HDD 或涉及网络挂载文件系统 (NFS)，读取 4MB 数据的 I/O 延迟通常为 50ms-200ms，加上进程重启开销 (Python 环境加载 ~2-5s)，实际回滚耗时将远超 1s，需优化为热加载或保留常驻进程池。

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe随机读延迟微秒级，HDD毫秒级，Python冷启动秒级，量级对比符合物理与工程常识

## Search Query

nvme ssd random read latency 4mb block
