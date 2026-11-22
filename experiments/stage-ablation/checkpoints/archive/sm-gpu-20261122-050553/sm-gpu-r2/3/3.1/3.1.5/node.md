# N67: FP8 精度对 32K 长上下文推理的累积误差影响：分析 KV Cache 若也采用 FP8 存储，在 32K 长度下注意力分数的量化噪声累积效应，对比 KV 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

FP8 精度对 32K 长上下文推理的累积误差影响：分析 KV Cache 若也采用 FP8 存储，在 32K 长度下注意力分数的量化噪声累积效应，对比 KV Cache 保持 BF16 时的质量差异，确定‘权重 FP8 + KV BF16’混合精度策略的质量-显存权衡点。

## Corrected Claim

在32K长上下文推理中，KV Cache采用FP8存储会引入量化噪声累积效应，通常导致注意力分数精度下降；相比KV Cache保持BF16，'权重FP8 + KV BF16'混合精度策略在显存占用与生成质量之间通常能取得较好的平衡，但具体最优权衡点需结合特定模型与量化算法实验确定。

## Evidence

[质询]该陈述包含具体的工程权衡结论（'权重 FP8 + KV BF16'为最优权衡点），属于经验事实。在缺乏具体模型架构、硬件平台及量化算法（如SmoothQuant, FP8 E4M3/E5M2）背景的情况下，直接断言该混合策略为确定的'权衡点'缺乏普适性，且不同场景下KV Cache量化对长上下文累积误差的影响程度差异巨大，可能存在过度概括的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该结论依赖具体实验数据，无法从第一性原理严格推出）。

## Search Query

FP8 KV cache long context 32k cumulative error attention accuracy LLM
