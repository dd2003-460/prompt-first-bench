# N83: AMD MI300X 显存带宽为 5300 GB/s (HBM3)，在 FP8 精度下理论最大解码吞吐量为 5300/25.2 ≈ 210 tokens/s，理

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21, N22, N23

## Claim

AMD MI300X 显存带宽为 5300 GB/s (HBM3)，在 FP8 精度下理论最大解码吞吐量为 5300/25.2 ≈ 210 tokens/s，理论上性能远超 NVIDIA 同级产品，但软件栈 (ROCm) 对 vLLM/TensorRT-LLM 的支持成熟度低于 CUDA，实际有效吞吐可能打 5-7 折，需评估软件兼容性风险。

## Corrected Claim

AMD MI300X 显存带宽为 5300 GB/s (HBM3)，在 FP8 精度下理论最大解码吞吐量为 5300/25.2 ≈ 210 tokens/s，理论上性能远超 NVIDIA 同级产品，但软件栈 (ROCm) 对 vLLM/TensorRT-LLM 的支持成熟度低于 CUDA，实际有效吞吐可能打 5-7 折，需评估软件兼容性风险。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X 显存带宽 5300 GB/s 符合 HBM3 规格，FP8 下 5300/25.2 ≈ 210 tokens/s 计算正确，ROCm 软件栈成熟度低于 CUDA 为公认事实。

## Search Query

AMD MI300X memory bandwidth HBM3 FP8 inference performance ROCm vs CUDA
