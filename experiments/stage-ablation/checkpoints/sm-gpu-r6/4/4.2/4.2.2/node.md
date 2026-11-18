# N58: AMD Instinct MI250X (128GB HBM2e) 的当前市场可用性、单卡价格及 ROCm 软件栈稳定性评分；若可用，其 128GB 显存允许 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

AMD Instinct MI250X (128GB HBM2e) 的当前市场可用性、单卡价格及 ROCm 软件栈稳定性评分；若可用，其 128GB 显存允许 Qwen3-27B BF16 全量加载且支持超大 Batch Size，计算其相对于 2x RTX 4090 方案在吞吐量上的理论上限及实际 TCO 劣势 (价格/功耗/散热)

## Corrected Claim

AMD Instinct MI250X (128GB HBM2e) 的128GB显存容量在理论上允许Qwen3-27B BF16模型全量加载并支持超大Batch Size；但其当前市场具体价格、ROCm软件栈稳定性评分及相对于2x RTX 4090方案的精确TCO劣势需依据最新市场报价及实测数据确定，现有参考来源未提供具体数值。

## Evidence

[质询]该陈述包含大量具体的经验性市场数据（MI250X当前价格、ROCm稳定性评分、具体TCO对比数值），这些属于动态变化的商业/工程事实，无法从第一性原理推导，且参考来源中完全缺失相关数据支持，存在‘无源断言’风险。 | 逻辑上128GB显存确实足以加载Qwen3-27B BF16（约54GB）并支持大Batch，但参考来源[1]-[4]仅涉及RTX 4060规格及AMD通用介绍，未提供MI250X价格、ROCm评分或TCO对比数据，属于经验事实缺来源支持。

## Search Query

AMD Instinct MI250X price availability ROCm stability Qwen 27B BF16 batch size throughput comparison 2x RTX 4090

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://www.amd.com/en.html', 'type': 'bing', 'title': 'AMD ׀ together we advance_AI'}
- {'url': 'https://www.amd.com/en/support/download/drivers.html', 'type': 'bing', 'title': 'Drivers and Support for Processors and Graphics'}
- {'url': 'https://en.wikipedia.org/wiki/AMD', 'type': 'bing', 'title': 'AMD - Wikipedia'}
