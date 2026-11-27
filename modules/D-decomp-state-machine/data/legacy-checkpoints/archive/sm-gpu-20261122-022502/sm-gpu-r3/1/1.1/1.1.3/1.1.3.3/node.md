# N113: CPU Offload 的交互效应：Offload 不仅增加延迟，还导致 PCIe 总线拥塞，可能降低 GPU 内部计算效率 (SM 利用率下降 10-20%)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

CPU Offload 的交互效应：Offload 不仅增加延迟，还导致 PCIe 总线拥塞，可能降低 GPU 内部计算效率 (SM 利用率下降 10-20%)，进一步恶化吞吐量，使得实际 tokens/s 低于纯带宽限制模型预测值

## Corrected Claim

CPU Offload 的交互效应：Offload 不仅增加延迟，还导致 PCIe 总线拥塞，可能降低 GPU 内部计算效率 (SM 利用率下降 10-20%)，进一步恶化吞吐量，使得实际 tokens/s 低于纯带宽限制模型预测值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CPU offload LLM inference performance degradation PCIe bottleneck
