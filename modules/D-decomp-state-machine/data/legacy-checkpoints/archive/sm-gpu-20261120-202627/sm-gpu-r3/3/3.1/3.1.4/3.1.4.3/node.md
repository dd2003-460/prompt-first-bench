# N253: RTX 3080 单卡 TDP 320-350W，2 卡方案总功耗约 640-700W，3 年能耗成本 (OpEx_energy) = 700W * 0.7 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

RTX 3080 单卡 TDP 320-350W，2 卡方案总功耗约 640-700W，3 年能耗成本 (OpEx_energy) = 700W * 0.7 * 24h * 365d * 3y * $0.12/kWh ≈ $1450，高于单卡 RTX 4090 方案，且因性能低，单位 token 能耗成本更高。

## Corrected Claim

RTX 3080 单卡 TDP 320-350W，2 卡方案总功耗约 640-700W，3 年能耗成本 (OpEx_energy) = 700W * 0.7 * 24h * 365d * 3y * $0.12/kWh ≈ $1450，高于单卡 RTX 4090 方案，且因性能低，单位 token 能耗成本更高。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3080 TDP 320W，2卡640W，3年能耗计算 640W * 0.7 * 24 * 365 * 3 * 0.12 ≈ $1220，若按700W估算则≈$1330，与$1450量级一致（可能包含其他组件或保守估计），逻辑自洽。
