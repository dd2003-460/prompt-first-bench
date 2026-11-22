# N235: 32K 上下文下 NVFP4 量化 Qwen3-27B 的重复率（Repetition Rate）具体数值需检索使用 DistilBART 或自定义 N-gra

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

32K 上下文下 NVFP4 量化 Qwen3-27B 的重复率（Repetition Rate）具体数值需检索使用 DistilBART 或自定义 N-gram 检测器在 LongBench 或 RULER 基准上的测试报告，以量化相对于 BF16 基线的增加幅度是否超过 5% 阈值

## Corrected Claim

需进一步检索以确认 32K 上下文下 NVFP4 量化 Qwen3-27B 在 LongBench 或 RULER 基准上的重复率相对于 BF16 基线的具体增加幅度。

## Evidence

[质询]该陈述本身是一个‘待检索任务’而非‘已确认事实’，且缺乏具体的基准测试数据支持，无法验证‘是否超过5%阈值’这一具体结论。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

LLM long context repetition rate quantization NVFP4 W4 benchmark LongBench
