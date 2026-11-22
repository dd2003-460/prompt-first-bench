# N83: INT8 量化在 32K 长上下文下的 KV Cache 精度损失导致长程依赖任务（如大海捞针）准确率下降 3-5%，该长程退化是短文本 PPL 未完全反映的额

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

INT8 量化在 32K 长上下文下的 KV Cache 精度损失导致长程依赖任务（如大海捞针）准确率下降 3-5%，该长程退化是短文本 PPL 未完全反映的额外质量成本

## Corrected Claim

INT8 量化在 32K 长上下文下通常会导致 KV Cache 精度损失，进而引起长程依赖任务（如大海捞针）准确率出现一定程度的下降（具体幅度视模型与量化策略而定，常见报告在 1-5% 区间），该长程退化往往无法被短文本 PPL 完全捕捉。

## Evidence

[质询]具体数值（3-5%）缺乏通用性，高度依赖模型架构、量化算法（如SmoothQuant, AWQ）及具体任务基准，将其表述为普遍事实存在以偏概全风险；且'短文本PPL未完全反映'虽逻辑合理，但缺乏量化对比数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体精度损失数值属于经验参数，无法从第一性原理严格推出）

## Search Query

Qwen3-27B INT8 KV cache long context needle in haystack accuracy
