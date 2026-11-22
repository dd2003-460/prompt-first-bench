# N155: W4 量化推理中 GPU 侧反量化计算开销：Tensor Core 执行 W4 到 BF16 的反量化及矩阵乘法，相比原生 BF16 推理，计算吞吐量下降约 2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

W4 量化推理中 GPU 侧反量化计算开销：Tensor Core 执行 W4 到 BF16 的反量化及矩阵乘法，相比原生 BF16 推理，计算吞吐量下降约 20-40%，主要因反量化指令占用 Tensor Core 周期 [待核验]

## Corrected Claim

W4 量化推理中，由于需要额外的反量化步骤（将 W4 权重转换为 BF16 或 FP16 以利用 Tensor Core），相比原生 BF16 推理，计算吞吐量通常会有一定程度的下降，具体幅度取决于硬件架构和实现细节。

## Evidence

[质询]该陈述包含具体的经验性数值范围（20-40%）和特定的硬件机制归因（反量化指令占用Tensor Core周期），属于硬件性能经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

W4 quantization inference throughput degradation tensor core overhead
