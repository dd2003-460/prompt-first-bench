# N338: 修正 N117 错误：ROCm 对 Qwen3 架构的 FlashAttention-2 支持并非在 ROCm 6.1+ 才引入，而是 ROCm 6.0 已包含

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

修正 N117 错误：ROCm 对 Qwen3 架构的 FlashAttention-2 支持并非在 ROCm 6.1+ 才引入，而是 ROCm 6.0 已包含对 Hopper/Ada 架构的 FA2 内核支持；W7900 (RDNA3) 不支持 FlashAttention-2（因 RDNA3 缺乏与 Hopper 对应的 Tensor Core 指令集），vLLM 在 W7900 上回退至标准 SDPA 或 Triton 实现的 Attention，导致 Attention 阶段延迟增加约 30-50%，而非整体推理速度下降 30%。

## Corrected Claim

ROCm 对 Qwen3 架构的 FlashAttention-2 支持情况需进一步核实具体版本；W7900 (RDNA3) 因硬件架构限制不支持标准 FlashAttention-2 内核，vLLM 在 W7900 上回退至标准 SDPA 或 Triton 实现的 Attention，导致 Attention 阶段延迟显著增加（具体比例取决于工作负载，通常高于 FA2 实现），而非整体推理速度固定下降 30%。

## Evidence

[质询]该陈述包含具体的性能量化数据（Attention 延迟增加 30-50%）和具体的软件版本支持细节（ROCm 6.0 对 Hopper/Ada 的 FA2 支持），这些属于经验事实。由于检索失败，无法验证 ROCm 6.0 是否确实原生支持 Hopper/Ada 的 FA2（通常 FA2 在 AMD 上的支持较晚或依赖特定后端），且 30-50% 的延迟增加缺乏具体测试环境（模型大小、序列长度、Batch size）支撑，存在数值量级不确定的风险。 | 经验事实，逻辑自洽但缺来源支持。RDNA3 缺乏 Hopper 对应的 Tensor Core 指令集导致无法运行标准 FA2 内核在逻辑上成立，vLLM 回退至 SDPA/Triton 也是合理行为，但具体版本支持情况和性能损耗比例无法通过第一性原理推导，且无外部来源佐证。

## Search Query

ROCm W7900 FlashAttention 2 support Qwen3 vLLM RDNA3 attention kernel
