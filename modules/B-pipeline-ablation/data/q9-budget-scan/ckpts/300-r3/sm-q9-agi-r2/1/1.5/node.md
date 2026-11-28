# N11: M1 Max的GPU峰值算力为13.6 TFLOPS (FP16)，CPU为10-core (8P+2E)，统一内存带宽400GB/s，但其缺乏CUDA生态支持

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

M1 Max的GPU峰值算力为13.6 TFLOPS (FP16)，CPU为10-core (8P+2E)，统一内存带宽400GB/s，但其缺乏CUDA生态支持，无法运行vLLM或PyTorch CUDA后端，仅能承担轻量级Python编排、JSON解析及API调用任务

## Corrected Claim

M1 Max的GPU峰值算力为13.6 TFLOPS (FP16)，CPU为10-core (8P+2E)，统一内存带宽400GB/s，但其缺乏CUDA生态支持，无法运行vLLM或PyTorch CUDA后端，仅能承担轻量级Python编排、JSON解析及API调用任务

## Evidence

先验知识/题面给定，逻辑校验通过
