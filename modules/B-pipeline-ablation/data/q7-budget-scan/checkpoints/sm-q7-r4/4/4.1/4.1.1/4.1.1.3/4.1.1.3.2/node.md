# N771: RAID 控制器故障切换时间 T_switchover_controller：双控冗余架构下，主控制器故障后副控制器接管时间 < 1 秒；单控架构下需重启系统，

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N286

## Claim

RAID 控制器故障切换时间 T_switchover_controller：双控冗余架构下，主控制器故障后副控制器接管时间 < 1 秒；单控架构下需重启系统，T_switchover ≈ 5-10 分钟

## Corrected Claim

RAID 控制器故障切换时间 T_switchover_controller：双控冗余架构下，主控制器故障后副控制器接管时间通常极短（毫秒至亚秒级）；单控架构下需重启系统或重新初始化，恢复时间较长（通常为分钟级，具体取决于硬件和固件）。

## Evidence

[质询]参考来源均与RAID控制器无关（来源1为Oracle数据库，来源2为Synology服务器高可用集群），缺乏直接证据支持具体的‘<1秒’和‘5-10分钟’数值；且单控架构下的恢复时间高度依赖具体硬件和固件实现，并非固定为5-10分钟。 | 逻辑自洽（双控热备通常毫秒级接管，单控冷启动需分钟级），但参考来源[1][2]均与RAID控制器主题无关，无法提供外部支持，属于经验事实缺来源支持。

## Search Query

RAID controller failover time dual controller redundancy

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29294975/article/details/158683353&rut=e73936a61e79b5ab32d7fc1332dae7687bc37e803e728d18a66d8e7d4d85f2e0', 'type': 'ddg', 'title': 'Oracle ADG 切换实战解析：Switchover 与 Failover 的最佳实践与场景选择-CSDN博客'}
- {'url': 'https://kb.synology.com/en-global/DSM/help/HighAvailability/switchover_failover&rut=974660fcd4986e74c649460727fb29d052a4241d32164a646ee12b9aec875770', 'type': 'ddg', 'title': 'Switchover/Auto-Failover | Synology High Availability - Synology ...'}
