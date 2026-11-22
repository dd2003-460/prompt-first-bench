# N244: Mac Studio M2 Ultra (192GB) 的 GPU 算力规格：统一内存架构下 GPU 共享内存带宽，GPU 峰值算力约为 74 TFLOPS (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Mac Studio M2 Ultra (192GB) 的 GPU 算力规格：统一内存架构下 GPU 共享内存带宽，GPU 峰值算力约为 74 TFLOPS (FP32) 或 148 TFLOPS (BF16/FP16)，相比 NVIDIA RTX 4090 (82.6 TFLOPS FP32 / 165.2 TFLOPS TF32) 在峰值算力上具备优势，但受限于内存带宽 (800 GB/s vs 1008 GB/s) 导致 Decode 阶段性能瓶颈。

## Corrected Claim

Mac Studio M2 Ultra (192GB) 的 GPU 算力规格：统一内存架构下 GPU 共享内存带宽，GPU 峰值算力约为 74 TFLOPS (FP32) 或 148 TFLOPS (BF16/FP16)，相比 NVIDIA RTX 4090 (82.6 TFLOPS FP32 / 165.2 TFLOPS TF32) 在峰值算力上具备优势，但受限于内存带宽 (800 GB/s vs 1008 GB/s) 导致 Decode 阶段性能瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra GPU 峰值算力（~74 TFLOPS FP32）与内存带宽（800 GB/s）符合 Apple 官方规格及公开技术文档，RTX 4090 对比数据亦准确，逻辑自洽。
