# N253: Qwen3-27B (BF16) 在 HumanEval (0-shot) 基准上的精确 pass@1 得分，需查阅 Qwen3 官方技术报告或 Hugging

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

Qwen3-27B (BF16) 在 HumanEval (0-shot) 基准上的精确 pass@1 得分，需查阅 Qwen3 官方技术报告或 HuggingFace 模型卡片以确认是否落在 70-75% 区间，若为 Qwen3.6-27B 则得分可能更高（约 75-80%），需区分具体版本号。

## Corrected Claim

Qwen3-27B (BF16) 在 HumanEval (0-shot) 基准上的 pass@1 得分需查阅官方技术报告确认，通常该规模模型得分在 70%-80% 区间，具体数值取决于确切版本号（如 Qwen3 或 Qwen2.5），'Qwen3.6' 版本号可能不存在或为误称。

## Evidence

[质询]该陈述包含具体的经验性数值区间（70-75% 和 75-80%），属于硬件/模型性能规格类事实，无法从第一性原理推导。且陈述中提到的 'Qwen3.6-27B' 版本号在已知公开信息中不存在（Qwen 系列通常为 Qwen2, Qwen2.5, Qwen3 等，无 3.6 版本），存在版本号混淆或虚构的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，且版本号 'Qwen3.6' 存疑，无法确认具体得分区间）。

## Search Query

Qwen3-27B HumanEval pass@1 score official technical report
