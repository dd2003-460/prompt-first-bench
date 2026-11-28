# N63: 2x RTX 3090 用于张量并行 (TP) 推理 27B 模型时，由于 PCIe 4.0 x16 互联带宽 (32 GB/s) 远低于 HBM2e 带宽 (

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

2x RTX 3090 用于张量并行 (TP) 推理 27B 模型时，由于 PCIe 4.0 x16 互联带宽 (32 GB/s) 远低于 HBM2e 带宽 (936 GB/s)，每次 All-Reduce 操作的通信延迟约为 0.5-1 ms/layer，导致整体吞吐量相比单卡理论值下降 15-30%，从而推高了每 Token 的有效成本。

## Corrected Claim

2x RTX 3090 用于张量并行 (TP) 推理 27B 模型时，由于 PCIe 4.0 x16 互联带宽 (32 GB/s) 远低于 HBM2e 带宽 (936 GB/s)，All-Reduce 操作会产生显著通信开销，导致整体吞吐量相比理想情况有明显下降，从而推高了每 Token 的有效成本。

## Evidence

[质询]具体数值（0.5-1 ms/layer 延迟、15-30% 吞吐量下降）缺乏直接来源支持，且不同模型架构和批处理大小下波动较大，属于经验性估算而非固定常数。 | 来源 [1][2][3] 确认 PCIe 带宽远低于 NVLink/HBM 且 TP 在 PCIe 上效率低于 PP，支持定性结论，但未提供具体的 ms/layer 延迟或百分比下降数据，故降级为定性表述。

## Search Query

multi-GPU tensor parallelism PCIe bandwidth overhead LLM inference latency

## Retrieval Sources

- {'url': 'https://gigagpu.com/pcie-bandwidth-multi-gpu-inference/&rut=2cabe1647e487a7cccbdf0889377b92c046fe4fd906212d25f8f0ac5472866b5', 'type': 'ddg', 'title': 'PCIe Bandwidth: Multi-GPU Impact GIGAGPU'}
- {'url': 'https://runaihome.com/blog/multi-gpu-local-ai-nvlink-vs-pcie-2026/&rut=758fe6a7d3da98ff2d2eb6fc17a1b512134cb38f72f403f7e7e9e86ae0836b18', 'type': 'ddg', 'title': 'Dual GPU for Local AI in 2026: NVLink vs PCIe Bandwidth and Real tok/s ...'}
- {'url': 'https://gpusmith.com/articles/en/tensor-vs-pipeline-parallelism-inference-pcie-nvlink&rut=ef79898d6bb40df4c5aa6b0f5e946be5a3a7572d95c1dd89efcd8b0adfea64e3', 'type': 'ddg', 'title': 'Tensor vs Pipeline Parallelism for Inference: NVLink vs PCIe'}
