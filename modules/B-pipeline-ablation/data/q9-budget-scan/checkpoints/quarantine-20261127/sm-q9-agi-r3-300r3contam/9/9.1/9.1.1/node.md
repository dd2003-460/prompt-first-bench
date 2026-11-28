# N240: MTP 接受率衰减模型：接受率 α(L) 随上下文长度 L 呈指数或对数衰减，α(L) = α_0 * exp(-k*L) 或 α(L) = α_0 - β*l

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

MTP 接受率衰减模型：接受率 α(L) 随上下文长度 L 呈指数或对数衰减，α(L) = α_0 * exp(-k*L) 或 α(L) = α_0 - β*log(L)。基于 Qwen 系列经验，在 8k 时 α≈0.85，在 64k 时 α≈0.60，拟合得到衰减系数 k 或 β，进而外推 L=128k 时的 α(128k) 是否低于 0.40 阈值。

## Corrected Claim

MTP 接受率 α(L) 通常随上下文长度 L 呈现衰减趋势，具体衰减模型（如指数或对数）和参数需基于特定模型系列的实证数据拟合。对于 Qwen 系列，需进一步实验验证其在不同上下文长度下的实际接受率以确认是否低于 0.40 阈值。

## Evidence

[质询]该陈述包含具体的经验数据点（Qwen系列在8k和64k时的MTP接受率分别为0.85和0.60）以及特定的衰减模型形式，这些属于经验事实而非第一性原理可推导内容。由于缺乏外部来源支持，无法验证这些具体数值和模型假设的准确性。 | 经验事实，逻辑自洽但缺来源支持。虽然数学模型本身逻辑自洽，但具体的经验参数（α≈0.85 at 8k, α≈0.60 at 64k）和模型选择（指数或对数衰减）需要实证数据支持，当前无可用来源验证。

## Search Query

Multi-token prediction speculative decoding acceptance rate decay context length qwen
