# N70: Pipeline Parallelism (PP) 显存分布：在2卡PP下，按层切分，每卡占用约Total_VRAM/2，但需考虑层间激活值传输开销。对于27B

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

Pipeline Parallelism (PP) 显存分布：在2卡PP下，按层切分，每卡占用约Total_VRAM/2，但需考虑层间激活值传输开销。对于27B模型（64层），每卡32层，权重和KV Cache各占一半，显存分布与TP类似，但PP的通信开销低于TP，适合长序列推理。

## Corrected Claim

在2卡Pipeline Parallelism (PP)下，按层切分使每卡占用约Total_VRAM/2的显存。PP的通信开销主要涉及层间激活值传输，通常低于Tensor Parallelism (TP)的全量激活值通信，适合长序列推理，但需注意流水线气泡带来的延迟影响。显存中权重与KV Cache的具体占比取决于序列长度和Batch Size，并非固定各占一半。

## Evidence

父节点级核验未通过：不完备（子节点1和子节点2虽然都涉及权重显存计算，但分别对应'单卡不可行性验证'和'2卡PP下的具体分布计算'，逻辑上是递进关系而非重复，故正交。然而，父节点明确提到'KV Cache各占一半'，但三个子节点中均未包含KV Cache的显存估算或分布分析，导致关键方面缺失。）

## Search Query

Pipeline Parallelism memory distribution LLM
