# N82: RTX 4090 在运行 Qwen3-27B (BF16) 时的实际功耗为 400W-450W，需考虑双卡同时运行的峰值功耗叠加效应

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 在运行 Qwen3-27B (BF16) 时的实际功耗为 400W-450W，需考虑双卡同时运行的峰值功耗叠加效应

## Corrected Claim

RTX 4090 在运行 Qwen3-27B (BF16) 时功耗接近其 TDP 上限（约 450W），双卡运行需考虑峰值功耗叠加及电源冗余。

## Evidence

[质询]具体功耗数值（400W-450W）属于经验事实，缺乏直接来源支持，且不同负载下波动较大，精确区间难以仅凭逻辑推导确定。 | 经验事实，逻辑自洽但缺来源支持（来源[1]无关，来源[2]为RTX 4060规格，与RTX 4090无关）

## Search Query

RTX 4090 power consumption LLM inference 27B model watts dual card

## Retrieval Sources

- {'url': 'https://tomshardware.com', 'type': None, 'title': 'direct-browser: tomshardware.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
