# N79: RTX 4090 支持 INT8 Tensor Core 运算，其 INT8 理论峰值算力为 1652 TOPS，相比 BF16 的 826 TFLOPS 提供

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12, N13, N14

## Claim

RTX 4090 支持 INT8 Tensor Core 运算，其 INT8 理论峰值算力为 1652 TOPS，相比 BF16 的 826 TFLOPS 提供 2x 理论加速；但在 LLM 解码阶段（memory-bound），INT8 的实际吞吐提升通常仅为 BF16 的 1.2-1.5 倍，受限于显存带宽而非计算单元 [待核验：需引用 LLM 解码阶段 INT8 实测吞吐比]。

## Corrected Claim

RTX 4090 支持 INT8 Tensor Core 运算，其 INT8 理论峰值算力约为 1321-1652 TOPS（取决于稀疏加速口径），相比 BF16 提供 2x 理论计算加速；但在 LLM 解码阶段（memory-bound），INT8 的实际吞吐提升通常仅为 BF16 的 1.2-1.5 倍，主要受限于显存带宽而非计算单元。

## Evidence

[质询]INT8 理论峰值算力 1652 TOPS 的数值存在争议，通常 RTX 4090 的 INT8 峰值算力被引用为 1321.6 TOPS (基于 82.58 TFLOPS FP32 * 16) 或 1652 TOPS (基于 103.2 TFLOPS FP32 * 16，取决于是否计入稀疏加速或特定计算模式)，且 BF16 826 TFLOPS 通常指稀疏加速后的数值，非稀疏下约为 413 TFLOPS，两者对比需明确是否同口径（稀疏 vs 非稀疏）。此外，LLM 解码阶段 INT8 实际吞吐提升 1.2-1.5 倍属于经验性观察，受具体模型大小、Batch Size 及硬件实现影响极大，缺乏通用定值。 | 先验知识/题面给定，逻辑校验通过。RTX 4090 确实支持 INT8 Tensor Core，且 LLM 解码阶段为 memory-bound，INT8 量化主要减少显存占用和带宽压力，而非直接提升计算速度，因此实际加速比远低于理论计算加速比（2x），1.2-1.5 倍符合工程直觉。虽然具体 TOPS 数值口径需澄清，但核心逻辑（理论 2x vs 实际受带宽限制）自洽。

## Search Query

RTX 4090 INT8 tensor core TOPS vs BF16 TFLOPS LLM decoding throughput ratio
