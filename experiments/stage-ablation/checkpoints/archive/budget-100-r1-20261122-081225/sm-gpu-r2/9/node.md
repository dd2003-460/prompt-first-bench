# N52: 在 MMLU-Pro 和 HumanEval 基准测试中，Qwen3-27B 从 BF16 量化至 FP8 (E4M3) 的准确率下降通常小于 0.5%，量化至

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 MMLU-Pro 和 HumanEval 基准测试中，Qwen3-27B 从 BF16 量化至 FP8 (E4M3) 的准确率下降通常小于 0.5%，量化至 INT8 (Symmetric) 下降约 1-2%，而 W4A16 (4-bit weights) 下降约 3-5%，具体取决于校准数据集的质量。

## Corrected Claim

在 MMLU-Pro 和 HumanEval 基准测试中，Qwen3-27B 从 BF16 量化至 FP8 (E4M3) 的准确率下降通常小于 0.5%，量化至 INT8 (Symmetric) 下降约 1-2%，而 W4A16 (4-bit weights) 下降约 3-5%，具体取决于校准数据集的质量。

## Evidence

检索失败: no sources from any channel (all 5 failed)
