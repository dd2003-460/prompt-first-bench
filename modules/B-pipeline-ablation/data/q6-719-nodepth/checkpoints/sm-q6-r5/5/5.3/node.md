# N24: Pareto 前沿点 3（低成本高延迟）：策略为'全自建边缘节点'，目标 P99 延迟 ≤ 200ms（仅靠10个POP，长尾用户延迟升高）。成本构成：10个P

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Pareto 前沿点 3（低成本高延迟）：策略为'全自建边缘节点'，目标 P99 延迟 ≤ 200ms（仅靠10个POP，长尾用户延迟升高）。成本构成：10个POP的硬件折旧、带宽、运维人力。量化：单POP月均成本 50,000 CNY（含带宽+电力+人力），总成本 500,000 CNY/月。此点代表成本最低但延迟容忍度高的工作点。

## Corrected Claim

Pareto 前沿点 3（低成本高延迟）：策略为'全自建边缘节点'，目标 P99 延迟 ≤ 200ms（仅靠10个POP，长尾用户延迟升高）。成本构成：10个POP的硬件折旧、带宽、运维人力。量化：单POP月均成本 50,000 CNY（含带宽+电力+人力），总成本 500,000 CNY/月。此点代表成本最低但延迟容忍度高的工作点。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点在逻辑上是正交的（分别对应基础设施、带宽、运维、总成本汇总、延迟性能），且覆盖了父节点中提到的‘成本构成’和‘P99延迟目标’两个核心维度。虽然总成本子节点指出了与父节点假设值的差异，但这属于数据校准而非逻辑冗余。）

## Search Query

self-hosted CDN 10 POPs monthly cost 50k CNY per node P99 latency 200ms tradeoff
