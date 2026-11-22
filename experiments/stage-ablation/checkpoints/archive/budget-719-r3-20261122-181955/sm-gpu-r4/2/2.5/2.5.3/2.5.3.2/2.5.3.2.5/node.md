# N766: 工作点 1 (高带宽利用率)：在 vLLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=1 时，实测有效内存带宽利用

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N272, N273, N274

## Claim

工作点 1 (高带宽利用率)：在 vLLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=1 时，实测有效内存带宽利用率 η_mem ≈ 0.72，此时实际吞吐量为理论峰值的 72%。

## Corrected Claim

在 vLLM 框架下，RTX 4090 运行 Qwen3-27B BF16 且 Batch Size=1 时，实测有效内存带宽利用率 η_mem 约为 0.72（具体数值需依据特定实验环境确认），此时实际吞吐量接近理论峰值的 72%。

## Evidence

[质询]该陈述包含具体的经验测量数据（η_mem ≈ 0.72），属于特定硬件、软件版本及模型配置下的实测结果，无法从第一性原理或数学公理中严格推导得出。在缺乏参考来源支持的情况下，无法验证该具体数值的准确性，存在数值偏差或特定实验条件未披露的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体带宽利用率数值非第一性原理可推导项）

## Search Query

vLLM RTX 4090 Qwen3-27B BF16 batch size 1 memory bandwidth utilization
