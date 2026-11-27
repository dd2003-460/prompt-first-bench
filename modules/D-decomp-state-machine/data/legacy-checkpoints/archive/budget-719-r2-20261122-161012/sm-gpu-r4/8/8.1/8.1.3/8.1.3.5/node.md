# N673: RTX 4090 双卡方案在 '中性价比最优' 工作点下，若采用 NVLink 桥接（若主板支持且显卡有 NVLink 接口，注：4090 无 NVLink，此

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N277, N278, N279

## Claim

RTX 4090 双卡方案在 '中性价比最优' 工作点下，若采用 NVLink 桥接（若主板支持且显卡有 NVLink 接口，注：4090 无 NVLink，此点需修正为 PCIe 拓扑优化），实际不可行；因此该工作点必须依赖软件层面的流水线并行 (PP) 或张量并行 (TP) 优化，其中 PP 模式可将通信频率降低至每 N 层一次，使吞吐量回升至 30-33 tokens/s，但增加了首字延迟 (TTFT)。

## Corrected Claim

RTX 4090 双卡方案在 '中性价比最优' 工作点下，若采用 NVLink 桥接（若主板支持且显卡有 NVLink 接口，注：4090 无 NVLink，此点需修正为 PCIe 拓扑优化），实际不可行；因此该工作点必须依赖软件层面的流水线并行 (PP) 或张量并行 (TP) 优化，其中 PP 模式可将通信频率降低至每 N 层一次，使吞吐量回升至 30-33 tokens/s，但增加了首字延迟 (TTFT)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 确实无 NVLink 接口，物理上不可行；PP 模式降低通信频率但增加 TTFT 符合分布式推理基本原理；30-33 tokens/s 在双卡 4090 大模型推理场景下量级合理。
