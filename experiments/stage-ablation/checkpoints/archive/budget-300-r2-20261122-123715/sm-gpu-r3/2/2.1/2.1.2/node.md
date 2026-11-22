# N54: Qwen3-27B 在代码生成任务（HumanEval/MBPP）上，INT8 量化（SmoothQuant/GPTQ）相对于 BF16 基准的 Pass@1 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3-27B 在代码生成任务（HumanEval/MBPP）上，INT8 量化（SmoothQuant/GPTQ）相对于 BF16 基准的 Pass@1 准确率下降需 < 2% 方可判定为质量损失可接受，若下降 > 5% 则必须升级至 BF16 或更高精度。

## Corrected Claim

Qwen3-27B 在代码生成任务上，INT8 量化相对于 BF16 基准的 Pass@1 准确率下降通常较小，具体可接受阈值需根据实际业务场景评估，一般工程实践中若下降超过 5% 可能需考虑升级精度，但缺乏统一硬性标准。

## Evidence

[质询]该陈述包含具体的工程经验阈值（<2% 可接受，>5% 必须升级），属于经验事实而非第一性原理可推导的数学/物理定律。参考来源仅讨论了 Qwen3-27B 的部署硬件需求（如 NPU 上只能用 INT4/INT8）和通用量化背景，并未提供 HumanEval/MBPP 上 INT8 相对于 BF16 的具体 Pass@1 下降数据或行业公认的量化质量损失阈值标准。 | 逻辑自洽（量化通常导致精度下降，设定阈值符合工程直觉），但参考来源 [1][2][3] 均未提供具体的 Pass@1 下降数值或该特定阈值标准，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B INT8 quantization code generation accuracy drop HumanEval

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29045585/article/details/166928995&rut=8265792bd606847626fd40317ebc20575dbff66ee12898895751896533512f39', 'type': 'ddg', 'title': 'Qwen3.8-27B本地部署实测：代码生成、视觉理解与Agent工具调用全解析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/95070160&rut=169d1ba757c32ba9dec9c6bffbd734d224608e67fce1b2d4ce67d6b041d66af5', 'type': 'ddg', 'title': '阿里云Qwen3.8 27B本地部署指南：代码生成、硬件需求与API集成_weixin_30387423-码道开发者社区'}
- {'url': 'https://blog.csdn.net/weixin_29041195/article/details/166864950&rut=e6c1bc79403fd6c093edb84cddc807f867d0f5e8bd055a2e6f2d41b0c04519f1', 'type': 'ddg', 'title': 'Intel NPU上部署Qwen3-8-27B大模型推理加速实战 - CSDN博客'}
