# N413: Loss_Rate 的量化分解：Loss_Rate = 1 - (Throughput_Pcie / Throughput_Nvlink)，其中 Through

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

Loss_Rate 的量化分解：Loss_Rate = 1 - (Throughput_Pcie / Throughput_Nvlink)，其中 Throughput_Nvlink 基于 H100 实测 tokens/s，Throughput_Pcie 基于 2×4090 实测 tokens/s，该比值直接决定等效 TCO 修正系数 1/(1-Loss_Rate) 的数值。

## Corrected Claim

Loss_Rate 的量化分解：Loss_Rate = 1 - (Throughput_Pcie / Throughput_Nvlink)，其中 Throughput_Nvlink 基于 H100 实测 tokens/s，Throughput_Pcie 基于 2×4090 实测 tokens/s，该比值直接决定等效 TCO 修正系数 1/(1-Loss_Rate) 的数值。

## Evidence

先验知识/题面给定，逻辑校验通过：Loss_Rate 定义为 1 - (实际吞吐/理想吞吐)，TCO 修正系数为 1/(1-Loss_Rate)，数学关系自洽且符合性能损耗与成本修正的基本逻辑。
