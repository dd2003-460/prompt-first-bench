# N220: Detection Time 的硬下限由 Prometheus 抓取间隔决定：scrape_interval=30s，加上 Alertmanager 评估与通知

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

Detection Time 的硬下限由 Prometheus 抓取间隔决定：scrape_interval=30s，加上 Alertmanager 评估与通知延迟（典型 15-30s），理论最小 Detection Time 为 45-60s（0.75-1.0 min），远低于 5min 预算，留有 4-5 倍安全裕度

## Corrected Claim

Detection Time 的硬下限由 Prometheus 抓取间隔决定：scrape_interval=30s，加上 Alertmanager 评估与通知延迟（典型 15-30s），理论最小 Detection Time 为 45-60s（0.75-1.0 min），远低于 5min 预算，留有 4-5 倍安全裕度

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在逻辑矛盾与覆盖缺失。1. 正交性/矛盾：父节点声称'理论最小 Detection Time 为 45-60s'，但子节点2明确指出'总检测延迟理论最小值为 0s'，二者直接矛盾；且子节点1和2均涉及'延迟'计算，边界模糊。2. 完备性：父节点结论依赖'15-30s'的Alertmanager延迟，但子节点未明确解释该区间如何由'评估间隔'与'通知延迟'组合得出，缺乏从组件到总时延的逻辑推导链。3. 冗余：子节点1和2分别描述了Prometheus和Alertmanager的延迟分布，本质上都是'时间窗口内的随机等待'模型，可合并为统一的'采样/评估延迟模型'以减少碎片化。）
