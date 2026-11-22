# N334: systemd 自动重启服务的实现成本与效果：部署 systemd service 文件配置 Restart=on-failure 和 RestartSec=1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110

## Claim

systemd 自动重启服务的实现成本与效果：部署 systemd service 文件配置 Restart=on-failure 和 RestartSec=10，开发成本约为 2 小时（一次性），运行后自动重启成功率为 95%，剩余 5% 需人工介入；该机制将平均故障恢复时间 (MTTR) 从人工干预的 4 小时降低至 15 秒，年化节省停机时间约为 380 小时（假设年故障 10 次）。

## Corrected Claim

systemd 通过配置 Restart=on-failure 和 RestartSec 可实现服务自动重启，通常能显著降低平均故障恢复时间（MTTR）并减少人工介入需求，具体节省的停机时间和成功率取决于系统稳定性及故障类型。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如95%成功率、4小时人工MTTR、15秒自动MTTR、380小时年化节省），这些并非第一性原理可推导的数学或物理事实，而是高度依赖具体系统环境、故障类型和运维流程的经验数据，缺乏通用性。 | 逻辑校验通过：数学计算自洽（10次故障 * (4小时 - 15秒) ≈ 39.96小时，若按380小时反推需约95次故障或更长的单次节省时间，此处存在数值量级上的轻微不一致，但作为估算模型逻辑框架成立；然而，由于source为knowledge且无外部来源支持，且具体数值（如95%成功率、380小时）属于经验事实，无法从第一性原理严格推出，根据规则应降级。
