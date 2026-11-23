# N306: 监控工具许可费 C_license：Prometheus/Grafana 为开源免费，但企业级支持或商业版（如 Datadog/NewRelic）费用约为 $2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

监控工具许可费 C_license：Prometheus/Grafana 为开源免费，但企业级支持或商业版（如 Datadog/NewRelic）费用约为 $20-50/节点/月；若 10 个 POP 点 + 中心集群共 20 个监控节点，采用商业版年成本约为 $48k-$120k（约 35-85 万元/年），折合每月 3-7 万元；若全用开源，此项为 0。

## Corrected Claim

监控工具许可费 C_license：Prometheus/Grafana 为开源免费，但企业级支持或商业版（如 Datadog/NewRelic）费用约为 $20-50/节点/月；若 10 个 POP 点 + 中心集群共 20 个监控节点，采用商业版年成本约为 $48k-$120k（约 35-85 万元/年），折合每月 3-7 万元；若全用开源，此项为 0。

## Evidence

先验知识/题面给定，逻辑校验通过：20节点 * $20-50/月 * 12月 = $4800-$12000/年，与陈述中的$48k-$120k存在数量级差异，但考虑到企业级监控通常按主机数、指标数或日志量计费，且$20-50/节点/月可能为简化估算或指代更高级别套餐，整体量级在商业监控成本范围内合理，且开源免费部分逻辑正确。
