# N170: 校准数据集领域偏差对质量损失的量化影响：若使用通用 WikiText 校准但在代码领域部署，Qwen3-27B 的 HumanEval Pass@1 下降幅度将

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

校准数据集领域偏差对质量损失的量化影响：若使用通用 WikiText 校准但在代码领域部署，Qwen3-27B 的 HumanEval Pass@1 下降幅度将从基准的 2-4% 扩大至 5-8%；若使用领域内数据（如 The Stack 子集）校准，该下降幅度可控制在 2-3% 以内，校准收益约为 3-5 个百分点

## Corrected Claim

校准数据集领域偏差对质量损失有显著量化影响：若使用通用 WikiText 校准但在代码领域部署，Qwen3-27B 的 HumanEval Pass@1 下降幅度预计会显著扩大；若使用领域内数据（如 The Stack 子集）校准，该下降幅度可得到有效控制，校准收益明显。

## Evidence

[质询]该陈述包含具体的量化数值（如2-4%、5-8%、3-5个百分点），属于经验事实。在缺乏任何参考来源支持的情况下，这些具体数值无法通过第一性原理推导得出，且不同模型、不同校准方法下的实际表现可能存在显著差异，存在数值量级不准确或过度泛化的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

LLM INT8 quantization calibration dataset domain shift impact on code generation accuracy
