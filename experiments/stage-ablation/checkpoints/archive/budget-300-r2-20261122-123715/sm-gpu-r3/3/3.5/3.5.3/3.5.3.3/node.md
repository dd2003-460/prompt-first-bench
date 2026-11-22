# N284: 多卡 PCIe 互联下的稳定性风险量化：PCIe 链路在长时间高负载下可能出现链路降速 (Link Retrain) 或 CRC 错误，导致推理中断。假设 3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

多卡 PCIe 互联下的稳定性风险量化：PCIe 链路在长时间高负载下可能出现链路降速 (Link Retrain) 或 CRC 错误，导致推理中断。假设 3 年内 PCIe 链路故障概率 P_pcie_fail = 0.05 (基于服务器运维经验值，需核验)，每次故障平均修复时间 MTTR = 4 小时，则额外停机成本 C_downtime_pcie = P_pcie_fail * MTTR * 时薪 * 3年。

## Corrected Claim

多卡 PCIe 互联下的稳定性风险量化：PCIe 链路在长时间高负载下可能出现链路降速 (Link Retrain) 或 CRC 错误，导致推理中断。假设 3 年内 PCIe 链路故障概率 P_pcie_fail = 0.05 (基于服务器运维经验值，需核验)，每次故障平均修复时间 MTTR = 4 小时，则额外停机成本 C_downtime_pcie = P_pcie_fail * MTTR * 时薪 * 3年。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PCIe link retrain failure rate high load GPU inference downtime
