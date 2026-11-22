# N367: 工作点 C（低吞吐/高延迟容忍）：假设 Batch Size=1 且序列长度 32K，Throughput_PCIe 降至 15 tokens/s (下降 62

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115

## Claim

工作点 C（低吞吐/高延迟容忍）：假设 Batch Size=1 且序列长度 32K，Throughput_PCIe 降至 15 tokens/s (下降 62.5%)。代入 N115 公式，隐性成本增加 = (40-15)/40 × (OpEx_per_hour + CapEx_annualized/8760)。此极端情况用于评估在长上下文低并发场景下，PCIe 瓶颈是否使 2×4090 方案完全不可行（隐性成本超过 CapEx 节省额）。

## Corrected Claim

工作点 C（低吞吐/高延迟容忍）：假设 Batch Size=1 且序列长度 32K，Throughput_PCIe 降至 15 tokens/s (下降 62.5%)。代入 N115 公式，隐性成本增加 = (40-15)/40 × (OpEx_per_hour + CapEx_annualized/8760)。此极端情况用于评估在长上下文低并发场景下，PCIe 瓶颈是否使 2×4090 方案完全不可行（隐性成本超过 CapEx 节省额）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算（(40-15)/40=62.5%）准确，公式结构符合成本效益分析逻辑，作为假设性极端场景的评估框架自洽。
