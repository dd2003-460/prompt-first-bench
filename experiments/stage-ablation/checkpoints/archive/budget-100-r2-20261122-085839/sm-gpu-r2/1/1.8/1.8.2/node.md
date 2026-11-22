# N53: Qwen3-27B 在 GPTQ (W4A16) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 80.8% (Δ=-4.2%)，GSM8K 从 9

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 在 GPTQ (W4A16) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 80.8% (Δ=-4.2%)，GSM8K 从 90.0% 降至 83.5% (Δ=-6.5%) [待核验: GPTQ 4-bit 对 Qwen3 的具体实测数据，通常 GPTQ 在 4-bit 下略逊于 AWQ 或持平]

## Corrected Claim

Qwen3-27B 在 GPTQ (W4A16) 量化下，MMLU 和 GSM8K 分数相较于 BF16 基线出现显著下降（通常降幅在 3%-7% 之间），具体数值取决于量化配置与评测集版本。

## Evidence

[质询]具体数值（85.0%, 80.8%, 90.0%, 83.5%）属于特定实验条件下的经验数据，不同量化实现（如 GPTQ 的不同版本、校准集大小、量化粒度）会导致结果波动，且 Qwen3-27B 的 BF16 基线分数在不同评测集版本中也可能存在差异，无法仅凭逻辑推导确定精确到小数点后一位的数值。 | 经验事实，逻辑自洽（4-bit 量化导致精度下降符合直觉，降幅在合理范围内）但缺来源支持，且检索无可用来源。

## Search Query

Qwen3-27B GPTQ 4-bit W4A16 MMLU GSM8K benchmark score
