# N238: 工作点A（高并行/高显存）：max_num_seqs=16, TP=4。CUDA Context固定开销1.8GB/卡，Block Manager元数据0.3G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

工作点A（高并行/高显存）：max_num_seqs=16, TP=4。CUDA Context固定开销1.8GB/卡，Block Manager元数据0.3GB/卡，模型权重分摊3.42GB/卡，KV Cache占用13.6GB/卡（N220），总占用19.12GB/卡 > 16GB物理限制，显存溢出，不可行。

## Corrected Claim

工作点A（高并行/高显存）：max_num_seqs=16, TP=4。CUDA Context固定开销1.8GB/卡，Block Manager元数据0.3GB/卡，模型权重分摊3.42GB/卡，KV Cache占用13.6GB/卡（N220），总占用19.12GB/卡 > 16GB物理限制，显存溢出，不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：各项显存占用之和（1.8+0.3+3.42+13.6=19.12GB）大于16GB物理限制，结论正确。
