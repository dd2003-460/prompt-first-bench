# N602: 若使用 llama.cpp 替代 vLLM 在 MI300X 上运行 Qwen3-27B，由于缺少 PagedAttention 支持，内存碎片化率增加 30%

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

若使用 llama.cpp 替代 vLLM 在 MI300X 上运行 Qwen3-27B，由于缺少 PagedAttention 支持，内存碎片化率增加 30%，导致最大支持上下文长度从 32K 降至 24K（在 192GB 显存下），除非启用手动内存预分配。

## Corrected Claim

若使用 llama.cpp 替代 vLLM 在 MI300X 上运行 Qwen3-27B，由于缺少 PagedAttention 支持，可能导致内存碎片化增加，从而降低最大支持上下文长度（具体数值需实测验证）。

## Evidence

[质询]具体数值（30%碎片率、24K上下文）缺乏公开基准测试支持，且llama.cpp在MI300X上的实际性能表现及内存管理细节属于高度依赖具体版本和配置的经验事实，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

llama.cpp AMD ROCm memory fragmentation max context length MI300X
