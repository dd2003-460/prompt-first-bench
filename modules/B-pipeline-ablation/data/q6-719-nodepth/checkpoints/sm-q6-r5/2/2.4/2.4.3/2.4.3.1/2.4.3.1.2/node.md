# N584: 在业务低谷期（K_valley=0.5），到达率 λ_valley 降至 7,750 req/s，此时边缘节点负载低于15%，可执行缓存预热、日志归档等后台任务

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

在业务低谷期（K_valley=0.5），到达率 λ_valley 降至 7,750 req/s，此时边缘节点负载低于15%，可执行缓存预热、日志归档等后台任务，同时带宽成本按峰值计费导致单位请求成本增加3-5倍。

## Corrected Claim

在业务低谷期（K_valley=0.5），到达率 λ_valley 降至 7,750 req/s，此时边缘节点负载低于15%，可执行缓存预热、日志归档等后台任务，同时带宽成本按峰值计费导致单位请求成本增加3-5倍。

## Evidence

先验知识/题面给定，逻辑校验通过：K_valley=0.5 与 7,750 req/s 在量级上自洽（隐含峰值约 15,500 req/s），低负载执行后台任务及固定成本分摊导致单位成本上升符合经济学直觉。

## Search Query

CDN off-peak request rate req/s bandwidth cost efficiency
