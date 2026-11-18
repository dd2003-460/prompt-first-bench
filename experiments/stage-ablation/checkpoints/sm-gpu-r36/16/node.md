# N313: AMD Radeon RX 7900 XTX 的显存容量为 24GB GDDR6，其带宽为 960 GB/s，单卡无法容纳 Qwen3-27B BF16 (54

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD Radeon RX 7900 XTX 的显存容量为 24GB GDDR6，其带宽为 960 GB/s，单卡无法容纳 Qwen3-27B BF16 (54GB) 或 FP8 (27GB) 权重，必须依赖 W4 量化 (14GB) 或双卡方案，这是评估 AMD 消费级方案可行性的基础参数。

## Corrected Claim

AMD Radeon RX 7900 XTX 的显存容量为 24GB GDDR6，其带宽为 960 GB/s（注：此为公认硬件规格，但当前参考来源未直接提供该具体数值），单卡无法容纳 Qwen3-27B BF16 (54GB) 或 FP8 (27GB) 权重，必须依赖 W4 量化 (14GB) 或双卡方案。

## Evidence

[质询]参考来源[1]仅提供了RX 7000系列的通用架构信息，未直接列出RX 7900 XTX的具体显存容量（24GB）和带宽（960 GB/s）数值；来源[2]和[3]与该事实完全无关。虽然这些参数符合AMD官方公开规格，但当前提供的参考来源中缺乏直接支持具体数值的证据。 | 逻辑校验通过：24GB显存确实无法容纳54GB (BF16) 或 27GB (FP8) 的模型权重，必须量化或双卡，推导自洽。但外部核验中，来源[1]主题相关但未提供具体数值支持，来源[2][3]无关，属于经验事实且缺直接来源支持。

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Radeon_RX_7000_series', 'type': None, 'title': 'wiki-full: Radeon RX 7000 series'}
- {'url': 'https://amd.com', 'type': None, 'title': 'direct-browser: amd.com'}
- {'url': 'http://arxiv.org/abs/2010.11678v1', 'type': 'arxiv', 'title': 'Neglected X-ray discovered polars: III. RX J0154.0-5947, RX J0600.5-2709, RX J08'}
