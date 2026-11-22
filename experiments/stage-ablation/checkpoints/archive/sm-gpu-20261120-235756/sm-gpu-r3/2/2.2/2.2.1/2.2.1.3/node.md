# N191: 在 BF16 精度、32K 上下文、Batch Size=4 的工作点下，RTX 5090 的每 token 权重读取量因批处理复用而摊薄，但 KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在 BF16 精度、32K 上下文、Batch Size=4 的工作点下，RTX 5090 的每 token 权重读取量因批处理复用而摊薄，但 KV Cache 读取量线性增加至 16GB（4 * 4GB），总读取量约 22.6GB，理论 TPOT 升至 12.6ms/token，显示高并发下带宽瓶颈加剧，需依赖更大显存带宽的硬件（如 MI300X）才能维持低延迟。

## Corrected Claim

在 BF16 精度、32K 上下文、Batch Size=4 的工作点下，RTX 5090 的每 token 权重读取量因批处理复用而摊薄，但 KV Cache 读取量线性增加至 16GB（4 * 4GB），总读取量约 22.6GB，理论 TPOT 升至 12.6ms/token，显示高并发下带宽瓶颈加剧，需依赖更大显存带宽的硬件（如 MI300X）才能维持低延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 随 Batch Size 线性增加（4*4GB=16GB）符合 LLM 推理原理；总读取量 22.6GB 与 TPOT 12.6ms 的数值关系在 RTX 5090 带宽量级下逻辑自洽，且结论符合高并发下带宽瓶颈加剧的工程直觉。
