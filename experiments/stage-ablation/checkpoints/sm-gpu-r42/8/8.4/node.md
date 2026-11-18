# N84: RTX 4090 的 TDP 为 450W，双卡方案总功耗为 900W，但实际运行 LLM 推理时功耗波动在 800W-900W 之间

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 的 TDP 为 450W，双卡方案总功耗为 900W，但实际运行 LLM 推理时功耗波动在 800W-900W 之间

## Corrected Claim

RTX 4090 的 TDP 为 450W，双卡方案总功耗上限为 900W，实际运行 LLM 推理时功耗通常低于 TDP 上限

## Evidence

[质询]来源[2]仅提供了RTX 4060的功耗（115W），未提供RTX 4090的TDP或双卡实际运行功耗数据，无法直接支持该具体数值断言；且实际运行功耗受负载影响，800W-900W的波动范围缺乏具体测试数据支撑。 | 经验事实，逻辑自洽（450W*2=900W，实际功耗略低于TDP上限符合物理直觉）但缺来源直接支持（来源[2]仅提及RTX 4060，与RTX 4090无关）

## Search Query

RTX 4090 TDP actual power draw dual card LLM inference average watts

## Retrieval Sources

- {'url': 'https://tomshardware.com', 'type': None, 'title': 'direct-browser: tomshardware.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
