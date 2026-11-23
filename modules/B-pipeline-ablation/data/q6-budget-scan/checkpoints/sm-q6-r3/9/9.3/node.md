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

父节点级核验通过：正交+完备+无冗余（子节点准确对应父节点公式中的四个独立成本项（Prometheus栈、日志、自动化、CMDB），彼此职责清晰无重叠。虽然Prometheus子节点的估算上限(¥60k)略高于父节点该项上限(¥50k)，且日志子节点包含了ELK/Loki两种方案对比，但这属于对同一组件不同技术选型的详细拆解，而非子节点间的冗余。所有关键成本构成均已覆盖。）
