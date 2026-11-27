# N18: 多卡并行效率损失 (Multi-GPU Efficiency Loss)：在 2× 消费卡方案中，由于 PCIe 带宽限制或 NVLink 缺失，All-Red

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

多卡并行效率损失 (Multi-GPU Efficiency Loss)：在 2× 消费卡方案中，由于 PCIe 带宽限制或 NVLink 缺失，All-Reduce 通信开销会导致实际吞吐量低于理论线性加速比，需量化通信延迟对整体 TCO 的影响

## Corrected Claim

多卡并行效率损失 (Multi-GPU Efficiency Loss)：在 2× 消费卡方案中，由于 PCIe 带宽限制或 NVLink 缺失，All-Reduce 通信开销会导致实际吞吐量低于理论线性加速比，需量化通信延迟对整体 TCO 的影响

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 944)
