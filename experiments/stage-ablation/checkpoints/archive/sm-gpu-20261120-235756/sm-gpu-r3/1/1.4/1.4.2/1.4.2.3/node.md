# N159: FP8 (E4M3) 权重在 HumanEval 代码生成基准测试中的 Pass@1 下降幅度：代码生成对 token 序列的精确匹配要求高，FP8 量化可能导

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

FP8 (E4M3) 权重在 HumanEval 代码生成基准测试中的 Pass@1 下降幅度：代码生成对 token 序列的精确匹配要求高，FP8 量化可能导致 Pass@1 下降 0.2% - 0.5%（例如 BF16: 78.5% -> FP8: 78.0%），需确认 Qwen3-27B 在 FP8 精度下的 HumanEval Pass@1 具体数值。

## Corrected Claim

FP8 (E4M3) 量化通常会导致代码生成基准（如 HumanEval）的 Pass@1 出现轻微下降，具体幅度取决于模型规模与量化策略，需查阅 Qwen3-27B 官方技术报告或相关评测数据以获取确切数值。

## Evidence

[质询]该陈述包含具体的经验性数值（Pass@1 下降 0.2%-0.5% 及具体基准分数 78.5%->78.0%），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

Qwen3-27B FP8 HumanEval Pass@1 code generation accuracy loss
