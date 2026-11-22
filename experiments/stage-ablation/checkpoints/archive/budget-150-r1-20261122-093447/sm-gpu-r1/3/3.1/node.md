# N25: 精度质量损失度量：使用 MMLU、GSM8K、HumanEval、MATH 基准测试，对比 BF16 基线与 FP8/INT8/NVFP4/W4 的准确率下降；

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

精度质量损失度量：使用 MMLU、GSM8K、HumanEval、MATH 基准测试，对比 BF16 基线与 FP8/INT8/NVFP4/W4 的准确率下降；典型值：FP8 下降 <1%, INT8 下降 1-3%, NVFP4 下降 3-8%, W4 下降 5-15% [待核验：Qwen3-27B 具体数据]

## Corrected Claim

精度质量损失度量：使用 MMLU、GSM8K、HumanEval、MATH 基准测试，对比 BF16 基线与 FP8/INT8/NVFP4/W4 的准确率下降。具体下降幅度取决于量化算法（如 GPTQ/AWQ）及模型特性，通常 FP8 损失极小，INT8 损失较小，低比特（W4/NVFP4）损失相对较大，需针对 Qwen3-27B 具体实验数据确定。

## Evidence

[质询]陈述中关于 FP8/INT8/NVFP4/W4 量化后准确率下降的具体数值范围（如 FP8 <1%, INT8 1-3% 等）属于经验事实，且未提供特定模型（如 Qwen3-27B）或特定量化算法（如 GPTQ, AWQ, SmoothQuant）的上下文，不同算法和模型下差异巨大，通用数值范围缺乏严谨性。 | 参考来源 [1][2][3] 仅介绍了 MMLU、GSM8K、HumanEval 等基准测试的定义和用途，未包含任何关于量化精度损失的具体数据或对比结果，属于经验事实且缺来源支持。

## Search Query

Qwen3-27B FP8 INT8 NVFP4 W4 quantization accuracy MMLU GSM8K benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/csdddn/article/details/161788779&rut=537ac525e6e42ee1f6dbc38a76a1c2a08a0551487665dbd568c3d816fa69add3', 'type': 'ddg', 'title': '大模型评估基准大全：解析MMLU、GSM8K、HumanEval与BBH'}
- {'url': 'https://blog.csdn.net/weixin_29531177/article/details/165098677&rut=7a74050480f4112371ecf010eaa1641c805ad73a015d821bbafb2c9133169c5a', 'type': 'ddg', 'title': '大模型评估三大基准：MMLU、HumanEval与GSM8K解析 - CSDN博客'}
- {'url': 'https://www.datalearner.com/benchmarks&rut=ae5a70ab1de524d0a282e473d07b987812dcb841b2d9ddf0486f4dfd7d3acf85', 'type': 'ddg', 'title': '大模型评测基准榜单 | MMLU, GSM8K, HumanEval等主流评测数据集 | DataLearnerAI'}
