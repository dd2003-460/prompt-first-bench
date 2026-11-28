# N35: Qwen3.8-27B NVFP4 量化在 FP16 基准下的绝对性能衰减率 Δ%（需检索 HuggingFace/官方技术报告获取 MMLU/ARC/GPQA

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3.8-27B NVFP4 量化在 FP16 基准下的绝对性能衰减率 Δ%（需检索 HuggingFace/官方技术报告获取 MMLU/ARC/GPQA 等基准的 FP16 vs NVFP4 分数差异），该值直接决定本地模型能否独立处理复杂科研逻辑，置信度 conf=low，属于关键黑盒参数。

## Corrected Claim

Qwen3.8-27B NVFP4 量化在 FP16 基准下的性能衰减率需查阅具体技术报告或社区评测获取，不同基准（如 MMLU、GPQA）的衰减幅度可能存在差异，目前缺乏统一的公开绝对数值。

## Evidence

[质询]该陈述声称存在一个具体的“绝对性能衰减率 Δ%”数值，但这是一个高度依赖具体量化实现细节（如校准数据集、量化算法版本）的经验事实，且不同基准（MMLU/ARC/GPQA）的衰减率通常不一致，不存在单一的通用“绝对”数值；此外，Qwen3.8-27B 这一具体型号及 NVFP4 量化版本的官方公开数据可能尚未广泛发布或存在版本混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值或确认该特定量化版本的公开基准数据）

## Search Query

Qwen3.8-27B NVFP4 quantization benchmark performance degradation vs FP16 MMLU GPQA
