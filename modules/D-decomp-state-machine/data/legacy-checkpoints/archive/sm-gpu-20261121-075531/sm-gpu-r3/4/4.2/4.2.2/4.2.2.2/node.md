# N260: Qwen3-27B 在 FP8 精度下（如 GPTQ-FP8 或原生 FP8）的 MMLU-Pro 实测得分具体数值，需区分量化方法（权重量化 vs 激活量化）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82, N83, N84

## Claim

Qwen3-27B 在 FP8 精度下（如 GPTQ-FP8 或原生 FP8）的 MMLU-Pro 实测得分具体数值，需区分量化方法（权重量化 vs 激活量化）。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 MMLU-Pro 得分取决于具体的量化方法（如 GPTQ-FP8 或原生 FP8）及评测配置，不同方法间存在性能差异，需查阅特定量化框架的官方报告或基准测试数据以获取准确数值。

## Evidence

[质询]该陈述要求提供具体的实测数值，但不同量化方法（GPTQ-FP8 vs 原生FP8）及不同评测设置下的得分存在差异，且缺乏统一基准，直接给出单一具体数值易产生误导或口径混淆。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B FP8 MMLU-Pro score GPTQ AWQ
