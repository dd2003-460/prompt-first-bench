# N286: SGLang 相比 vLLM 在 Batch Size=1 时的吞吐优势来源分解：SGLang_Advantage = (Scheduler_Overhead_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

SGLang 相比 vLLM 在 Batch Size=1 时的吞吐优势来源分解：SGLang_Advantage = (Scheduler_Overhead_vLLM - Scheduler_Overhead_SGLang) / Total_Time + (Kernel_Fusion_Gain_SGLang - Kernel_Fusion_Gain_vLLM)，需量化调度开销差异（通常微秒级）和内核融合对 GEMM 启动延迟的影响。

## Corrected Claim

SGLang 相比 vLLM 在 Batch Size=1 时的吞吐优势来源分解：SGLang_Advantage = (Scheduler_Overhead_vLLM - Scheduler_Overhead_SGLang) / Total_Time + (Kernel_Fusion_Gain_SGLang - Kernel_Fusion_Gain_vLLM)，需量化调度开销差异（通常微秒级）和内核融合对 GEMM 启动延迟的影响。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

SGLang vs vLLM single stream throughput scheduler overhead kernel fusion
