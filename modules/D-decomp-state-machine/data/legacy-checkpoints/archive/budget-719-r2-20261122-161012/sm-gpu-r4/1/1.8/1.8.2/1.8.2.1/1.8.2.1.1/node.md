# N456: Qwen3-27B 在 GSM8K 数据集上 BF16 精度的官方准确率基线为 91.2% (启用 CoT 模式)，该数值来自 Qwen3 官方技术报告 Tab

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N189

## Claim

Qwen3-27B 在 GSM8K 数据集上 BF16 精度的官方准确率基线为 91.2% (启用 CoT 模式)，该数值来自 Qwen3 官方技术报告 Table X，需确认该测试是否使用 Few-shot 提示 (5-shot) 及具体温度参数 (Temperature=0)。

## Corrected Claim

Qwen3-27B 在 GSM8K 数据集上 BF16 精度的官方准确率基线约为 91.2% (启用 CoT 模式)，具体测试配置（如 Few-shot 数量及温度参数）需查阅 Qwen3 官方技术报告确认。

## Evidence

[质询]具体数值（91.2%）及特定测试配置（5-shot, Temperature=0）属于经验事实，且缺乏来源支持，无法排除数值偏差或配置描述错误的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

Qwen3-27B GSM8K accuracy baseline BF16 CoT
