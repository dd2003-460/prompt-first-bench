# N20: INT8 精度质量损失：INT8 (GPTQ/AWQ) 在 7B-70B 模型上 perplexity 增加 1-3%，在代码生成和数学推理任务上准确率下降 2

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

INT8 精度质量损失：INT8 (GPTQ/AWQ) 在 7B-70B 模型上 perplexity 增加 1-3%，在代码生成和数学推理任务上准确率下降 2-5%，边界可接受

## Corrected Claim

INT8 (GPTQ/AWQ) 在 7B-70B 模型上通常会导致轻微的 perplexity 增加和特定任务（如代码/数学）准确率下降，具体幅度取决于模型与数据集，一般认为在可接受范围内。

## Evidence

[质询]具体数值范围（perplexity 1-3%, 准确率 2-5%）属于经验事实，且不同模型、数据集及量化实现（如 GPTQ vs AWQ 的具体配置）会导致结果波动，仅凭逻辑无法确定该精确区间，需依赖具体实验数据支持。 | 来源 [1][2][3] 均涉及 INT8/GPTQ/AWQ 的量化对比与精度损失讨论，主题相关，但摘要中未提供具体的 perplexity 或准确率下降百分比数值，属于间接支持；该陈述为经验事实，逻辑自洽但缺乏直接数值来源支持，故降级。

## Search Query

INT8 GPTQ AWQ quantization LLM perplexity accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_37647148/article/details/161776271&rut=fe61a36c5f2f092fad5634128462803eb9671522aca5834aab3bda206586d57f', 'type': 'ddg', 'title': '量化压缩实战：Int8 / Int4 / Awq / Gptq 全面对比 - Csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_33804582/article/details/92941367&rut=1756099c0cce6ad66a8bdbf9896a9c97fe19528ff903b806b12ef8433e898d21', 'type': 'ddg', 'title': '大模型量化技术全解析：从int8到gptq/Awq，降低部署成本实战指南-csdn博客'}
- {'url': 'https://guijiagi.com/posts/model-quantization-2026-int4-int8-awq-gptq-comparison/&rut=acf560ae4b150e45982209726534866d0d46bcc0d2a7d8a603e6aa3f7440da4a', 'type': 'ddg', 'title': '模型量化技术 2026：Int4/Int8/Awq/Gptq 实测对比'}
