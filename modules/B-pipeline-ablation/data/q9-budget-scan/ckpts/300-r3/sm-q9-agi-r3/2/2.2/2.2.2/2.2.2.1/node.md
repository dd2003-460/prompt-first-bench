# N190: V100-SXM2-16GB 的 FP16 峰值算力为 15.7 TFLOPS (Tensor Core)，但混合精度训练/推理中实际可达利用率通常为 40%-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

V100-SXM2-16GB 的 FP16 峰值算力为 15.7 TFLOPS (Tensor Core)，但混合精度训练/推理中实际可达利用率通常为 40%-60%，取保守值 40% 计算，单卡有效算力为 15.7e12 * 0.4 = 6.28e12 FLOPs/s

## Corrected Claim

V100-SXM2-16GB 的 FP16 峰值算力为 15.7 TFLOPS (Tensor Core)，但混合精度训练/推理中实际可达利用率通常为 40%-60%，取保守值 40% 计算，单卡有效算力为 15.7e12 * 0.4 = 6.28e12 FLOPs/s

## Evidence

先验知识/题面给定，逻辑校验通过：V100 Tensor Core FP16 峰值算力确为 15.7 TFLOPS，40% 利用率下的算术运算正确（15.7 * 0.4 = 6.28），符合工程常识。
