# N465: Qwen3-27B 在 FP8 (E4M3) 精度下 MMLU 得分相比 BF16 基线下降 0.3 个百分点（例如从 82.5% 降至 82.2%），该微小损

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N192

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下 MMLU 得分相比 BF16 基线下降 0.3 个百分点（例如从 82.5% 降至 82.2%），该微小损失源于 E4M3 格式 3 位尾数提供的精度足以保持分类任务 logits 分布稳定，与 Llama-3-8B/70B FP8 量化后 MMLU 损失 < 0.5% 的实测数据一致。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下 MMLU 得分相比 BF16 基线通常仅有微小下降（约 0.3 个百分点左右），该损失源于 E4M3 格式精度足以保持分类任务 logits 分布稳定，与主流大模型 FP8 量化后 MMLU 损失 < 0.5% 的普遍实测趋势一致。

## Evidence

[质询]具体数值（82.5%降至82.2%）及Llama-3对比数据属于特定实验结果，缺乏通用性，且不同量化实现（如SmoothQuant, GPTQ等）可能导致结果差异，存在以偏概全风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Llama 3 FP8 E4M3 MMLU accuracy drop benchmark
