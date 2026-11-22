# N632: Qwen3-27B 在 FP8 (E4M3) 精度下的 WikiText-103 Perplexity 实测值 (PPL_FP8) 需检索第三方评测（如 Ope

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N262

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 WikiText-103 Perplexity 实测值 (PPL_FP8) 需检索第三方评测（如 OpenCompass 或 vLLM 官方基准），若无法直接获取，采用经验公式 PPL_FP8 ≈ PPL_BF16 * (1 + 0.005 * (1 - 8/16)) 估算，其中系数 0.005 为 8-bit 量化相对于 16-bit 的标准 PPL 增量系数 [待核验]。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 WikiText-103 Perplexity 实测值需检索第三方评测（如 OpenCompass 或 vLLM 官方基准）。若无法直接获取，可参考同类大模型在 8-bit 量化下的典型 PPL 增量范围（通常为 0.1-0.5 PPL 或相对增加 1%-5%）进行定性估算，具体数值需依据实际量化算法和校准数据集确定，不宜使用固定线性公式。

## Evidence

[质询]经验事实排除条款适用：该陈述包含具体的量化误差系数（0.005）和特定的估算公式，属于经验参数而非第一性原理可推导的数学/物理事实。且该公式假设 PPL 增量与位宽线性相关，忽略了不同模型架构、数据集分布及量化算法（如 GPTQ, AWQ, SmoothQuant）对 PPL 影响的巨大差异，缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且系数 0.005 为特定经验值，无法从第一性原理严格推出，符合 degraded 判定条件）

## Search Query

Qwen3-27B FP8 E4M3 WikiText-103 perplexity benchmark
