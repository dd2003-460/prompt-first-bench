# N259: Qwen3-27B 在 NVFP4 (4-bit) 量化下，MMLU 基准测试得分相比 BF16 下降约 3-5 个百分点（例如从 85% 降至 80-82%）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Qwen3-27B 在 NVFP4 (4-bit) 量化下，MMLU 基准测试得分相比 BF16 下降约 3-5 个百分点（例如从 85% 降至 80-82%），具体数值需参考 Qwen 官方技术报告或第三方评测。

## Corrected Claim

Qwen3-27B 在 4-bit 量化下，MMLU 基准测试得分相比 BF16 通常会有所下降，具体幅度取决于量化算法（如 GPTQ, AWQ 等）及校准数据集，一般下降幅度在 1-5 个百分点之间，具体数值需参考官方技术报告或第三方评测。

## Evidence

[质询]具体数值（85%降至80-82%）及量化方法（NVFP4）缺乏公开权威来源支持，且NVFP4并非Qwen官方标准量化格式，存在参数臆造或混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值与量化格式组合无法从第一性原理推出）

## Search Query

Qwen3-27B NVFP4 MMLU benchmark score
