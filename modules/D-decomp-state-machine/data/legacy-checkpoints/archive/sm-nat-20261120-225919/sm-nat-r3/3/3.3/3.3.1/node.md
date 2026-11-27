# N59: 在频率突变场景下，LFU 缓存中旧热点对象的残留比例 f_stale 由 LFU 的遗忘因子 λ 和突变时间尺度 T_shift 决定，f_stale ≈ ex

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

在频率突变场景下，LFU 缓存中旧热点对象的残留比例 f_stale 由 LFU 的遗忘因子 λ 和突变时间尺度 T_shift 决定，f_stale ≈ exp(-λ * T_shift)，当 T_shift << 1/λ 时 f_stale → 1。

## Corrected Claim

在频率突变场景下，LFU 缓存中旧热点对象的残留比例 f_stale 由 LFU 的遗忘因子 λ 和突变时间尺度 T_shift 决定，f_stale ≈ exp(-λ * T_shift)，当 T_shift << 1/λ 时 f_stale → 1。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 的遗忘机制通常建模为频率随时间指数衰减，公式 f_stale ≈ exp(-λ * T_shift) 符合指数衰减规律，且 T_shift << 1/λ 时指数项趋近于 0，f_stale 趋近于 1，逻辑自洽。

## Search Query

LFU forgetting factor lambda steady state hit ratio
