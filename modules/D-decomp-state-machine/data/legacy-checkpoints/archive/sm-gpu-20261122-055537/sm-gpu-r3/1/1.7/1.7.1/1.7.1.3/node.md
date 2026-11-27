# N191: 框架基础开销 (CUDA Context + vLLM 内存池) 的精确量化：vLLM 在初始化时会预分配 CUDA Context 和 PagedAttent

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

框架基础开销 (CUDA Context + vLLM 内存池) 的精确量化：vLLM 在初始化时会预分配 CUDA Context 和 PagedAttention 内存池，基础开销通常为 1-2GB。此开销与模型大小无关，但在显存紧张时（如 24GB 卡运行 27B 模型）可能成为 OOM 的触发因素。需验证 vLLM 在 RTX 4090 上的实际基础开销值，以及是否可通过 --gpu-memory-utilization 参数调整预分配比例以优化显存利用。[待核验: vLLM 在 RTX 4090 上的实际基础开销实测数据]

## Corrected Claim

vLLM 在初始化时会预分配 CUDA Context 和 PagedAttention 内存池，存在基础显存开销（通常为数GB量级，具体数值随版本和配置变化）。此开销与模型权重大小无关，但在显存紧张时可能成为 OOM 的触发因素。可通过 --gpu-memory-utilization 参数调整预分配比例以优化显存利用。

## Evidence

[质询]该陈述包含具体的经验性数值（1-2GB基础开销）和特定硬件（RTX 4090）下的行为断言，属于经验事实。由于检索失败，无法提供外部来源直接支持该具体数值范围，且不同vLLM版本或配置下该开销可能存在波动，仅凭逻辑自洽不足以确认为精确量化事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。vLLM确实存在CUDA Context和KV Cache预分配开销，且与模型大小相对独立，但具体数值1-2GB缺乏当前检索证据直接验证。

## Search Query

vLLM RTX 4090 CUDA context memory overhead baseline benchmark
