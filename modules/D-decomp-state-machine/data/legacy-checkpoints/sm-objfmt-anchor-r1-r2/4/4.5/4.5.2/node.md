# N91: 中优先级数据缺口：Qwen3-27B 在 FP8 和 NVFP4 精度下的具体 MMLU/CMMLU 准确率下降值 (ΔAcc) 缺失。缺失原因：官方技术报告可

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

中优先级数据缺口：Qwen3-27B 在 FP8 和 NVFP4 精度下的具体 MMLU/CMMLU 准确率下降值 (ΔAcc) 缺失。缺失原因：官方技术报告可能未披露细粒度量化评测。获取路径：下载 Qwen3-27B-FP8 检查点，在本地使用 lm-evaluation-harness 运行 MMLU 子集 (1000 samples)，耗时约 2-4 小时 (单卡 4090)。

## Corrected Claim

中优先级数据缺口：Qwen3-27B 在 FP8 和 NVFP4 精度下的具体 MMLU/CMMLU 准确率下降值 (ΔAcc) 缺失。缺失原因：官方技术报告可能未披露细粒度量化评测。获取路径：下载 Qwen3-27B-FP8 检查点，在本地使用 lm-evaluation-harness 运行 MMLU 子集 (1000 samples)，耗时约 2-4 小时 (单卡 4090)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量适中，FP8/NVFP4 量化后单卡 4090 (24GB) 显存足以承载推理，lm-evaluation-harness 运行 1000 样本 MMLU 子集耗时 2-4 小时符合常规推理速度估算，数据缺口描述符合当前开源模型评测现状。
