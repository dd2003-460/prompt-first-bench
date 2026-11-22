# N291: vLLM 在 FP8 推理模式下，若检测到 GPU 架构不支持原生 FP8 Tensor Core（如 Ampere sm_80），其内部调度器会强制将权重反量

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105, N106, N108

## Claim

vLLM 在 FP8 推理模式下，若检测到 GPU 架构不支持原生 FP8 Tensor Core（如 Ampere sm_80），其内部调度器会强制将权重反量化为 BF16 执行 GEMM，此过程引入的额外显存拷贝开销约为权重体积的 100%（即 27.18GB FP8 权重需额外 54.36GB 显存用于反量化缓冲），导致实际显存占用从 40GB 飙升至 90GB+，直接导致 48GB 卡 OOM。

## Corrected Claim

vLLM 在 FP8 推理模式下，若检测到 GPU 架构不支持原生 FP8 Tensor Core（如 Ampere sm_80），通常会使用支持 FP8 反量化的 GEMM kernel（如 Marlin）或在线反量化策略，而非将全部权重反量化为 BF16 并常驻显存。显存占用主要取决于模型权重本身（FP8 格式）及 KV Cache 等动态部分，不会因反量化过程导致显存占用翻倍至 90GB+。48GB 卡 OOM 更可能由 KV Cache 或 Batch Size 过大导致，而非权重反量化缓冲。

## Evidence

[质询]数值量级与逻辑存在严重矛盾：1. 若权重为27.18GB FP8，反量化为BF16后体积应为54.36GB，而非'额外'54.36GB（总显存占用应从40GB增至约67GB，而非90GB+）；2. vLLM通常采用在线反量化（on-the-fly dequantization）或混合精度策略，极少在推理时一次性将全部权重反量化并常驻显存，'强制反量化为BF16执行GEMM'且'额外显存拷贝开销约为权重体积的100%'的描述不符合主流推理引擎的内存管理逻辑；3. 48GB卡OOM的结论基于错误的显存计算（90GB+），若实际占用为67GB，48GB卡确实会OOM，但原因描述（额外54.36GB缓冲）不准确。 | 先验知识/题面给定，逻辑校验未通过：显存计算存在内部矛盾（27.18GB FP8 -> 54.36GB BF16，总占用应约为54.36GB+其他开销，而非40GB+54.36GB=94.36GB），且vLLM在Ampere上通常使用Marlin kernel或在线反量化，不会简单地将全部权重反量化后常驻显存导致显存翻倍。

## Search Query

vLLM FP8 dequantization overhead memory Ampere A100 fallback mechanism
