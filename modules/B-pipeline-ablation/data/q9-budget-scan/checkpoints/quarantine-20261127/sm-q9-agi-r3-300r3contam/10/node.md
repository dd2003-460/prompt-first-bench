# N254: Tesla V100-SXM2 单卡 FP16 峰值算力为 15.7 TFLOPS，FP32 为 15.7 TFLOPS，Tensor Core FP16 为 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Tesla V100-SXM2 单卡 FP16 峰值算力为 15.7 TFLOPS，FP32 为 15.7 TFLOPS，Tensor Core FP16 为 125 TFLOPS；在 4 卡 TP=4 架构下，理论峰值聚合算力为 508 TFLOPS (FP16 Tensor Core)，但受 AllReduce 通信开销（N237, N242）及 NVFP4 反量化效率限制，实际有效算力利用率 (MFU) 预计仅在 15%-25% 之间，导致实际推理吞吐远低于理论上限。

## Corrected Claim

Tesla V100-SXM2 单卡 FP16 峰值算力为 15.7 TFLOPS，FP32 为 15.7 TFLOPS，Tensor Core FP16 为 125 TFLOPS；在 4 卡 TP=4 架构下，理论峰值聚合算力为 508 TFLOPS (FP16 Tensor Core)，但受 AllReduce 通信开销（N237, N242）及 NVFP4 反量化效率限制，实际有效算力利用率 (MFU) 预计仅在 15%-25% 之间，导致实际推理吞吐远低于理论上限。

## Evidence

检索失败: no sources from any channel (all 5 failed)
