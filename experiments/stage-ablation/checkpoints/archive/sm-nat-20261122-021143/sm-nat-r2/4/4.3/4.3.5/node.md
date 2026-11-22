# N55: 实际可用缓存容量：C_eff = 128GB - Stale_bytes，其中 Stale_bytes 需通过 N25 的积分计算，而非固定 12.8GB，St

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

实际可用缓存容量：C_eff = 128GB - Stale_bytes，其中 Stale_bytes 需通过 N25 的积分计算，而非固定 12.8GB，Stale_bytes 可能显著小于 12.8GB，因为热门对象更新频率高但驻留时间短，冷对象更新频率低但驻留时间长。

## Corrected Claim

实际可用缓存容量：C_eff = 128GB - Stale_bytes，其中 Stale_bytes 需通过 N25 的积分计算，而非固定 12.8GB，Stale_bytes 可能显著小于 12.8GB，因为热门对象更新频率高但驻留时间短，冷对象更新频率低但驻留时间长。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存有效容量确实等于总容量减去陈旧数据占用，且陈旧数据量取决于对象更新频率与驻留时间的动态平衡，而非固定比例，符合缓存管理基本原理。

## Search Query

effective cache capacity stale data exclusion
