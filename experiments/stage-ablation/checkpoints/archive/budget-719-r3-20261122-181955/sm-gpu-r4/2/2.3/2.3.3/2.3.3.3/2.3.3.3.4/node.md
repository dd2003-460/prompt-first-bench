# N704: vLLM 在 RTX 4090 (24GB) 上运行 Qwen3-27B (INT4 权重 13.5GB) 时的最大并发数计算：可用显存 = 24 - 13.5

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N251, N252, N253

## Claim

vLLM 在 RTX 4090 (24GB) 上运行 Qwen3-27B (INT4 权重 13.5GB) 时的最大并发数计算：可用显存 = 24 - 13.5 - 3 (框架) - 1 (OS) = 6.5 GB；考虑 10% 碎片率，有效 KV 容量 = 6.5 / 1.1 ≈ 5.9 GB；单请求 KV Cache = 8 GB (BF16)；最大并发 = 0 (无法支持单请求 32K BF16)；若启用 INT8 KV Cache (4 GB/req)，有效容量 5.9 GB 支持 1 个并发 (5.9/4.0=1.47, floor=1)。

## Corrected Claim

vLLM 在 RTX 4090 (24GB) 上运行 Qwen3-27B (INT4 权重 13.5GB) 时，若假设单请求 32K 序列 BF16 KV Cache 占用约 8GB，则有效显存约 5.9GB 无法支持单请求；若启用 INT8 KV Cache (约 4GB/req)，理论上支持 1 个并发。

## Evidence

[质询]单请求 KV Cache 为 8GB (BF16) 的数值缺乏具体模型架构参数（如层数、头数、序列长度）支持，属于经验估算，可能存在量级偏差；此外，vLLM 默认通常使用 PagedAttention 且 KV Cache 精度常与权重或独立配置，直接假设 8GB/req 且未考虑 PagedAttention 的块分配效率（通常比 1.1 碎片率更复杂）是主要攻击点。 | 先验知识/题面给定，逻辑校验通过：显存减法逻辑自洽，并发数计算（floor(5.9/4.0)=1）数学正确，但 KV Cache 单请求大小 8GB 为经验估算值，缺乏来源直接支持具体参数，故降级。

## Search Query

vLLM memory efficiency vs llama.cpp batch size limit
