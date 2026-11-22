# N439: AMD Radeon PRO W7900 在 ROCm 6.0+ 下运行 Qwen3-27B 的兼容性验证：需确认 vLLM 是否支持 ROCm 后端及 Qwe

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N172

## Claim

AMD Radeon PRO W7900 在 ROCm 6.0+ 下运行 Qwen3-27B 的兼容性验证：需确认 vLLM 是否支持 ROCm 后端及 Qwen3 的 GQA 架构。截至 2024 Q4，vLLM 对 ROCm 的支持仍处于实验阶段，Qwen3 模型需通过 `--device rocm` 加载，且可能存在 10-20% 的性能损失 [待核验：需查阅 vLLM GitHub Issues 或 AMD 官方文档]。

## Corrected Claim

AMD Radeon PRO W7900 在 ROCm 6.0+ 下运行 Qwen3-27B 的兼容性需验证 vLLM 对 ROCm 后端及 Qwen3 GQA 架构的支持情况。截至 2024 Q4，vLLM 对 ROCm 的支持可能仍处于实验阶段，具体性能损失需实测确认。

## Evidence

[质询]该陈述包含具体的经验性参数（如'10-20%的性能损失'）和特定时间点的软件状态（'2024 Q4 vLLM对ROCm支持处于实验阶段'），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM ROCm Qwen3 support status 2024
