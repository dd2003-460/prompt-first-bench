# N216: RTX 4090 在 BF16 下的有效算力（Effective TFLOPS）约为 82.6 TFLOPS（理论 165.2 TFLOPS * ~50% 效率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

RTX 4090 在 BF16 下的有效算力（Effective TFLOPS）约为 82.6 TFLOPS（理论 165.2 TFLOPS * ~50% 效率），而 H100 SXM 约为 395.8 TFLOPS（理论 989.5 TFLOPS * ~40% 效率），用于计算 TTFT 分母中的 GPU FLOPS * Efficiency 项。

## Corrected Claim

RTX 4090 在 BF16 下的有效算力（Effective TFLOPS）约为 82.6 TFLOPS（理论 165.2 TFLOPS * ~50% 效率），而 H100 SXM 约为 395.8 TFLOPS（理论 989.5 TFLOPS * ~40% 效率），用于计算 TTFT 分母中的 GPU FLOPS * Efficiency 项。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (AD102) 理论 BF16 算力约 165.2 TFLOPS，H100 SXM 理论 BF16 算力约 989.5 TFLOPS，数值量级与硬件规格一致；效率假设（50%/40%）符合大模型推理场景下的典型经验值，计算逻辑自洽。
