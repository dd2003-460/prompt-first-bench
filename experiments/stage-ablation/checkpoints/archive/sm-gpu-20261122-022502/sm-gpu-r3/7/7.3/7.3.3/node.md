# N260: Apple M3 Ultra 方案的修正 TCO 计算：CapEx 取 Mac Studio M3 Ultra 512GB 配置约 $6,000-$8,000 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

Apple M3 Ultra 方案的修正 TCO 计算：CapEx 取 Mac Studio M3 Ultra 512GB 配置约 $6,000-$8,000 (非 N85 假设的 $1020)，OpEx 取 100W 功耗 × 26280h × $0.15/kWh ≈ $394，3 年总成本约 $6,400-$8,400。若吞吐量为 25 tokens/s，总生成 Token 数 = 25 × 3600 × 26280 ≈ 2.37B tokens，TCO/token ≈ $0.0027-$0.0035，低于 $0.0075 阈值，但前提是硬件成本按实际零售价而非折旧后残值计算。

## Corrected Claim

Apple M3 Ultra 方案的修正 TCO 计算：CapEx 取 Mac Studio M3 Ultra 512GB 配置约 $6,000-$8,000 (非 N85 假设的 $1020)，OpEx 取 100W 功耗 × 26280h × $0.15/kWh ≈ $394，3 年总成本约 $6,400-$8,400。若吞吐量为 25 tokens/s，总生成 Token 数 = 25 × 3600 × 26280 ≈ 2.37B tokens，TCO/token ≈ $0.0027-$0.0035，低于 $0.0075 阈值，但前提是硬件成本按实际零售价而非折旧后残值计算。

## Evidence

先验知识/题面给定，逻辑校验通过：CapEx区间合理，OpEx计算(100W*26280h*0.15/kWh≈394)准确，Token总量(25*3600*26280≈2.37B)及TCO/token推导符合算术逻辑。
