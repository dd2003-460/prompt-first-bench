# N419: 数据湖扫描场景的实际有效 QD 分布：FIO 测试显示，在 4K 随机读模式下，Linux 内核默认 io_uring 提交批处理大小为 16-32，因此实际稳

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

数据湖扫描场景的实际有效 QD 分布：FIO 测试显示，在 4K 随机读模式下，Linux 内核默认 io_uring 提交批处理大小为 16-32，因此实际稳态 QD 集中在 24±8 区间，对应功耗稳定在 16.5-17.5W，而非峰值 22W

## Corrected Claim

在特定 FIO 测试配置下，4K 随机读模式的实际稳态 QD 可能集中在 24±8 区间，对应功耗约 16.5-17.5W，但这取决于具体的 io_uring 参数设置及硬件特性，并非 Linux 内核默认的通用固定值。

## Evidence

[质询]将特定硬件/驱动配置下的 FIO 测试结果泛化为 Linux 内核默认行为缺乏普适性，且 'io_uring 提交批处理大小' 与 '稳态 QD' 之间的映射关系受具体存储设备队列深度限制及调度策略影响，并非固定常数。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值组合无法从第一性原理严格推导，属于特定实验观测值）

## Search Query

Linux io_uring default batch size NVMe random read effective queue depth data lake scan
