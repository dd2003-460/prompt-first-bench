# N311: 吞吐量公式的修正项：实际吞吐量 = 理论带宽上限 / (1 + Communication_Overhead_Ratio)，其中 Communication_O

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

吞吐量公式的修正项：实际吞吐量 = 理论带宽上限 / (1 + Communication_Overhead_Ratio)，其中 Communication_Overhead_Ratio = (AllReduce_Size_per_token / PCIe_Bandwidth) / (Weight_Size / Memory_Bandwidth)，用于量化互联带宽对整体吞吐的折损

## Corrected Claim

吞吐量公式的修正项：实际吞吐量 = 理论带宽上限 / (1 + Communication_Overhead_Ratio)，其中 Communication_Overhead_Ratio = (AllReduce_Size_per_token / PCIe_Bandwidth) / (Weight_Size / Memory_Bandwidth)，用于量化互联带宽对整体吞吐的折损

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PCIe vs NVLink impact on LLM inference throughput latency
