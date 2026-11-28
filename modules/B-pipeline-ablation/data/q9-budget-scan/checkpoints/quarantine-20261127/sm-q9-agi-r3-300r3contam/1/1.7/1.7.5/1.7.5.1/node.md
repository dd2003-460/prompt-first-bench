# N148: Docker 容器冷启动耗时的主要构成是内核模块加载与网络命名空间创建，具体数值受宿主机内核版本影响，需实测 `time docker run --rm alp

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N52

## Claim

Docker 容器冷启动耗时的主要构成是内核模块加载与网络命名空间创建，具体数值受宿主机内核版本影响，需实测 `time docker run --rm alpine echo hi` 获取 P50 和 P95 值，当前估算 150ms 为 P50，P95 可能达 300ms。

## Corrected Claim

Docker 容器冷启动耗时主要受镜像准备、命名空间创建及运行时初始化影响，具体数值受宿主机环境与内核版本显著影响，建议通过实测 `time docker run --rm alpine echo hi` 获取 P50 和 P95 值以评估实际性能。

## Evidence

[质询]将Docker容器冷启动耗时主要归因于“内核模块加载”缺乏普遍性支持，通常主要开销在于镜像层解压/挂载、PID/NetNS创建及runc初始化，且具体数值（150ms/300ms）高度依赖硬件与内核配置，作为通用估算值缺乏严谨性。 | 先验知识/题面给定，逻辑校验通过，但具体数值与归因细节属经验事实，缺乏外部来源直接支持，故降级。
