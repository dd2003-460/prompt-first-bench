# N12: 多卡互连带宽对推理的影响：PCIe 4.0 x16 单向 ~32 GB/s, NVLink (A100/H100) 单向 ~400-600 GB/s。单卡方案无

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

多卡互连带宽对推理的影响：PCIe 4.0 x16 单向 ~32 GB/s, NVLink (A100/H100) 单向 ~400-600 GB/s。单卡方案无需考虑张量并行通信开销；双卡方案需评估 all-reduce 延迟对 decode 吞吐的影响。

## Corrected Claim

多卡互连带宽对推理的影响：PCIe 4.0 x16 单向 ~32 GB/s, NVLink (A100/H100) 单向 ~400-600 GB/s。单卡方案无需考虑张量并行通信开销；双卡方案需评估 all-reduce 延迟对 decode 吞吐的影响。

## Evidence

[质询]NVLink 带宽数值范围（400-600 GB/s）可能混淆了不同代际（A100 为 600 GB/s，H100 为 900 GB/s）或单向/双向口径，但作为量级参考在工程估算中通常可接受。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽约 32 GB/s，NVLink 带宽远高于 PCIe，符合硬件规格常识及推理通信开销分析逻辑。

## Search Query

PCIe 4.0 bandwidth vs NVLink bandwidth LLM inference tensor parallel overhead
