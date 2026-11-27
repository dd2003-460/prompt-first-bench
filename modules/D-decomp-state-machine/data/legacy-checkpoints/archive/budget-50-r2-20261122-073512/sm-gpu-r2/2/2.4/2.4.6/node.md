# N112: 二手 Tesla V100 32GB HBM2 的 2024-05 至 2024-11 期间平均价格为 $800-$1,200/卡，因架构老旧（Volta）缺乏

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

二手 Tesla V100 32GB HBM2 的 2024-05 至 2024-11 期间平均价格为 $800-$1,200/卡，因架构老旧（Volta）缺乏最新 CUDA 支持，性能折旧系数为 0.6-0.7。

## Corrected Claim

二手 Tesla V100 32GB HBM2 在 2024 年末至 2026 年初的市场价格约为 $980-$1,000/卡；因架构老旧，其相对最新架构的性能/价格比显著降低（具体折旧系数视基准而定，通常认为性价比低于新一代架构）。

## Evidence

[质询]来源仅提供了2024-2026年间的部分价格快照（如$983, $995），缺乏2024年5月至11月期间的完整历史数据以证实“平均价格”为$800-$1,200；且“性能折旧系数0.6-0.7”属于主观经验估算，无来源直接支持该具体数值范围。 | 来源[2]和[3]显示二手V100 32GB价格在$983-$995左右，落在$800-$1,200区间内，间接支持价格量级；但折旧系数为经验事实，缺直接来源支持，故降级。

## Search Query

Tesla V100 32GB used price 2024 depreciation factor

## Retrieval Sources

- {'url': 'https://www.ebay.com/sch/i.html?_nkw=tesla+v100+32gb&_sop=12&rut=2cabbc8fd8aa2663aa4c1e6b0eebb1e40755d45e071835522eb9e045bb38f47b', 'type': 'ddg', 'title': 'Tesla V100 32GB for sale - eBay'}
- {'url': 'https://gpupoet.com/gpu/shop/nvidia-tesla-v100-32gb&rut=cf8f6d261e7a628e3534294011ca6547803529dbc2f123841041047e35169d0a', 'type': 'ddg', 'title': 'Used NVIDIA Tesla V100 32GB for Sale — 81 Listings from $983'}
- {'url': 'https://gpudojo.com/tesla-v100&rut=92272d60dbedd89f06c9fe8239d00c8b7439c87f49ac378dfdb13cbdd79ccf6c', 'type': 'ddg', 'title': 'Tesla V100 32GB Used Price & History (Nov 2026) | GPUDojo'}
