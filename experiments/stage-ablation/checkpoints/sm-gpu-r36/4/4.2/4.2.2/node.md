# N58: AMD Instinct MI250X (128GB HBM2e) 的当前市场可用性、单卡价格及 ROCm 软件栈稳定性评分；若可用，其 128GB 显存允许 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

AMD Instinct MI250X (128GB HBM2e) 的当前市场可用性、单卡价格及 ROCm 软件栈稳定性评分；若可用，其 128GB 显存允许 Qwen3-27B BF16 全量加载且支持超大 Batch Size，计算其相对于 2x RTX 4090 方案在吞吐量上的理论上限及实际 TCO 劣势 (价格/功耗/散热)

## Corrected Claim

AMD Instinct MI250X (128GB HBM2e) 具备128GB显存，理论上允许Qwen3-27B BF16全量加载并支持较大Batch Size；但其当前市场可用性、具体单卡价格、ROCm软件栈稳定性评分，以及相对于2x RTX 4090方案在吞吐量和TCO（价格/功耗/散热）上的具体量化对比，需依据最新市场报价及实测基准测试数据确定，现有参考来源未提供相关数值。

## Evidence

[质询]该陈述包含大量具体的经验性数值断言（如MI250X当前市场价格、ROCm稳定性评分、具体吞吐量理论上限及TCO劣势），这些属于硬件规格、市场价格及软件生态现状，无法从第一性原理推导，且参考来源中完全缺失相关数据支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]-[4]均未提供MI250X价格、ROCm评分或具体吞吐量对比数据）

## Search Query

AMD Instinct MI250X price availability ROCm stability Qwen 27B BF16 batch size throughput comparison 2x RTX 4090

## Retrieval Sources

- {'url': 'https://anandtech.com', 'type': None, 'title': 'direct-browser: anandtech.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://www.amd.com/en.html', 'type': 'bing', 'title': 'AMD ׀ together we advance_AI'}
- {'url': 'https://www.amd.com/en/support/download/drivers.html', 'type': 'bing', 'title': 'Drivers and Support for Processors and Graphics'}
