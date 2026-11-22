# N187: AMD MI300X 单卡运行 Qwen3-27B 的 TCO 对比基准：MI300X 192GB HBM3 价格约为 $20,000-$25,000，TDP 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

AMD MI300X 单卡运行 Qwen3-27B 的 TCO 对比基准：MI300X 192GB HBM3 价格约为 $20,000-$25,000，TDP 750W，年电力成本约为 750W * 8760h * $0.14/kWh ≈ $920/年；相比 2x RTX 4090 方案，MI300X 的一次性成本高 6-8 倍，但单卡支持 BF16 全精度推理，无需量化导致的精度损失 [待核验]

## Corrected Claim

AMD MI300X 单卡运行 Qwen3-27B 的 TCO 对比基准：MI300X 192GB HBM3 价格约为 $20,000-$25,000（视市场波动），TDP 750W，年电力成本约为 750W * 8760h * $0.14/kWh ≈ $920/年；相比 2x RTX 4090 方案，MI300X 的一次性成本高 6-8 倍，但单卡支持 BF16 全精度推理，通常可减少或避免量化带来的精度损失。

## Evidence

[质询]MI300X 的市场价格（$20,000-$25,000）属于经验事实，且该价格区间可能随市场波动或采购渠道不同而有较大差异，缺乏实时市场数据支持；此外，'无需量化导致的精度损失'这一表述过于绝对，虽然 MI300X 支持 BF16，但在实际部署中是否完全不需要任何量化优化（如 KV Cache 量化）取决于具体应用场景和显存占用情况，并非绝对真理。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，价格与具体性能对比属于经验数据，无法从第一性原理严格推出）

## Search Query

AMD MI300X price 2024 TCO comparison RTX 4090
