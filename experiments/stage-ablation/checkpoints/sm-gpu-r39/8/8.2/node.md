# N82: RTX 4090 在运行 Qwen3-27B (BF16) 时的实际功耗为 400W-450W，需考虑双卡同时运行的峰值功耗叠加效应

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 在运行 Qwen3-27B (BF16) 时的实际功耗为 400W-450W，需考虑双卡同时运行的峰值功耗叠加效应

## Corrected Claim

RTX 4090 在运行 Qwen3-27B (BF16) 时的实际功耗接近其 TDP（约 450W），需考虑双卡同时运行的峰值功耗叠加效应

## Evidence

[质询]参考来源仅提及 RTX 4060 的功耗（115W），完全未涉及 RTX 4090 或 Qwen3-27B 的负载情况，无法提供外部证据支持 400W-450W 的具体数值；且该数值属于经验事实，需实测数据支持。 | 经验事实，逻辑自洽（RTX 4090 TDP 450W，满载推理功耗接近 TDP 合理），但参考来源 [1] 仅涉及 RTX 4060，与事实主题无关，无可用外部证据支持具体数值。

## Search Query

RTX 4090 power consumption LLM inference 27B model watts dual card

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
