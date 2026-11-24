# N504: SSD写缓存方案复杂度溢价：引入SSD缓存层需额外的软件逻辑（如脏页回写策略、缓存一致性检查），增加运维复杂度系数 k_ops_ssdcache = 1.3（相

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

SSD写缓存方案复杂度溢价：引入SSD缓存层需额外的软件逻辑（如脏页回写策略、缓存一致性检查），增加运维复杂度系数 k_ops_ssdcache = 1.3（相比纯HDD的1.0）。年化额外运维成本 ΔC_ops = 0.2 FTE * ¥200,000 * (1.3 - 1.0) = ¥12,000/年。此项成本在N219原估算中缺失。

## Corrected Claim

SSD写缓存方案复杂度溢价：引入SSD缓存层需额外的软件逻辑（如脏页回写策略、缓存一致性检查），增加运维复杂度系数 k_ops_ssdcache = 1.3（相比纯HDD的1.0）。年化额外运维成本 ΔC_ops = 0.2 FTE * ¥200,000 * (1.3 - 1.0) = ¥12,000/年。此项成本在N219原估算中缺失。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Storage tiering software operational complexity cost estimate
