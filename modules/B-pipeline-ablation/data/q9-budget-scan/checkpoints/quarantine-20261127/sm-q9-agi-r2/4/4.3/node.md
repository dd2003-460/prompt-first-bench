# N19: 代码执行沙箱资源隔离与超时控制：基于 Docker + cgroups 的 Python 沙箱，限制单任务 CPU 时间 T_cpu_max=300s，内存 M

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

代码执行沙箱资源隔离与超时控制：基于 Docker + cgroups 的 Python 沙箱，限制单任务 CPU 时间 T_cpu_max=300s，内存 Mem_max=4GB，磁盘 Disk_max=10GB；对于典型科研计算任务（如 PyTorch 训练小模型、统计回归），平均执行时间 T_exec≈15-60s，失败率（因 OOM 或死循环）P_fail≈5-10%；重试机制引入的额外期望时间 E[T_retry] = T_exec * (1/(1-P_fail)) ≈ 1.05-1.1 * T_exec。

## Corrected Claim

代码执行沙箱资源隔离与超时控制：基于 Docker + cgroups 的 Python 沙箱，限制单任务 CPU 时间 T_cpu_max=300s，内存 Mem_max=4GB，磁盘 Disk_max=10GB；对于典型科研计算任务（如 PyTorch 训练小模型、统计回归），平均执行时间 T_exec≈15-60s，失败率（因 OOM 或死循环）P_fail≈5-10%；重试机制引入的额外期望时间 E[T_retry] = T_exec * (1/(1-P_fail)) ≈ 1.05-1.1 * T_exec。

## Evidence

先验知识/题面给定，逻辑校验通过：资源限制参数符合常见沙箱配置惯例；重试期望时间公式 E[T]=T/(1-p) 在 p=0.05~0.1 时系数约为 1.05~1.11，与陈述一致；典型科研任务耗时量级合理。
