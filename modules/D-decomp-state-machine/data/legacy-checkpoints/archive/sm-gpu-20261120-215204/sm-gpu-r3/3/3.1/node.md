# N18: 工作点 1: 极致性价比 (低性能/低成本) - 单卡 RTX 4090 + 4-bit 量化。硬件成本 ~$1600，电力消耗 ~350W，TCO (3年) 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

工作点 1: 极致性价比 (低性能/低成本) - 单卡 RTX 4090 + 4-bit 量化。硬件成本 ~$1600，电力消耗 ~350W，TCO (3年) 约 $2500-3000 [待核验: 电价假设]。适用于非关键任务。

## Corrected Claim

工作点 1: 极致性价比 (低性能/低成本) - 单卡 RTX 4090 + 4-bit 量化。硬件成本 ~$1600，电力消耗 ~450W (TDP) 或 ~300-350W (降压优化后)，TCO (3年) 取决于电价，若仅计电力成本约 $2800+ (来源[1])，总 TCO 需结合具体电价计算。适用于非关键任务。

## Evidence

[质询]电力消耗数值存在口径混淆：RTX 4090 的 TDP 为 450W，而 350W 是 RTX 3090 的 TDP（来源[1]明确对比了两者功耗）。虽然通过降压超频（来源[2]）或特定负载下可能达到 350W，但将其作为标准工作点功耗陈述且未注明“降压/特定负载”条件，易与标准 TDP 混淆。此外，TCO 计算依赖于未明确给出的电价假设，且来源[1]给出的 3 年电力 TCO 为 $2,837（仅电力成本），若加上硬件成本 $1600，总 TCO 将远超 $2500-3000 的范围（除非电价极低或硬件成本已摊销/二手），数值量级与来源数据存在潜在矛盾。 | 来源[1]指出 RTX 4090 功耗为 450W 且 3 年电力 TCO 为 $2,837，与陈述中的 350W 功耗及 $2500-3000 总 TCO 存在数值偏差或口径不一致；来源[2]证实 4090 可降压至 300W 以下，支持低功耗可能性但非默认状态。

## Search Query

RTX 4090 TCO 3 years electricity cost 350W

## Retrieval Sources

- {'url': 'https://www.thesiliconreport.com/compare/nvidia-rtx-4090-vs-nvidia-rtx-3090&rut=df3b0271d679c81e6396e9b613a00032c6942fc1620ccf4a4aac2b4f25dd5360', 'type': 'ddg', 'title': 'RTX 4090 vs RTX 3090: Specs, Benchmarks & TCO | The Silicon Report'}
- {'url': 'https://www.xda-developers.com/rtx-4090-under-300w-voltage-curve-undervolt/&rut=a08d6ee882c1d59365cb9c77e580bb69760fb348b2a2563abe4ad3e50e8b9208', 'type': 'ddg', 'title': 'I got my RTX 4090 under 300W without tanking my 1% ... - XDA Developers'}
- {'url': 'https://aggressive.ai/gpu-cloud-4090-tco-in-autumn-2026&rut=f1bc30ba6f2dffcb99685dab7e4e87e435fb2e992ab61418c013ab9f8624d34f', 'type': 'ddg', 'title': 'RTX 4090 cloud total cost of ownership in autumn 2026 (2026)'}
