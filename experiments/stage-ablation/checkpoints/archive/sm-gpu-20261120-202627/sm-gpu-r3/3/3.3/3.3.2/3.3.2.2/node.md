# N275: Apple M3 Ultra 在 llama.cpp 或 MLX 框架下推理 Qwen3-27B (BF16, 32K context) 的实测吞吐量约为 8-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

Apple M3 Ultra 在 llama.cpp 或 MLX 框架下推理 Qwen3-27B (BF16, 32K context) 的实测吞吐量约为 8-12 tokens/s，受限于内存带宽瓶颈 (800 GB/s) 及软件栈优化程度，比 NVIDIA A100 (40 tokens/s) 低约 70-80%，比 MI300X (20-35 tokens/s) 低约 50-60%。

## Corrected Claim

Apple M3 Ultra 在 llama.cpp 或 MLX 框架下推理 Qwen3-27B (BF16, 32K context) 的实测吞吐量受限于内存带宽瓶颈 (800 GB/s)，预计处于 8-15 tokens/s 区间，显著低于拥有更高显存带宽的 NVIDIA A100 和 AMD MI300X。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（吞吐量、对比百分比），属于经验事实。由于检索失败，无法验证具体数值（8-12 tokens/s）及对比基准（A100/MI300X的具体配置和软件栈版本）的准确性，存在因软件优化程度不同导致数值偏差的风险。 | 经验事实，逻辑自洽但缺来源支持。M3 Ultra内存带宽800GB/s，Qwen3-27B BF16模型大小约54GB，理论上限约14.8 tokens/s，实测8-12 tokens/s符合内存带宽瓶颈下的合理范围；但具体对比数值缺乏外部证据直接支持。

## Search Query

M3 Ultra llama.cpp Qwen3-27B throughput tokens per second 32k context
