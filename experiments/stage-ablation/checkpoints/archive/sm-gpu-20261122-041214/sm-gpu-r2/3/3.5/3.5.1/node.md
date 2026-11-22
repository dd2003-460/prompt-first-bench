# N111: 修正 N31 中的功耗错误：1x A6000 的 TDP 为 300W，2x RTX 4090 的总 TDP 为 900W（450W x 2），单卡方案 OpE

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

修正 N31 中的功耗错误：1x A6000 的 TDP 为 300W，2x RTX 4090 的总 TDP 为 900W（450W x 2），单卡方案 OpEx 更低的前提是 A6000 功耗确实低于 2x 4090 总和，但需考虑系统级功耗（主板、风扇等）差异约 50-100W。

## Corrected Claim

修正 N31 中的功耗错误：1x A6000 的 TDP 为 300W，2x RTX 4090 的总 TDP 为 900W（450W x 2），单卡方案 OpEx 更低的前提是 A6000 功耗确实低于 2x 4090 总和，但需考虑系统级功耗（主板、风扇等）差异约 50-100W。

## Evidence

先验知识/题面给定，逻辑校验通过：A6000 TDP 300W 与 RTX 4090 TDP 450W 均为公开稳定规格，2x 4090 总功耗 900W 计算正确，系统级功耗差异估算合理。
