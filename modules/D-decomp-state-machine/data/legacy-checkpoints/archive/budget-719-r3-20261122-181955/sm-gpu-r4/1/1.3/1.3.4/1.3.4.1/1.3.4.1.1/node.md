# N522: AMD MI300X 的 BF16 稠密算力为 1307.4 TFLOPS (基于 512 FP32 CUDA cores equivalent 或官方规格，需

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N182

## Claim

AMD MI300X 的 BF16 稠密算力为 1307.4 TFLOPS (基于 512 FP32 CUDA cores equivalent 或官方规格，需核实具体架构代际)，用于计算 Prefill 阶段算力瓶颈：Prefill_TPS = 1307.4e12 / (2 * 27e9 * 32768) ≈ 23.7 tokens/s，该值远低于带宽受限的 Decode 上限，表明 MI300X 在 32K 长上下文 Prefill 阶段是算力瓶颈而非带宽瓶颈。

## Corrected Claim

AMD MI300X 的 BF16 稠密算力约为 1300 TFLOPS（基于 228 个 CU 的 CDNA 3 架构），用于计算 Prefill 阶段算力瓶颈：Prefill_TPS ≈ 1300e12 / (2 * 27e9 * 32768) ≈ 23.5 tokens/s，该值远低于带宽受限的 Decode 上限，表明 MI300X 在 32K 长上下文 Prefill 阶段是算力瓶颈而非带宽瓶颈。

## Evidence

[质询]数值量级与架构常识存在显著偏差：AMD MI300X 基于 CDNA 3 架构，其 BF16 稠密算力官方规格约为 1307.4 TFLOPS 的说法可能混淆了稀疏算力或特定峰值条件，且通常 MI300X 的 BF16 稠密算力在 1000-1300 TFLOPS 区间，但 1307.4 这一精确数值缺乏广泛公认的官方直接引用（常见引用为 ~1300 TFLOPS 或 1.3 PFLOPS），且 '512 FP32 CUDA cores equivalent' 表述错误，AMD 使用 CU (Compute Unit) 而非 CUDA cores，MI300X 拥有 228 个 CU，该等效描述在技术术语上不准确。 | 经验事实，逻辑自洽但缺来源支持；且存在术语错误（CUDA cores vs CU）及数值精确度存疑，无法通过第一性原理严格推导具体 TFLOPS 值，故降级。

## Search Query

AMD MI300X BF16 dense TFLOPS specifications
