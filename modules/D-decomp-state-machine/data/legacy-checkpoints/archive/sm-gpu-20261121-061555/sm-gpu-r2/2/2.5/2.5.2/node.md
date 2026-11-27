# N70: Pipeline Parallelism (PP) 显存分布：在2卡PP下，按层切分，每卡占用约Total_VRAM/2，但需考虑层间激活值传输开销。对于27B

- **status**: degraded
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

[质询]陈述中“权重和KV Cache各占一半”这一具体比例缺乏通用性，严重依赖于序列长度、Batch Size及具体模型架构（如GQA/MQA），并非PP切分的固有属性；此外，PP在长序列推理中虽通信量小，但存在流水线气泡（Bubble）问题，并非绝对优于TP。 | 先验知识/题面给定，逻辑校验通过：PP按层切分确实使显存近似均分，且通信量（仅激活值）通常小于TP（全量激活值），但“权重与KV Cache各占一半”为特定场景下的经验估算而非普适规律，故降级。

## Search Query

Pipeline Parallelism memory distribution LLM
