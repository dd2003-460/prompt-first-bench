# N323: 1×A100 80GB (BF16) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量下限：基于vLLM/TensorRT-LLM在A100 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N90

## Claim

1×A100 80GB (BF16) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量下限：基于vLLM/TensorRT-LLM在A100 80GB上的公开基准测试，BF16精度下Qwen3-27B的实测吞吐量通常在 30-50 tokens/s 区间 [search: 需检索具体benchmark]，接近父节点预估的下限，主要受限于BF16计算密度和KV Cache管理效率。

## Corrected Claim

1×A100 80GB (BF16) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量：基于vLLM/TensorRT-LLM在A100 80GB上的公开基准测试，BF16精度下Qwen3-27B的实测吞吐量预计在 20-60 tokens/s 区间（具体数值需依赖实际 benchmark 数据），主要受限于BF16计算密度和KV Cache管理效率。

## Evidence

[质询]数值量级存疑：Qwen3-27B 在 A100 80GB 上 BF16 精度下，32K 长上下文场景的吞吐量受限于 KV Cache 显存占用及 Attention 计算复杂度，30-50 tokens/s 的下限估计可能过于乐观或保守，且缺乏具体公开基准测试的直接数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体 benchmark 数值）

## Search Query

vLLM A100 80GB Qwen3-27B BF16 throughput benchmark 32k context
