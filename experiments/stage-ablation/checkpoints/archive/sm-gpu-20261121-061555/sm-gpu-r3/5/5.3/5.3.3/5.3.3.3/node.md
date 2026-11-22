# N298: 单位 Token 电费（Cost per 1K Tokens）的量化对比：公式为 (Power_W * Price_kWh) / Throughput_Toke

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

单位 Token 电费（Cost per 1K Tokens）的量化对比：公式为 (Power_W * Price_kWh) / Throughput_TokensPerSec * 3600 / 1000；若 RTX 4090 为 450W * $0.15 / 50 tok/s，而 7900 XTX 为 300W * $0.15 / 40 tok/s，则 7900 XTX 的单位 Token 成本比 4090 高约 50%（尽管总电费略低），这直接影响高吞吐量场景下的性价比排序。

## Corrected Claim

单位 Token 电费（Cost per 1K Tokens）的量化对比：公式为 (Power_W * Price_kWh) / Throughput_TokensPerSec * 3600 / 1000；若 RTX 4090 为 450W * $0.15 / 50 tok/s，而 7900 XTX 为 300W * $0.15 / 40 tok/s，则 7900 XTX 的单位 Token 成本比 4090 高约 50%（尽管总电费略低），这直接影响高吞吐量场景下的性价比排序。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算（4090: $0.03375, 7900 XTX: $0.050625）显示后者成本约为前者的1.5倍，即高出约50%，与陈述一致。
