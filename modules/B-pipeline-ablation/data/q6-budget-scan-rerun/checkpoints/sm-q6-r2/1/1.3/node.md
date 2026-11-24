# N8: 自建 10 个 POP 点（假设覆盖中国主要省级节点）的 P99 延迟基准值约为 200ms（受限于节点密度低，长尾地区回源距离增加，导致尾延迟显著高于公有云）

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

自建 10 个 POP 点（假设覆盖中国主要省级节点）的 P99 延迟基准值约为 200ms（受限于节点密度低，长尾地区回源距离增加，导致尾延迟显著高于公有云）

## Corrected Claim

自建 10 个 POP 点（假设覆盖中国主要省级节点）的 P99 延迟基准值约为 200ms（受限于节点密度低，长尾地区回源距离增加，导致尾延迟显著高于公有云）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于延迟（Latency）的构成拆解，子节点2聚焦于缓存命中率（CHR）这一关键变量及其成因。两者分别解释了父节点中‘延迟高’的两个主要驱动因素（物理距离/回源延迟 和 低命中率导致的回源频率增加），维度不同且互不重叠，共同完整解释了200ms P99延迟的来源。）

## Search Query

Self-hosted CDN 10 PoP points China P99 latency 200ms edge node density impact
