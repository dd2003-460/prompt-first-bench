# N410: Intel Gaudi 3 (128GB) 运行 Qwen3-27B 的软件栈效率 η_gaudi ≈ 0.7 [待核验]，主要损失来自量化算子覆盖率不足 (I

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139

## Claim

Intel Gaudi 3 (128GB) 运行 Qwen3-27B 的软件栈效率 η_gaudi ≈ 0.7 [待核验]，主要损失来自量化算子覆盖率不足 (INT8/FP8 支持度低于 CUDA 30-40%)，实际有效吞吐 = 理论吞吐 * 0.7；若理论吞吐为 50 tokens/s，实际仅 35 tokens/s

## Corrected Claim

Intel Gaudi 3 (128GB) 运行 Qwen3-27B 时，由于量化算子（INT8/FP8）支持度可能低于 CUDA 生态，软件栈效率预计低于 1.0（具体数值如 0.7 需实测验证），导致实际有效吞吐低于理论峰值。

## Evidence

[质询]该陈述包含具体的经验性参数（效率系数0.7、量化算子覆盖率差距30-40%、具体吞吐数值），这些属于特定硬件与模型组合下的实测或估算数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值0.7及30-40%的覆盖率差距）。

## Search Query

Intel Gaudi 3 Qwen3 inference efficiency 2024
