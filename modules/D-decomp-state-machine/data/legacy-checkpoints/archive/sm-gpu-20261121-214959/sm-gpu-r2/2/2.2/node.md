# N13: 数据中心级显卡候选集：NVIDIA H100 SXM (80GB HBM3, 2039 GB/s, $25,000-30,000), NVIDIA H200 (

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

数据中心级显卡候选集：NVIDIA H100 SXM (80GB HBM3, 2039 GB/s, $25,000-30,000), NVIDIA H200 (141GB HBM3e, 4800 GB/s, $30,000-35,000) [待核验：H200 实际价格], NVIDIA B200 (192GB HBM3e, 8000 GB/s, $40,000+) [待核验：B200 价格], AMD MI300X (192GB HBM3, 5300 GB/s, $15,000-20,000) [待核验：MI300X 市场实际成交价]。

## Corrected Claim

数据中心级显卡候选集：NVIDIA H100 SXM (80GB HBM3, 2039 GB/s), NVIDIA H200 (141GB HBM3e, 4800 GB/s), NVIDIA B200 (192GB HBM3e, 8000 GB/s), AMD MI300X (192GB HBM3, 5300 GB/s)。具体价格需参考最新市场报价，通常H100在$25k-30k区间，H200/B200/MI300X价格随市场波动较大。

## Evidence

父节点级核验未通过：有冗余（子节点4（MI300X）与子节点1-3结构高度重复，属于同一计算模板的不同参数实例；子节点5（TCO）虽独立但与前四个硬件性能节点在逻辑层级上略有混杂（性能 vs 成本），但整体无矛盾且覆盖全面。）

## Search Query

NVIDIA H200 B200 price specs AMD MI300X price 2024 2025
