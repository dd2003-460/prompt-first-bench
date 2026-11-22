# N99: Qwen3-27B 在 FP8 精度下的 MMLU-Pro 基准分数及相对于 BF16 的分数下降幅度，需查找社区一手机测数据，预期下降幅度在 1-3 分之间

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Qwen3-27B 在 FP8 精度下的 MMLU-Pro 基准分数及相对于 BF16 的分数下降幅度，需查找社区一手机测数据，预期下降幅度在 1-3 分之间

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 MMLU-Pro 基准分数及相对于 BF16 的分数下降幅度需查找社区一手机测数据，预期下降幅度可能在 1-3 分之间，但具体数值取决于量化方法。

## Evidence

[质询]具体数值（MMLU-Pro分数及1-3分的下降幅度）属于经验事实，缺乏直接来源支持，且不同量化实现（如SmoothQuant, GPTQ等）可能导致精度损失差异较大，1-3分的范围可能过于乐观或特定于某种量化方法。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization MMLU-Pro score degradation
