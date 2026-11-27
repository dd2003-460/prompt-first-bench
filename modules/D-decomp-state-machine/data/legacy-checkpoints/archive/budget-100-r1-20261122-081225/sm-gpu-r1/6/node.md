# N49: NVIDIA RTX 4090 在运行 Qwen3-27B (W4A16, 32K ctx) 时的实测推理吞吐约为 15-20 tokens/s (prefil

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA RTX 4090 在运行 Qwen3-27B (W4A16, 32K ctx) 时的实测推理吞吐约为 15-20 tokens/s (prefill 阶段受限于内存带宽，decode 阶段受限于算力与显存访问)，而 H100 在相同配置下约为 100-150 tokens/s。

## Corrected Claim

NVIDIA RTX 4090 在运行 Qwen3-27B (W4A16, 32K ctx) 时的实测推理吞吐显著低于 H100，具体数值需参考更多基准测试数据。

## Evidence

[质询]参考来源仅提及在 RTX 4090 上运行 Qwen3.8-27B，未提供具体的吞吐数值（15-20 tokens/s），也未提供 H100 的对比数据，无法直接验证具体数值量级。 | 来源 [1] 确认了 RTX 4090 可运行该模型，但缺乏具体性能指标支持；逻辑上 4090 与 H100 的性能差距符合硬件规格差异，但具体数值缺乏直接证据。

## Retrieval Sources

- {'url': 'https://github.com/sergiuszm/ninfer-4090&rut=7e5cfcd5fcaf3213eaab405c24e99d7efaf49593ba2f715140ed1fe7b3fbcd68', 'type': 'ddg', 'title': 'GitHub - sergiuszm/ninfer-4090: Qwen3.8-27B on one RTX 4090: full ...'}
