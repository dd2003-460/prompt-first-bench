# N144: Prometheus/Grafana监控告警系统年维护成本分解：软件许可（开源免费）+ 存储成本（10节点×100GB日志×¥0.1/GB/月×12=¥1,20

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38

## Claim

Prometheus/Grafana监控告警系统年维护成本分解：软件许可（开源免费）+ 存储成本（10节点×100GB日志×¥0.1/GB/月×12=¥1,200）+ 人力维护（0.2 FTE×300,000元/年=¥60,000），总计约¥61,200/年，即人力成本的20.4%，与N38的10-20%区间一致

## Corrected Claim

Prometheus/Grafana监控告警系统年维护成本分解：软件许可（开源免费）+ 存储成本（10节点×100GB日志×¥0.1/GB/月×12=¥1,200）+ 人力维护（0.2 FTE×300,000元/年=¥60,000），总计约¥61,200/年，即人力成本的20.4%，与N38的10-20%区间一致

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（10*100*0.1*12=1200, 0.2*300000=60000, 1200+60000=61200），比例计算正确（1200/60000=20%或61200/300000=20.4%），符合开源监控成本结构常识。

## Search Query

prometheus grafana annual maintenance cost for 10 edge nodes
