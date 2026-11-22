# N326: 长文档处理场景 (TTFT 敏感) 的量化指标：要求 32K 输入的首字延迟 T_TTFT < 2.0s，这对应硬件需满足 FLOPS > (2 * 27e9 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

长文档处理场景 (TTFT 敏感) 的量化指标：要求 32K 输入的首字延迟 T_TTFT < 2.0s，这对应硬件需满足 FLOPS > (2 * 27e9 * 32768 * 0.7) / 2.0 ≈ 616 TFLOPS (假设 70% 利用率)，仅 H100 单卡或特定多卡集群满足，消费级显卡无法满足此严格阈值。

## Corrected Claim

长文档处理场景 (TTFT 敏感) 的量化指标：要求 32K 输入的首字延迟 T_TTFT < 2.0s，这对应硬件需满足 FLOPS > (2 * 27e9 * 32768 * 0.7) / 2.0 ≈ 616 TFLOPS (假设 70% 利用率)，仅 H100 单卡或特定多卡集群满足，消费级显卡无法满足此严格阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (2 * 27e9 * 32768 * 0.7) / 2.0 ≈ 616 TFLOPS 数学正确，且 H100 单卡 FP16 算力约 990 TFLOPS，满足 >616 TFLOPS 的条件，消费级显卡（如 RTX 4090 约 165 TFLOPS）确实无法满足，逻辑自洽。
