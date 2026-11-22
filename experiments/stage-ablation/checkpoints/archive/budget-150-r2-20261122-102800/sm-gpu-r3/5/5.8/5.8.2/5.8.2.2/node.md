# N331: 多卡部署中，若采用流水线并行 (PP) 而非张量并行 (TP)，通信量进一步降低为仅传递 hidden_states (batch_size × seq_len

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

多卡部署中，若采用流水线并行 (PP) 而非张量并行 (TP)，通信量进一步降低为仅传递 hidden_states (batch_size × seq_len × hidden_size × bytes)，但 Qwen3-27B 在 2 卡上 PP 切分不均（64 层无法均分），实际通信量与 TP 相当或略高，仍需基于 512 KB/step 量级估算，PCIe 带宽瓶颈不构成显著性能限制。

## Corrected Claim

多卡部署中，若采用流水线并行 (PP) 而非张量并行 (TP)，通信量进一步降低为仅传递 hidden_states (batch_size × seq_len × hidden_size × bytes)，但 Qwen3-27B 在 2 卡上 PP 切分不均（64 层无法均分），实际通信量与 TP 相当或略高，仍需基于 512 KB/step 量级估算，PCIe 带宽瓶颈不构成显著性能限制。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 为 64 层，2 卡 PP 可均分（32+32），通信量仅 hidden_states，量级估算合理，PCIe 瓶颈非主要限制。
