# N619: T=150ms 工作点下，增加 2-3 个 POP 节点的硬件增量成本 ΔC_infra 计算为：新增 3 POP * 2 台/POP * ¥1,500/台/月

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N203

## Claim

T=150ms 工作点下，增加 2-3 个 POP 节点的硬件增量成本 ΔC_infra 计算为：新增 3 POP * 2 台/POP * ¥1,500/台/月 = ¥9,000/月，占总基础设施成本 ¥30,000 的 30%，但考虑到 T=150ms 允许更宽松的带宽冗余，实际有效成本增幅通过带宽节省抵消后净增 10%。

## Corrected Claim

T=150ms 工作点下，增加 3 个 POP 节点的硬件增量成本为 ¥9,000/月，占总基础设施成本 ¥30,000 的 30%；考虑到 T=150ms 允许更宽松的带宽冗余，预计带宽成本节省可部分抵消该增量，但具体净增幅需结合带宽定价模型进一步测算。

## Evidence

[质询]「带宽节省抵消后净增10%」这一结论缺乏具体的带宽成本模型、流量分布假设及冗余系数支撑，属于未经验证的定性推断，且与前面精确计算的30%硬件增量存在逻辑跳跃。 | source=knowledge，硬件成本算术正确（3*2*1500=9000, 9000/30000=30%），但带宽节省抵消逻辑缺乏具体参数支撑，属经验性推断，降级为定性表述。

## Search Query

adding edge POP nodes cost increase 150ms latency budget
