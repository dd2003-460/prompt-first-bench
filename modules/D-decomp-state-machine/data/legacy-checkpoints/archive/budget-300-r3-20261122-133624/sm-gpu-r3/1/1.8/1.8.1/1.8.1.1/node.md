# N235: 修正系数错误：Qwen3-27B 在 INT8 下 Prefill 每生成 1 token 的计算量为 2 × 27B × 1 = 54 GFLOPs (0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

修正系数错误：Qwen3-27B 在 INT8 下 Prefill 每生成 1 token 的计算量为 2 × 27B × 1 = 54 GFLOPs (0.054 TFLOPS)，而非 270 TOPS；原 N13 的 135 TOPS 可能是误用了 BF16 字节数或参数计数错误。

## Corrected Claim

修正系数错误：Qwen3-27B 在 INT8 下 Prefill 每生成 1 token 的计算量为 2 × 27B × 1 = 54 GFLOPs (0.054 TFLOPS)，而非 270 TOPS；原 N13 的 135 TOPS 可能是误用了 BF16 字节数或参数计数错误。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算量公式为 2 * 参数量 * 序列长度，2 * 27e9 * 1 = 54e9 FLOPs = 54 GFLOPs，量纲与数值推导正确。
