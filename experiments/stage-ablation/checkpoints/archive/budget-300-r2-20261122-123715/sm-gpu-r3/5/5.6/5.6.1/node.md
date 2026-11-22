# N338: vLLM 在 AMD MI300X (ROCm 6.0+) 上针对 Qwen3-27B 的 PagedAttention 算子效率系数 k_vllm_rocm：

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

vLLM 在 AMD MI300X (ROCm 6.0+) 上针对 Qwen3-27B 的 PagedAttention 算子效率系数 k_vllm_rocm：需检索 vLLM GitHub 仓库中 ROCm 平台的 MI300X 专项 Benchmark Issue 或 NVIDIA/AMD 联合发布数据，若缺失则标记 [待核验] 并采用保守值 0.75-0.85（基于 A100 到 MI300X 的通常性能映射）

## Corrected Claim

vLLM 在 AMD MI300X (ROCm 6.0+) 上针对 Qwen3-27B 的 PagedAttention 算子效率系数 k_vllm_rocm 暂无公开基准数据，标记为 [待核验]，建议采用保守估计值 0.75-0.85 作为临时参考。

## Evidence

[质询]该系数为特定硬件（MI300X）与特定软件栈（ROCm 6.0+）及模型（Qwen3-27B）组合下的经验性能参数，无法从第一性原理推导，且缺乏公开基准数据支持，属于典型的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数非数学/物理定律，不适用第一性原理豁免条款）。

## Search Query

vLLM MI300X ROCm benchmark Qwen3-27B throughput
