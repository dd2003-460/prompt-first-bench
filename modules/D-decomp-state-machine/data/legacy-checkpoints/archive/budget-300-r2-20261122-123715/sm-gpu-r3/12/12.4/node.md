# N379: RTX 4090 预填充阶段的实际 TTFT 修正系数 k_prefill_efficiency 通常为 0.7-0.9，主要受限于 CUDA 内核启动开销、K

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

RTX 4090 预填充阶段的实际 TTFT 修正系数 k_prefill_efficiency 通常为 0.7-0.9，主要受限于 CUDA 内核启动开销、KV Cache 写入带宽瓶颈及 vLLM/TensorRT-LLM 的批处理策略，实际 TTFT = Theoretical_TTFT / k_prefill_efficiency。

## Corrected Claim

RTX 4090 预填充阶段的实际 TTFT 通常高于理论值，修正系数 k_prefill_efficiency 受 CUDA 内核启动开销、KV Cache 写入带宽及批处理策略影响，具体数值随模型规模、序列长度及软件栈版本变化，一般小于 1。

## Evidence

[质询]该陈述包含具体的经验参数（0.7-0.9）和特定的工程归因（CUDA内核开销、KV Cache带宽等），属于经验事实而非第一性原理可推导内容。由于检索无可用来源，无法验证该具体数值范围及归因的准确性，且不同硬件配置、模型大小及软件版本下该系数波动较大，固定区间可能缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值范围0.7-0.9及归因的准确性）

## Search Query

RTX 4090 LLM prefill latency efficiency benchmark
