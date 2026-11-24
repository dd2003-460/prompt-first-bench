# N301: 自建 POP 监控与日志系统月度成本 C_tool_monthly 的构成：C_tool_monthly = C_monitoring + C_logging 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

自建 POP 监控与日志系统月度成本 C_tool_monthly 的构成：C_tool_monthly = C_monitoring + C_logging + C_ci_cd，其中 C_monitoring (Prometheus/Grafana 集群+告警) ≈ 5000 CNY/月，C_logging (ELK/ClickHouse 存储与计算) ≈ 8000 CNY/月，C_ci_cd (GitLab/Jenkins 许可及 CI 资源) ≈ 2000 CNY/月，合计 C_tool_monthly ≈ 15000 CNY/月。

## Corrected Claim

自建 POP 监控与日志系统月度成本 C_tool_monthly 的构成：C_tool_monthly = C_monitoring + C_logging + C_ci_cd，其中 C_monitoring (Prometheus/Grafana 集群+告警) ≈ 5000 CNY/月，C_logging (ELK/ClickHouse 存储与计算) ≈ 8000 CNY/月，C_ci_cd (GitLab/Jenkins 许可及 CI 资源) ≈ 2000 CNY/月，合计 C_tool_monthly ≈ 15000 CNY/月。

## Evidence

先验知识/题面给定，逻辑校验通过
