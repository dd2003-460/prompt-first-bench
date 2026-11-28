# N208: Crossref REST API 在 2025-2026 年的标准速率限制为 50 requests/sec per IP，但在高负载时段实际 P99 延迟可

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

Crossref REST API 在 2025-2026 年的标准速率限制为 50 requests/sec per IP，但在高负载时段实际 P99 延迟可能飙升至 2-3 秒，远超 500ms 的设计假设，需引入本地缓存层（Redis）以应对突发流量。

## Corrected Claim

Crossref REST API 在高负载时段可能出现显著延迟（如 P99 超过 500ms），建议引入本地缓存层（如 Redis）以优化响应时间并减轻上游压力；具体速率限制阈值需参照 Crossref 最新官方文档确认。

## Evidence

[质询]Crossref 官方文档通常建议客户端保持保守速率（如每秒 1-5 次请求以避免被限流或视为滥用），声称其‘标准速率限制’为 50 requests/sec 缺乏权威来源支持，且该数值可能混淆了服务器最大承载能力与推荐客户端行为；此外，P99 延迟数据属于特定时间段的经验观测值，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且具体 API 速率限制参数及延迟表现属于经验规格，不适用第一性原理推导条款）

## Search Query

Crossref API rate limit 2025 latency P99 benchmark
