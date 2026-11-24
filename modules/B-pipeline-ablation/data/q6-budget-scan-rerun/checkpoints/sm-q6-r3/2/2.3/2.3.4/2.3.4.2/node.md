# N199: 自建10 POP点开源监控栈（Prometheus+Grafana）人力与存储成本：假设需0.5 FTE运维（年薪20万）及每POP点1TB监控数据存储（10点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

自建10 POP点开源监控栈（Prometheus+Grafana）人力与存储成本：假设需0.5 FTE运维（年薪20万）及每POP点1TB监控数据存储（10点共10TB，对象存储约0.12元/GB/月），年成本 = 200,000 + (10,000GB * 0.12 * 12) = 200,000 + 14,400 = 214,400元 ≈ 21.4万元/年。

## Corrected Claim

自建10 POP点开源监控栈（Prometheus+Grafana）人力与存储成本：假设需0.5 FTE运维（年薪20万）及每POP点1TB监控数据存储（10点共10TB，对象存储约0.12元/GB/月），年成本 = 200,000 + (10,000GB * 0.12 * 12) = 200,000 + 14,400 = 214,400元 ≈ 21.4万元/年。

## Evidence

先验知识/题面给定，逻辑校验通过：人力成本20万与存储成本1.44万（10TB*0.12元/GB/月*12月）相加得21.44万，计算无误且量级合理。

## Search Query

Prometheus monitoring operational cost FTE estimate
