# N217: gVisor 内存隔离开销修正：50MB/实例仅为静态 RSS 基线，动态开销随代码执行复杂度增加；对于运行 Python 数值计算脚本（如 NumPy/Pan

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63, N64, N65

## Claim

gVisor 内存隔离开销修正：50MB/实例仅为静态 RSS 基线，动态开销随代码执行复杂度增加；对于运行 Python 数值计算脚本（如 NumPy/Pandas），峰值内存占用通常为基线的 3-5 倍（150-250MB），需设置 cgroup memory.limit 为 256MB 以防止 OOM 杀死宿主进程。

## Corrected Claim

gVisor 内存隔离开销中，50MB/实例仅为静态 RSS 基线，动态开销随代码执行复杂度增加；对于运行 Python 数值计算脚本（如 NumPy/Pandas），峰值内存占用通常显著高于基线（视数据规模而定，可能达到数百 MB），建议根据实际负载监控设置 cgroup memory.limit 以防止 OOM。

## Evidence

[质询]数值量级与具体倍数缺乏普适性：Python 数值计算脚本（NumPy/Pandas）的内存占用高度依赖于数据规模和处理逻辑，'3-5倍'及'150-250MB'仅为特定小规模场景的经验估算，并非固定属性；此外，gVisor 的内存开销主要源于用户态内核模拟，其动态增长与宿主进程 RSS 基线的比例关系受多种因素影响，断言固定的倍数范围过于绝对。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，无外部检索结果，且具体数值倍数属于依赖负载的经验参数，非第一性原理可推导，故降级）
