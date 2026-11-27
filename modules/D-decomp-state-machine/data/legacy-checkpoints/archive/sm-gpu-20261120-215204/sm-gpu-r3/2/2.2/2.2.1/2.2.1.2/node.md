# N204: FP8 (E4M3) 量化 Qwen3-27B 后在 HumanEval (Code) 基准测试上的 Pass@1 下降具体数值为 0.8%，基于 vLLM 社

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

FP8 (E4M3) 量化 Qwen3-27B 后在 HumanEval (Code) 基准测试上的 Pass@1 下降具体数值为 0.8%，基于 vLLM 社区针对 27B 规模模型的量化对比实验，该值低于 N71 声称的 1% 阈值，但接近边界，需关注代码生成任务的敏感性。

## Corrected Claim

FP8 (E4M3) 量化 Qwen3-27B 后在 HumanEval (Code) 基准测试上的 Pass@1 下降幅度较小（约 0.8% 左右，具体数值需进一步核实），低于 1% 阈值，但接近边界，需关注代码生成任务的敏感性。

## Evidence

[质询]具体数值 0.8% 属于经验事实，且参考来源全部缺失，无法验证该特定实验数据是否真实存在或准确；此外，'vLLM 社区针对 27B 规模模型的量化对比实验'这一具体出处描述模糊，难以确认为权威或可复现的基准测试。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值 0.8% 及特定实验背景）

## Search Query

Qwen3-27B FP8 quantization HumanEval Pass@1 performance drop
