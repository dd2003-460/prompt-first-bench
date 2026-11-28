# N240: 工作点C（保守/低延迟）：max_num_seqs=4, TP=4。CUDA Context固定开销1.8GB/卡，Block Manager元数据0.3GB/

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

工作点C（保守/低延迟）：max_num_seqs=4, TP=4。CUDA Context固定开销1.8GB/卡，Block Manager元数据0.3GB/卡，模型权重分摊3.42GB/卡，KV Cache占用3.4GB/卡（N220），总占用8.92GB/卡，剩余7.08GB显存可用于动态扩容或降低KV量化精度（如FP8->FP16）以提升精度。

## Corrected Claim

工作点C（保守/低延迟）：max_num_seqs=4, TP=4。CUDA Context固定开销1.8GB/卡，Block Manager元数据0.3GB/卡，模型权重分摊3.42GB/卡，KV Cache占用3.4GB/卡（N220），总占用8.92GB/卡，剩余7.08GB显存可用于动态扩容或降低KV量化精度（如FP8->FP16）以提升精度。

## Evidence

先验知识/题面给定，逻辑校验通过：各项显存占用数值相加（1.8+0.3+3.42+3.4=8.92GB）与总占用一致，剩余显存计算（16-8.92=7.08GB，假设单卡16GB显存）逻辑自洽，符合LLM推理显存估算常识。
