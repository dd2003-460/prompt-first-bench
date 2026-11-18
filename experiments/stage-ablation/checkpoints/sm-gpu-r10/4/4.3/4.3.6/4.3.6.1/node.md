# N208: Apple M2 Ultra 的内存控制器支持最多 8 个 LPDDR5 颗粒（4 个 16Gb x16 或等效配置），理论峰值带宽 = 颗粒数量 × 单颗粒带

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Apple M2 Ultra 的内存控制器支持最多 8 个 LPDDR5 颗粒（4 个 16Gb x16 或等效配置），理论峰值带宽 = 颗粒数量 × 单颗粒带宽（~17.6 GB/s per 16Gb x16 @ 6400MT/s），上限为 800 GB/s；增加 GPU 核心数不改变内存控制器通道数，因此带宽不可扩展

## Corrected Claim

Apple M2 Ultra 的内存控制器支持最多 8 个 LPDDR5 颗粒（4 个 16Gb x16 或等效配置），理论峰值带宽 = 颗粒数量 × 单颗粒带宽（~17.6 GB/s per 16Gb x16 @ 6400MT/s），上限为 800 GB/s；增加 GPU 核心数不改变内存控制器通道数，因此带宽不可扩展

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Apple M2 Ultra memory controller LPDDR5 channel count bandwidth limit
