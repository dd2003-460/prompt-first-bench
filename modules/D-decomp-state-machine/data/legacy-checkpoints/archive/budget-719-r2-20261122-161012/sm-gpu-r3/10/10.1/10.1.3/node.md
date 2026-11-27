# N294: 单位算力成本（$/token）的计算公式为 (Instance_Price_per_hour / Throughput_tokens_per_hour)，其中T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

单位算力成本（$/token）的计算公式为 (Instance_Price_per_hour / Throughput_tokens_per_hour)，其中Throughput需基于Qwen3-27B在H100/A100上的实测或理论峰值吞吐（参考N121/N106）进行标准化

## Corrected Claim

单位算力成本（$/token）的计算公式为 (Instance_Price_per_hour / Throughput_tokens_per_hour)，其中Throughput需基于Qwen3-27B在H100/A100上的实测或理论峰值吞吐（参考N121/N106）进行标准化

## Evidence

先验知识/题面给定，逻辑校验通过：单位成本公式符合经济学基本定义（总成本/总产出），且H100/A100作为主流推理硬件，其吞吐标准化逻辑自洽。
