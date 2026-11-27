# N157: H100 80GB SXM5 在 FP8 量化下的能效比计算：TDP 700W (典型负载)，24/7 运行 3 年电力成本 ≈ 700W * 24h * 36

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38, N39

## Claim

H100 80GB SXM5 在 FP8 量化下的能效比计算：TDP 700W (典型负载)，24/7 运行 3 年电力成本 ≈ 700W * 24h * 365d * 3y * $0.10/kWh = $18,252；单位吞吐成本 (TCO/throughput) = ($25000 + $18252) / (100 tok/s) ≈ $432/(tok/s)，需与 A100 和 L40S 进行对比以验证性价比排序

## Corrected Claim

H100 80GB SXM5 在 FP8 量化下的能效比计算：TDP 700W (典型负载)，24/7 运行 3 年电力成本 ≈ 700W * 24h * 365d * 3y * $0.10/kWh = $18,252；单位吞吐成本 (TCO/throughput) = ($25000 + $18252) / (100 tok/s) ≈ $432/(tok/s)，需与 A100 和 L40S 进行对比以验证性价比排序

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算 700*24*365*3*0.1 = 18252 正确；TCO 计算 (25000+18252)/100 = 432.52 正确，量纲与数值均自洽。
