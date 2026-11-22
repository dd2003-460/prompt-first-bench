# N126: 修正N20的定性描述：激活值占用并非与权重精度无关。在推理阶段（batch_size=1, 无梯度），激活值主要取决于序列长度和模型结构，与权重精度（BF16 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

修正N20的定性描述：激活值占用并非与权重精度无关。在推理阶段（batch_size=1, 无梯度），激活值主要取决于序列长度和模型结构，与权重精度（BF16 vs FP8）无直接线性关系，但KV Cache部分受精度影响。N20声称的2.5GB峰值需分解为：注意力中间激活 + MLP中间激活。

## Corrected Claim

修正N20的定性描述：激活值占用并非与权重精度无关。在推理阶段（batch_size=1, 无梯度），激活值主要取决于序列长度和模型结构，与权重精度（BF16 vs FP8）无直接线性关系，但KV Cache部分受精度影响。N20声称的2.5GB峰值需分解为：注意力中间激活 + MLP中间激活。

## Evidence

先验知识/题面给定，逻辑校验通过：在推理阶段（batch_size=1），激活值大小主要由序列长度和模型维度决定，与权重存储精度（BF16/FP8）无直接线性关系，KV Cache精度影响属于特例，逻辑自洽。

## Search Query

inference activation memory vs weight precision
