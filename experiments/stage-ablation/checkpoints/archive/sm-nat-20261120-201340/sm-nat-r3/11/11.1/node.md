# N156: LFU 的瞬态优势量化：在缓存未饱和或存在突发冷请求时，LFU 因保留高频对象而避免驱逐热点，其增益 ΔH_transient 可通过模拟计算，典型值在 5-1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

LFU 的瞬态优势量化：在缓存未饱和或存在突发冷请求时，LFU 因保留高频对象而避免驱逐热点，其增益 ΔH_transient 可通过模拟计算，典型值在 5-15 个百分点之间，但稳态下此增益消失。

## Corrected Claim

LFU 的瞬态优势量化：在缓存未饱和或存在突发冷请求时，LFU 因保留高频对象而避免驱逐热点，其增益 ΔH_transient 可通过模拟计算，典型值在 5-15 个百分点之间，但稳态下此增益消失。

## Evidence

先验知识/题面给定，逻辑校验通过
