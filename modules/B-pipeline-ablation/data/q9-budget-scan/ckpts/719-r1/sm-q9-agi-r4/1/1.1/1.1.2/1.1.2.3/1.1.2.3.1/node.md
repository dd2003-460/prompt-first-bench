# N355: GVisor (runsc) 沙箱启动开销并非恒定 1s，而是受宿主机负载影响波动；在 Mac M1 Max 或 Linux 服务器上，冷启动 (cold st

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

GVisor (runsc) 沙箱启动开销并非恒定 1s，而是受宿主机负载影响波动；在 Mac M1 Max 或 Linux 服务器上，冷启动 (cold start) 耗时通常为 0.5-1.5s，热启动 (warm start) 可降至 50-100ms；若采用 Docker 替代 GVisor，启动开销可进一步降低至 200-500ms，但安全性略降

## Corrected Claim

GVisor (runsc) 沙箱启动开销受宿主机负载及环境配置影响显著波动；通常冷启动耗时高于热启动，热启动优化后可大幅降低延迟；相比 GVisor，Docker 容器启动开销通常更低，但提供的隔离安全性较弱。

## Evidence

[质询]具体数值范围（如冷启动0.5-1.5s、热启动50-100ms、Docker 200-500ms）属于高度依赖硬件配置、内核版本及镜像大小的经验数据，缺乏通用标准，且不同基准测试结果差异巨大，易产生误导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

GVisor runsc cold start latency benchmark vs Docker
