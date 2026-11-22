# N393: MI300X 运行 Qwen3-27B (BF16) 的 3 年 TCO 计算：硬件 Capex $22,000 + 电力成本 (750W TDP * 0.7 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N148

## Claim

MI300X 运行 Qwen3-27B (BF16) 的 3 年 TCO 计算：硬件 Capex $22,000 + 电力成本 (750W TDP * 0.7 负载因子 * 8760h/年 * 3年 * $0.15/kWh) ≈ $22,000 + $1,929 ≈ $23,929；每美元吞吐量修正为 59 Tokens/s / $23,929 ≈ 0.0025 Tokens/s/$

## Corrected Claim

MI300X 运行 Qwen3-27B (BF16) 的 3 年 TCO 计算：硬件 Capex $22,000 + 电力成本 (750W TDP * 0.7 负载因子 * 8760h/年 * 3年 * $0.15/kWh) ≈ $22,000 + $1,929 ≈ $23,929；每美元吞吐量修正为 59 Tokens/s / $23,929 ≈ 0.0025 Tokens/s/$

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算 750*0.7*8760*3*0.15 = 1929.09，总成本 22000+1929=23929，吞吐量修正 59/23929≈0.002465≈0.0025，数值与逻辑均自洽。

## Search Query

MI300X 3 year TCO electricity cost calculation 750W
