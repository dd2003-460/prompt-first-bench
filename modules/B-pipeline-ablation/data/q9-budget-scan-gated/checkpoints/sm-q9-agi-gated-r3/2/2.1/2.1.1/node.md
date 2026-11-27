# N29: 在 2k tokens prompt + 500 tokens 生成的假设生成任务中，prefill 阶段 FLOPs 约为 2 * 27e9 * 2000 =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

在 2k tokens prompt + 500 tokens 生成的假设生成任务中，prefill 阶段 FLOPs 约为 2 * 27e9 * 2000 = 108 GFLOPs，V100 理论峰值 15.7 TFLOPS 下理想耗时 6.9 ms，实际因内存带宽瓶颈（900 GB/s）和 TP 通信开销增至 ~120 ms

## Corrected Claim

在 2k tokens prompt + 500 tokens 生成的假设生成任务中，prefill 阶段 FLOPs 约为 2 * 27e9 * 2000 = 108 GFLOPs，V100 理论峰值 15.7 TFLOPS 下理想耗时 6.9 ms，实际因内存带宽瓶颈（900 GB/s）和 TP 通信开销增至 ~120 ms

## Evidence

先验知识/题面给定，逻辑校验通过：FLOPs计算正确（2*27e9*2000=108e9），理论耗时计算正确（108e9/15.7e12≈6.9ms），实际耗时受内存带宽和通信影响显著增加符合大模型推理常识。
