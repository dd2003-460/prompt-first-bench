# N52: Qwen3-27B 在 AWQ (W4A16) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 81.5% (Δ=-3.5%)，GSM8K 从 90

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 在 AWQ (W4A16) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 81.5% (Δ=-3.5%)，GSM8K 从 90.0% 降至 84.0% (Δ=-6.0%) [待核验: AWQ 对 Qwen3 的具体实测数据]

## Corrected Claim

Qwen3-27B 在 AWQ (W4A16) 量化下，MMLU 和 GSM8K 分数相较于 BF16 基线出现显著下降（具体数值需参考特定实验报告，通常 GSM8K 降幅大于 MMLU）。

## Evidence

[质询]具体数值（85.0%, 81.5%, 90.0%, 84.0%）属于特定实验条件下的经验数据，缺乏公开权威基准测试的直接引用，存在数值虚构或混淆不同量化方案（如GPTQ vs AWQ）结果的风险。 | 经验事实，逻辑自洽（量化通常导致性能下降，且数学推理任务GSM8K对量化更敏感，降幅大于MMLU符合直觉），但检索无可用来源支持具体数值，无法排除其他可能性。

## Search Query

Qwen3-27B AWQ W4A16 MMLU GSM8K benchmark score
