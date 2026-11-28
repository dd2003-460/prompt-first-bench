# N602: NLI模型选型参数：选用DeBERTa-v3-base-mnli-fever-anli模型，其准确率在Fever数据集上为91.3%；推理延迟在V100上约为5

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N214, N215, N216

## Claim

NLI模型选型参数：选用DeBERTa-v3-base-mnli-fever-anli模型，其准确率在Fever数据集上为91.3%；推理延迟在V100上约为50ms/句，相比LLM-as-judge（~500ms/句）快10倍，适合批量预筛。

## Corrected Claim

选用DeBERTa-v3-base-mnli-fever-anli模型，其在Fever数据集上的准确率通常高于90%；在V100 GPU上单句推理延迟显著低于LLM（约50-100ms vs ~500ms+），适合批量预筛。

## Evidence

[质询]具体数值（91.3%准确率、50ms延迟）属于经验事实，缺乏来源支持，且不同硬件/批处理配置下延迟波动较大，50ms仅为特定优化下的理想值，非通用标准。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

DeBERTa-v3-base-mnli-fever-anli accuracy latency V100 benchmark
