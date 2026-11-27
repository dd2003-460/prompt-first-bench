# N311: H100 80GB 在 128K 上下文下的 TCO 交叉点计算：CapEx = $25,000 + $5,000 (配套) = $30,000，年 OpEx 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110, N111, N112

## Claim

H100 80GB 在 128K 上下文下的 TCO 交叉点计算：CapEx = $25,000 + $5,000 (配套) = $30,000，年 OpEx = 700W * 8760h * $0.10/kWh = $6,132；对比 2x 4090 方案 (CapEx $5,198, OpEx $7,884)，TCO 交叉点 t = (30000-5198)/(7884-6132) ≈ 14.16 年，表明在 14 年内 H100 方案 TCO 显著更高，仅适用于高吞吐量或低延迟敏感场景。

## Corrected Claim

H100 80GB 在 128K 上下文下的 TCO 交叉点计算：CapEx = $25,000 + $5,000 (配套) = $30,000，年 OpEx = 700W * 8760h * $0.10/kWh = $6,132；对比 2x 4090 方案 (CapEx $5,198, OpEx $7,884)，TCO 交叉点 t = (30000-5198)/(7884-6132) ≈ 14.16 年，表明在 14 年内 H100 方案 TCO 显著更高，仅适用于高吞吐量或低延迟敏感场景。

## Evidence

先验知识/题面给定，逻辑校验通过：CapEx与OpEx数值量级符合H100及4090硬件市场常识，TCO交叉点计算公式及算术推导（(30000-5198)/(7884-6132)≈14.16）逻辑自洽且无内部矛盾。

## Search Query

H100 vs RTX 4090 TCO crossover point 128k context
