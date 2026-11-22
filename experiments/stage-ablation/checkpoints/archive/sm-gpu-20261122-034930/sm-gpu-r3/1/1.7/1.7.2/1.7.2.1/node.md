# N199: vLLM 0.6.0+ 版本已正式支持 Apple Silicon (M1/M2/M3)，但仅支持 llama.cpp 后端或特定的 Metal 优化路径，不支

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

vLLM 0.6.0+ 版本已正式支持 Apple Silicon (M1/M2/M3)，但仅支持 llama.cpp 后端或特定的 Metal 优化路径，不支持 CUDA 后端。在 Qwen3-27B 上，vLLM on Apple Silicon 的吞吐量通常比 llama.cpp 原生 Metal 后端低 10-20%，因为缺乏针对 Apple GPU 的 PagedAttention 深度优化。

## Corrected Claim

vLLM 在较新版本中已支持 Apple Silicon (M1/M2/M3)，通常依赖 llama.cpp 后端或 Metal 优化路径。在 Qwen3-27B 等大模型上，其吞吐量可能略低于原生 llama.cpp Metal 后端，具体性能差异取决于模型大小、序列长度及具体优化程度，通常认为存在一定性能开销。

## Evidence

[质询]该陈述包含具体的版本号（0.6.0+）、性能对比数据（低10-20%）及特定技术实现细节（PagedAttention优化缺失），属于经验事实。vLLM对Apple Silicon的支持通常通过llama.cpp后端或实验性Metal后端实现，但具体版本界限和精确的性能损耗比例缺乏公开权威基准测试的直接支持，且‘不支持CUDA’在Apple Silicon上属于同义反复（Apple Silicon无CUDA），表述略显冗余但逻辑上无硬伤，主要风险在于具体数值和版本号的准确性无法验证。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM Apple Silicon M2 Ultra performance vs llama.cpp Metal backend
