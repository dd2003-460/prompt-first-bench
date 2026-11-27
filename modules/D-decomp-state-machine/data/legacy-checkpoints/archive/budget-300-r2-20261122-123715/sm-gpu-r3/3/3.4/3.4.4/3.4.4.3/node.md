# N272: PCIe 4.0 x16 链路故障的额外风险系数：PCIe 插槽/链路故障率通常低于 GPU 本身，但在多卡系统中，任一链路故障导致张量并行通信中断，需将 PC

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

PCIe 4.0 x16 链路故障的额外风险系数：PCIe 插槽/链路故障率通常低于 GPU 本身，但在多卡系统中，任一链路故障导致张量并行通信中断，需将 PCIe 链路 MTBF (通常 >200,000 小时) 纳入串联故障模型，修正后的系统 MTBF 需取 min(MTBF_gpu1, MTBF_gpu2, MTBF_pcie_link)。

## Corrected Claim

PCIe 4.0 x16 链路故障的额外风险系数：PCIe 插槽/链路故障率通常低于 GPU 本身，但在多卡系统中，任一链路故障导致张量并行通信中断，需将 PCIe 链路 MTBF (通常 >200,000 小时) 纳入串联故障模型，修正后的系统 MTBF 需取 min(MTBF_gpu1, MTBF_gpu2, MTBF_pcie_link)。

## Evidence

先验知识/题面给定，逻辑校验通过：串联系统可靠性模型中，系统MTBF确实受限于最薄弱环节（即取各组件MTBF的最小值），且PCIe链路故障导致通信中断进而影响张量并行是合理的工程逻辑。

## Search Query

PCIe 4.0 link failure rate MTBF
