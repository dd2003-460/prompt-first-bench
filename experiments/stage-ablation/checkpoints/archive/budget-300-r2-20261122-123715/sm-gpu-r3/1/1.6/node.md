# N10: 多卡互联带宽与延迟约束：PCIe 4.0 x16 带宽 ~32GB/s，NVLink 3.0 带宽 ~900GB/s；对于 2×24GB 消费卡方案，若需跨卡传

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

多卡互联带宽与延迟约束：PCIe 4.0 x16 带宽 ~32GB/s，NVLink 3.0 带宽 ~900GB/s；对于 2×24GB 消费卡方案，若需跨卡传输 KV Cache 或权重，PCIe 带宽可能成为瓶颈，需评估实际推理框架（如 vLLM, TensorRT-LLM）对多卡支持的效率损失。

## Corrected Claim

多卡互联带宽与延迟约束：PCIe 4.0 x16 带宽 ~32GB/s，NVLink 3.0 带宽 ~900GB/s；对于 2×24GB 消费卡方案，若需跨卡传输 KV Cache 或权重，PCIe 带宽可能成为瓶颈，需评估实际推理框架（如 vLLM, TensorRT-LLM）对多卡支持的效率损失。

## Evidence

[质询]NVLink 3.0 带宽数值存在歧义：通常指代 A100 的 NVLink 3.0 为 600GB/s，而 900GB/s 更接近 H100 的 NVLink 4.0 或特定聚合带宽，但作为量级对比（PCIe vs NVLink）的核心逻辑无误。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽约 32GB/s，NVLink 带宽远高于 PCIe（600-900GB/s 量级），多卡推理中跨卡通信确实受限于互联带宽，逻辑自洽。
