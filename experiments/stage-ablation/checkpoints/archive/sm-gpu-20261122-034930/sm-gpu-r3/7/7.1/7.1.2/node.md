# N391: AMD MI300X vs 2x RTX 4090 性价比对比：MI300X单卡价格约$4,000-$5,000 [待核验]，TDP 750W，3年TCO（含$

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139

## Claim

AMD MI300X vs 2x RTX 4090 性价比对比：MI300X单卡价格约$4,000-$5,000 [待核验]，TDP 750W，3年TCO（含$3,000基础设施）≈ $5,500 + 3*(750*0.5*8760/1000*0.15) ≈ $5,500 + $1,874 = $7,374。性价比指标 = 112.5 tokens/s / $7,374 ≈ 15.26 tokens/s/$。对比2x RTX 4090的11.83 tokens/s/$（N115），MI300X在纯性能/成本比上高出29%。但此结论依赖于MI300X在ROCm上能达到112.5 tokens/s的假设，若实际效率仅为50%（56.25 tokens/s），则性价比降至7.63 tokens/s/$，低于4090方案。

## Corrected Claim

AMD MI300X vs 2x RTX 4090 性价比对比：基于假设 MI300X 单卡价格约 $4,000-$5,000 且 ROCm 效率达到 112.5 tokens/s，其 3 年 TCO 约为 $7,374，性价比指标约为 15.26 tokens/s/$，高于 2x RTX 4090 的 11.83 tokens/s/$。但该结论高度依赖于价格与性能假设，若实际效率或价格偏离假设，结论可能反转。

## Evidence

[质询]MI300X 单卡价格 $4,000-$5,000 为经验事实，且该价格区间可能偏低（通常企业级采购价更高），同时 112.5 tokens/s 的性能假设缺乏具体模型和上下文支持，属于未经验证的假设参数。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证价格与性能假设）

## Search Query

AMD MI300X price 2024 Qwen3 27B inference throughput ROCm benchmark
