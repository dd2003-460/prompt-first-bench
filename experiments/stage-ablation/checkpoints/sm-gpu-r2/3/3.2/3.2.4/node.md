# N75: AMD MI300X 支持 FP8 和 INT8 硬件加速，通过 CDNA 3 架构的 Matrix Core 实现。W4 支持情况：ROCm 6.0+ 已初步

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

AMD MI300X 支持 FP8 和 INT8 硬件加速，通过 CDNA 3 架构的 Matrix Core 实现。W4 支持情况：ROCm 6.0+ 已初步支持 4-bit 量化推理，但性能优化程度低于 NVIDIA 生态，实测吞吐量可能比同级别 NVIDIA 卡低 10-20% [时效待核]。

## Corrected Claim

AMD MI300X 支持 FP8 和 INT8 硬件加速，通过 CDNA 3 架构的 Matrix Core 实现。W4 支持情况：ROCm 6.0+ 已初步支持 4-bit 量化推理，但性能优化程度可能低于 NVIDIA 生态，具体吞吐量差异需视具体工作负载而定。

## Evidence

[质询]具体性能对比数据（低10-20%）及ROCm 6.0+对W4量化的具体支持状态属于经验事实，缺乏权威基准测试或官方文档直接佐证，且不同工作负载下性能差异波动较大，该具体数值区间可能不准确或具有误导性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AMD MI300X W4 4-bit quantization inference performance ROCm 6.0
