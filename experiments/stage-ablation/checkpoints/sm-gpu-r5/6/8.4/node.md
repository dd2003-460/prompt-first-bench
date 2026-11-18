# N84: RTX 4090 的 TDP 为 450W，双卡方案总功耗为 900W，但实际运行 LLM 推理时功耗波动在 800W-900W 之间

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 的 TDP 为 450W，双卡方案总功耗为 900W，但实际运行 LLM 推理时功耗波动在 800W-900W 之间

## Corrected Claim

RTX 4090 的 TDP 通常为 450W，双卡方案理论总功耗为 900W，实际运行 LLM 推理时功耗通常在 800W-900W 之间波动（具体数值需依据官方规格书确认）。

## Evidence

[质询]参考来源仅提及 RTX 4060 的功耗（115W），完全未覆盖 RTX 4090 的 TDP 或双卡推理功耗，属于来源缺失/不相关，无法通过外部证据直接验证具体数值（450W/900W/800-900W）。 | 逻辑上 450W*2=900W 自洽，且 LLM 推理功耗波动在 800-900W 符合高负载 GPU 特性；但参考来源 [1] 仅涉及 RTX 4060，与 RTX 4090 无关，无可用外部证据支持具体数值，属经验事实缺来源支持。

## Search Query

RTX 4090 TDP actual power draw dual card LLM inference average watts

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
