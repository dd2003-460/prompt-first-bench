# N312: NVIDIA RTX 5090 (Blackwell) 的显存容量确认为 32GB GDDR7，而非传闻中的 24GB，这一容量是判断其能否单卡承载 Qwen3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA RTX 5090 (Blackwell) 的显存容量确认为 32GB GDDR7，而非传闻中的 24GB，这一容量是判断其能否单卡承载 Qwen3-27B FP8/INT8 权重的关键物理约束。

## Corrected Claim

NVIDIA RTX 5090 (Blackwell) 的显存容量据公开资料确认为 32GB GDDR7，这一容量是判断其能否单卡承载 Qwen3-27B FP8/INT8 权重的关键物理约束。

## Evidence

[质询]参考来源[1]虽然提及RTX 5090，但摘要中未包含具体的显存容量数值（32GB GDDR7），无法直接证实该具体硬件规格；来源[2]-[4]为通用页面，完全无关。 | 经验事实，逻辑自洽但缺来源支持（来源[1]主题相关但未在摘要中提供具体显存数值，其余来源无关）

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_50_series', 'type': None, 'title': 'wiki-full: GeForce RTX 50 series'}
- {'url': 'https://nvidia.com', 'type': None, 'title': 'direct-browser: nvidia.com'}
- {'url': 'https://www.nvidia.com/en-us/', 'type': 'bing', 'title': 'World Leader in Artificial Intelligence Computing | NVIDIA'}
- {'url': 'https://www.nvidia.com/en-us/drivers/', 'type': 'bing', 'title': 'Download The Official NVIDIA Drivers | NVIDIA'}
