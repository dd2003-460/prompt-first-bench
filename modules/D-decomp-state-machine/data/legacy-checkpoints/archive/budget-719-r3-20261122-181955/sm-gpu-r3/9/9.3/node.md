# N122: Apple M3 Ultra 的 TDP 约为 145W (Mac Studio M3 Ultra 整机功耗)，RTX 4090 的 TDP 为 450W；在 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

Apple M3 Ultra 的 TDP 约为 145W (Mac Studio M3 Ultra 整机功耗)，RTX 4090 的 TDP 为 450W；在 24/7 运行假设下，Apple 方案的年电力成本比 RTX 4090 低约 60-70%，具体数值取决于当地电价 [待核验]。

## Corrected Claim

Apple M3 Ultra 方案（Mac Studio）的整机功耗显著低于 RTX 4090 方案（约 145W vs 450W+），在 24/7 运行假设下，Apple 方案的年电力成本通常比 RTX 4090 低 60% 以上，具体数值取决于当地电价及实际负载。

## Evidence

[质询]数值量级与口径混淆：Apple M3 Ultra 的 TDP 通常指芯片功耗（约 100-120W），而 145W 更接近 Mac Studio 整机在特定负载下的功耗上限或平均值，直接将其与 GPU 的 TDP（450W）对比存在口径不一致；此外，60-70% 的成本节省是基于特定电价和负载假设的推导值，并非固定物理常数。 | 来源 [1] 和 [2] 确认了 Mac Studio M3 Ultra 与 RTX 4090 在功耗和能效上的显著差异，支持 Apple 方案更省电的定性结论，但未直接提供 145W 这一具体整机功耗数值及 60-70% 的精确成本比例，属于间接支持。

## Search Query

Apple M3 Ultra Mac Studio power consumption TDP vs RTX 4090

## Retrieval Sources

- {'url': 'https://www.myaihardware.com/compare-article/mac-studio-m3-ultra-vs-dual-rtx-4090&rut=72d77fdb930bd849fda0cfe6b8ee70bd95cd9ea128617a6e048fdacc711a4285', 'type': 'ddg', 'title': 'Mac Studio M3 Ultra vs 2x NVIDIA RTX 4090: It Depends [2026]'}
- {'url': 'https://techfixweekly.blog/nvidia-rtx-4090-vs-apple-m3-ultra-gpu-80-core&rut=04d79ea4311d0bc2bfc355b984fd3b11f8052d6b27f61dea3cce5e6f8a3941ff', 'type': 'ddg', 'title': 'NVIDIA RTX 4090 vs Apple M3 Ultra GPU 80 Core [Comparison]'}
- {'url': 'https://gadgetversus.com/graphics-card/apple-m3-ultra-gpu-80-core-vs-nvidia-geforce-rtx-4090/&rut=ea0294ffa7a97bb73592efe46dd19e24cd2b15ac58e6642c32b7656e16d5644c', 'type': 'ddg', 'title': 'Apple M3 Ultra GPU 80-Core vs Nvidia GeForce RTX 4090 - GadgetVersus'}
