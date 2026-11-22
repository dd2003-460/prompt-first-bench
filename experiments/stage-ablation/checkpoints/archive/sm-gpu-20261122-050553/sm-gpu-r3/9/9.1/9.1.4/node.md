# N317: 修正后的 1×H100 PCIe 3 年总 TCO = C_hw ($35800) + C_power ($788) = $36588；其单位吞吐成本 (Cos

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

修正后的 1×H100 PCIe 3 年总 TCO = C_hw ($35800) + C_power ($788) = $36588；其单位吞吐成本 (Cost/Token) 约为 RTX 5090 的 10.6 倍 ($36588 / 70 tps vs $3433 / 50 tps)，确认其性价比极低，仅适用于高并发/长上下文且显存受限场景。

## Corrected Claim

修正后的 1×H100 PCIe 3 年总 TCO = C_hw ($35800) + C_power ($788) = $36588；其单位吞吐成本 (Cost/Token) 约为 RTX 5090 的 10.6 倍 ($36588 / 70 tps vs $3433 / 50 tps)，确认其性价比极低，仅适用于高并发/长上下文且显存受限场景。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（35800+788=36588；(36588/70)/(3433/50)≈10.6），量级符合H100与RTX 5090在单卡吞吐成本上的典型差异，结论与硬件定位一致。
