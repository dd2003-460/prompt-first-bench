# N16: INT8精度下Qwen3-27B的权重显存占用为27GB，KV Cache在FP16下为10.7GB，总显存需求约41.7GB。

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

INT8精度下Qwen3-27B的权重显存占用为27GB，KV Cache在FP16下为10.7GB，总显存需求约41.7GB。

## Corrected Claim

INT8精度下Qwen3-27B的权重显存占用为27GB，KV Cache在FP16下为10.7GB，总显存需求约41.7GB。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1详细计算了KV Cache在FP16和INT8下的显存占用及总显存，子节点2又重复了相同的计算过程（27+10.7+4=41.7和36.35），两者内容高度重叠，缺乏正交性；子节点2的核心价值在于指出需明确推荐方案，但这部分逻辑本应整合进子节点1的结论中，而非独立存在。）
