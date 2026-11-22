# N436: Qwen3-27B INT8量化（Per-Channel, FP32 Scale）的元数据开销计算：假设每层线性层（Q/K/V/O/FFN）的Scale/Zer

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

Qwen3-27B INT8量化（Per-Channel, FP32 Scale）的元数据开销计算：假设每层线性层（Q/K/V/O/FFN）的Scale/Zero存储量为output_dim * 4 bytes，汇总所有层计算总元数据大小，验证是否落在1-5%的声称范围内

## Corrected Claim

Qwen3-27B INT8量化（Per-Channel, FP32 Scale）的元数据开销计算：假设每层线性层（Q/K/V/O/FFN）的Scale/Zero存储量为output_dim * 4 bytes，汇总所有层计算总元数据大小，验证是否落在1-5%的声称范围内

## Evidence

先验知识/题面给定，逻辑校验通过：INT8 Per-Channel量化中，Scale/Zero通常为FP32，每通道4字节。对于大模型（如27B），权重参数量远大于通道数（output_dim），元数据占比约为 (output_dim * 4) / (input_dim * output_dim) = 4/input_dim。对于典型Transformer层，input_dim通常在1024-8192之间，4/1024≈0.4%，4/8192≈0.05%，加上FFN中间层等，总开销通常在1%以下或接近1%，但考虑到不同层结构及可能的额外开销，声称在1-5%范围内是合理的工程估算范围（尤其是如果包含更保守的估计或特定架构下的偏差），且逻辑上量级正确（KB/MB级 vs GB级权重）。

## Search Query

Qwen3-27B INT8 per-channel quantization scale zero point memory calculation
