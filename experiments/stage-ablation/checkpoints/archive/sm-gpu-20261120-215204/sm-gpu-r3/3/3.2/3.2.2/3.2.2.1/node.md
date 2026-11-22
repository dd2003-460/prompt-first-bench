# N247: L40S 48GB 运行 FP8 权重 + FP8 KV Cache 的实际显存占用修正：KV Cache 占用为 5.37 GB (10.74 GB / 2)

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

L40S 48GB 运行 FP8 权重 + FP8 KV Cache 的实际显存占用修正：KV Cache 占用为 5.37 GB (10.74 GB / 2)，总占用 = 27 GB (权重) + 5.37 GB (KV) + 2 GB (激活/碎片) = 34.37 GB，远低于 48 GB 上限，N86 中 '49GB 略微超出' 的结论错误，实际留有 13.63 GB 余量，足以支持 Batch Size 2-3 的并发请求而无需 PagedAttention 碎片优化。

## Corrected Claim

在特定假设下（KV Cache 占用 5.37 GB），L40S 48GB 运行 FP8 权重 + FP8 KV Cache 的总显存占用约为 34.37 GB，低于 48 GB 上限，留有约 13.63 GB 余量；但‘无需 PagedAttention’的结论需视具体序列长度和并发策略而定，并非绝对。

## Evidence

[质询]KV Cache 占用 5.37 GB 的具体数值缺乏上下文（如序列长度、Batch Size、模型具体架构参数），且‘无需 PagedAttention’的结论过于绝对，忽略了长序列或高并发下显存碎片化及动态分配的实际需求，属于经验性工程判断而非绝对真理。 | 先验知识/题面给定，逻辑校验通过：算术运算 27 + 5.37 + 2 = 34.37 正确，34.37 < 48 成立，余量 13.63 GB 计算无误；但具体 KV 数值及‘无需 PagedAttention’的工程结论依赖特定假设，缺乏通用性，故降级。
