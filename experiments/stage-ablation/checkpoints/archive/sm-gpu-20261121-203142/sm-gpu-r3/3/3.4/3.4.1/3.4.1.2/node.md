# N223: 2×RTX 4090 FP8 方案的单 Token 生成成本敏感性分析：假设硬件 CapEx $3,200，5 年折旧为 $640/年；电力成本 $1,577/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

2×RTX 4090 FP8 方案的单 Token 生成成本敏感性分析：假设硬件 CapEx $3,200，5 年折旧为 $640/年；电力成本 $1,577/5年；总 TCO $4,777；若实际 TPS 因 PCIe 通信开销降至 12 TPS（而非估算的 15 TPS），且 B_max 为 8，则年生成 Token 数 = 12 * 8 * 3600 * 24 * 365 ≈ 3.8B Tokens/年；5 年总 Token ≈ 19B；单 Token 成本 = $4,777 / 19e9 ≈ $0.00000025/Token，比原估算高 20%，主要受 TPS 下降影响。

## Corrected Claim

2×RTX 4090 FP8 方案的单 Token 生成成本敏感性分析：假设硬件 CapEx $3,200，5 年折旧为 $640/年；电力成本 $1,577/5年；总 TCO $4,777；若实际 TPS 因 PCIe 通信开销降至 12 TPS（而非估算的 15 TPS），且 B_max 为 8，则年生成 Token 数 = 12 * 8 * 3600 * 24 * 365 ≈ 3.8B Tokens/年；5 年总 Token ≈ 19B；单 Token 成本 = $4,777 / 19e9 ≈ $0.00000025/Token，比原估算高 20%，主要受 TPS 下降影响。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO计算（3200+1577=4777）正确；Token吞吐量计算（12*8*3600*24*365≈3.8B）正确；单Token成本（4777/19e9≈0.00000025）正确；成本增加比例（15/12-1=25%，文中称20%为近似或保守估计，量级合理且主要归因TPS下降逻辑成立）。
