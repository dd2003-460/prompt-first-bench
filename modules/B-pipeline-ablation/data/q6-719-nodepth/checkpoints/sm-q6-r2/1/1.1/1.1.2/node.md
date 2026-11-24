# N51: P99 延迟目标 T 的成本-体验权衡曲线：T 每降低 10ms，自建 POP 策略的基础设施成本（硬件/带宽）增加约 5-15%（因需更密集部署或更高性能硬件

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

P99 延迟目标 T 的成本-体验权衡曲线：T 每降低 10ms，自建 POP 策略的基础设施成本（硬件/带宽）增加约 5-15%（因需更密集部署或更高性能硬件），而公有云 CDN 的成本增加幅度较小（约 2-5%），具体系数需基于厂商报价单计算。

## Corrected Claim

P99 延迟目标 T 的降低通常会导致自建 POP 策略的基础设施成本增加幅度大于公有云 CDN，具体增加比例需基于厂商报价单和实际部署密度计算。

## Evidence

[质询]该陈述包含具体的经验性数值范围（5-15% vs 2-5%），这些系数高度依赖于具体的业务场景、流量分布、硬件选型及厂商定价策略，并非普适的物理或数学定律，属于典型的经验事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

CDN latency optimization cost tradeoff infrastructure investment per ms reduction
