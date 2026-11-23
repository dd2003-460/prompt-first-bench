# N194: 工作点 B（均衡型）：采用标准配置服务器（如 32GB RAM / 16 vCPU），单服务器并发能力 $C_{srv} \approx 8,000$，在 $C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

工作点 B（均衡型）：采用标准配置服务器（如 32GB RAM / 16 vCPU），单服务器并发能力 $C_{srv} \approx 8,000$，在 $C_{peak}=50,000$ 时 $N_{servers}=7$，单服务器成本约 12,000 元/月，总成本 84,000 元/月，但 P99 延迟更低。

## Corrected Claim

工作点 B（均衡型）：采用标准配置服务器（如 32GB RAM / 16 vCPU），单服务器并发能力 $C_{srv} \approx 8,000$，在 $C_{peak}=50,000$ 时 $N_{servers}=7$，单服务器成本约 12,000 元/月，总成本 84,000 元/月，但 P99 延迟更低。

## Evidence

先验知识/题面给定，逻辑校验通过：50,000/8,000=6.25，向上取整为7台服务器；7*12,000=84,000元，数值计算自洽且符合常规云资源成本量级。
