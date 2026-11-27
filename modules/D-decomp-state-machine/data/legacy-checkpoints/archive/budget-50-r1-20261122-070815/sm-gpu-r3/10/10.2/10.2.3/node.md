# N422: Ada 架构 FP8 模拟的性能损失比 L_loss = 1 - (Throughput_FP8_Sim / Throughput_BF16)，若 L_loss

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

Ada 架构 FP8 模拟的性能损失比 L_loss = 1 - (Throughput_FP8_Sim / Throughput_BF16)，若 L_loss 为负（即 FP8 更快），则验证了 N146 中'快42%'的说法；若 L_loss 为正（10-20%），则需分析 Ada Tensor Core 对 FP8 的模拟开销（dequantize 成本）是否超过了内存带宽节省的收益。

## Corrected Claim

Ada 架构 FP8 模拟的性能损失比 L_loss = 1 - (Throughput_FP8_Sim / Throughput_BF16)，若 L_loss 为负（即 FP8 更快），则验证了 N146 中'快42%'的说法；若 L_loss 为正（10-20%），则需分析 Ada Tensor Core 对 FP8 的模拟开销（dequantize 成本）是否超过了内存带宽节省的收益。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义与性能分析逻辑自洽，且符合Ada架构不支持原生FP8需模拟的技术事实。
