# N103: 监控与自动化工具栈成本：C_tool = C_prometheus_stack + C_logging + C_automation + C_cmdb，其中C_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

监控与自动化工具栈成本：C_tool = C_prometheus_stack + C_logging + C_automation + C_cmdb，其中C_prometheus_stack=¥20k-50k/年（自建Grafana+Prometheus集群），C_logging=¥10k-30k/年（ELK或Loki），C_automation=¥10k-20k/年（Ansible/Terraform），C_cmdb=¥5k-15k/年，总计¥45k-115k/年

## Corrected Claim

监控与自动化工具栈成本：C_tool = C_prometheus_stack + C_logging + C_automation + C_cmdb，其中C_prometheus_stack=¥20k-50k/年（自建Grafana+Prometheus集群），C_logging=¥10k-30k/年（ELK或Loki），C_automation=¥10k-20k/年（Ansible/Terraform），C_cmdb=¥5k-15k/年，总计¥45k-115k/年

## Evidence

先验知识/题面给定，逻辑校验通过：各项成本区间符合自建开源监控栈（Prometheus/Grafana/ELK/Ansible）在中小规模集群下的典型人力与基础设施投入量级，且分项之和与总计区间（45k-115k）数学自洽。
