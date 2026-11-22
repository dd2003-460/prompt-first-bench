# N240: Qwen3-27B 在 BF16 精度下，上下文长度从 2K 增加到 32K 时，在长上下文基准（如 RULER 或 LongBench）上的性能保持率（例如：

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N70

## Claim

Qwen3-27B 在 BF16 精度下，上下文长度从 2K 增加到 32K 时，在长上下文基准（如 RULER 或 LongBench）上的性能保持率（例如：2K 得分 80%，32K 得分 75%，保持率 93.75%），需获取具体数值以建立 BF16 的长文本性能曲线。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，上下文长度从 2K 增加到 32K 时，在长上下文基准（如 RULER 或 LongBench）上的性能保持率需获取具体实测数值以建立 BF16 的长文本性能曲线，当前缺乏具体数据支持。

## Evidence

[质询]该陈述包含具体的经验性数值（如80%、75%、93.75%），属于特定模型在特定基准下的实测性能数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B long context benchmark 32k RULER LongBench score
