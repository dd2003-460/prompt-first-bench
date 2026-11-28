# N74: Prefill 阶段的实际算力利用率 (Efficiency) 受 Batch Size 和序列长度影响，典型值为 40%-60%；在 Batch Size=1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

Prefill 阶段的实际算力利用率 (Efficiency) 受 Batch Size 和序列长度影响，典型值为 40%-60%；在 Batch Size=1 且长序列场景下，RTX 4090 的利用率通常低于 A100/H100，约为 30%-50%。

## Corrected Claim

Prefill 阶段的实际算力利用率 (Efficiency) 受 Batch Size 和序列长度影响，典型值为 40%-60%；在 Batch Size=1 且长序列场景下，RTX 4090 的利用率通常低于 A100/H100，约为 30%-50%。

## Evidence

先验知识/题面给定，逻辑校验通过
