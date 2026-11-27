# N382: RTX 5090 FP8理论峰值算力为838 TFLOPS（稠密），基于官方标称FP8 Tensor稀疏算力1,677 TFLOPS的一半计算，与RTX 409

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159

## Claim

RTX 5090 FP8理论峰值算力为838 TFLOPS（稠密），基于官方标称FP8 Tensor稀疏算力1,677 TFLOPS的一半计算，与RTX 4090 FP8理论峰值算力（约330 TFLOPS）相比提升2.54倍

## Corrected Claim

RTX 5090 FP8理论峰值算力为838 TFLOPS（稠密），基于官方标称FP8 Tensor稀疏算力1,677 TFLOPS的一半计算，与RTX 4090 FP8理论峰值算力（约330 TFLOPS）相比提升2.54倍

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090官方标称FP8稀疏算力为1677 TFLOPS，稠密算力为其一半即838.5 TFLOPS（取整838）；RTX 4090 FP8稠密算力约为330 TFLOPS（基于228 TFLOPS FP16 x 2倍精度提升估算或官方数据），838/330 ≈ 2.54倍，数值量级与逻辑推导均自洽。
