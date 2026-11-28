# N29: Qwen3.8-27B 在 V100 (Compute Cap 7.0) 上启用 FlashAttention-2 时，Prefill 阶段的计算密度提升约 2

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3.8-27B 在 V100 (Compute Cap 7.0) 上启用 FlashAttention-2 时，Prefill 阶段的计算密度提升约 2.0x 相比标准 Attention，但受限于 V100 缺乏 FP8 Tensor Core，FP8 KV Cache 的读取仍需通过 CPU-GPU 拷贝或 INT8 模拟，导致 Prefill 实际加速比仅为 1.2x-1.5x，单条 262k 上下文 Prefill 耗时 T_prefill ≈ 120-180s。

## Corrected Claim

Qwen3.8-27B 在 V100 (Compute Cap 7.0) 上启用 FlashAttention-2 时，理论上 Prefill 阶段计算密度有显著提升，但受限于 V100 缺乏 FP8 Tensor Core，FP8 KV Cache 的处理效率受限，实际 Prefill 加速比及 262k 上下文耗时需依赖具体实测数据，现有资料未提供确切数值。

## Evidence

[质询]该陈述包含大量具体的性能基准数据（如2.0x计算密度提升、1.2x-1.5x实际加速比、120-180s耗时），这些属于经验事实，无法从第一性原理推导，且参考来源仅涉及启动参数与显存推导，未提供FlashAttention-2在V100上的具体性能测试数据，存在来源缺失风险。 | 逻辑自洽（V100无FP8 Tensor Core导致KV Cache处理受限符合硬件事实），但参考来源[1]仅涵盖参数与显存说明，未直接支持具体的Prefill加速比和耗时数值，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://github.com/openclawzhangchong/llama-cpp-v100-kit/blob/main/docs/03-Qwen3.8-27B-%E5%8F%82%E6%95%B0%E4%B8%8E%E6%98%BE%E5%AD%98%E8%AF%B4%E6%98%8E.md&rut=022b52d9349b439f084f62353055ca3f5dd81f0cc7d6a5398aef77da3eb70da9', 'type': 'ddg', 'title': 'llama-cpp-v100-kit/docs/03-Qwen3.8-27B-参数与显存说明 ... - GitHub'}
