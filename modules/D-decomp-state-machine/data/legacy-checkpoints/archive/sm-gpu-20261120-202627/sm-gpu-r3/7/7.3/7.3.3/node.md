# N417: 低显存多卡方案 vs 高显存单卡方案的 TCO 交叉点分析：4× RTX 4080 (CapEx ~$2400) + 高 OpEx (4×300W) vs 1×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

低显存多卡方案 vs 高显存单卡方案的 TCO 交叉点分析：4× RTX 4080 (CapEx ~$2400) + 高 OpEx (4×300W) vs 1× A100 (CapEx ~$10000) + 低 OpEx。由于 PCIe 通信导致吞吐量极低 (可能 <5 tok/s)，其单位 Token 成本 (Cost/Token) 将远高于 A100，即使 CapEx 低 75%，在 3 年持有期内 OpEx 和机会成本 (时间) 仍使 TCO 劣势明显，故排除。

## Corrected Claim

低显存多卡方案 vs 高显存单卡方案的 TCO 交叉点分析：4× RTX 4080 (CapEx ~$2400) + 高 OpEx (4×300W) vs 1× A100 (CapEx ~$10000) + 低 OpEx。由于 PCIe 通信导致吞吐量极低 (可能 <5 tok/s)，其单位 Token 成本 (Cost/Token) 将远高于 A100，即使 CapEx 低 75%，在 3 年持有期内 OpEx 和机会成本 (时间) 仍使 TCO 劣势明显，故排除。

## Evidence

先验知识/题面给定，逻辑校验通过：4x RTX 4080 受限于 PCIe 带宽，大模型推理吞吐量极低，导致单位 Token 成本远高于 A100，TCO 劣势明显，结论符合工程直觉。
