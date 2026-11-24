# N1235: LRU 驱逐率 E_lru 与对象大小 s 的关系模型：E_lru ∝ 1/s，当 s 减至 1/4 时，理论上 E_lru 应降低至 1/4；需结合实际访问频

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N424

## Claim

LRU 驱逐率 E_lru 与对象大小 s 的关系模型：E_lru ∝ 1/s，当 s 减至 1/4 时，理论上 E_lru 应降低至 1/4；需结合实际访问频率分布（Zipf 指数 α）计算新的驱逐率，若 α > 1.0，则驱逐率降幅可能小于 4 倍。

## Corrected Claim

LRU 驱逐率 E_lru 与对象大小 s 的关系模型：E_lru ∝ 1/s，当 s 减至 1/4 时，理论上 E_lru 应降低至 1/4；需结合实际访问频率分布（Zipf 指数 α）计算新的驱逐率，若 α > 1.0，则驱逐率降幅可能小于 4 倍。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU eviction rate dependence on object size and Zipf distribution
