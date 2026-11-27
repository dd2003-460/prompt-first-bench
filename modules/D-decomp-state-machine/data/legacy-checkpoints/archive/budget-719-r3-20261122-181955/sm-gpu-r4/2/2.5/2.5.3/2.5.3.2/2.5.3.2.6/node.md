# N767: 工作点 2 (中等带宽利用率)：在 vLLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=4 时，由于 KV Cac

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N272, N273, N274

## Claim

工作点 2 (中等带宽利用率)：在 vLLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=4 时，由于 KV Cache 访问模式变化及内存控制器排队，实测有效内存带宽利用率 η_mem ≈ 0.65，此时每 token 生成时间增加约 10%。

## Corrected Claim

在 vLLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=4 时，受 KV Cache 访问模式及内存控制器排队影响，有效内存带宽利用率预计显著低于峰值（约 0.65 左右），导致每 token 生成时间增加约 10%。

## Evidence

[质询]该陈述包含具体的经验性数值（η_mem ≈ 0.65, 延迟增加 10%），属于特定硬件、模型和框架配置下的实测数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM RTX 4090 Qwen3-27B BF16 batch size 4 memory bandwidth utilization
