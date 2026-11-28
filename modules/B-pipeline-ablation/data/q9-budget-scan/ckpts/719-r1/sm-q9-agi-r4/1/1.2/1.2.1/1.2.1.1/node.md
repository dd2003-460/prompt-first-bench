# N121: RULER 基准中 Multi-needle retrieval 任务的具体定义：在 128K 上下文中嵌入 K 根针（K∈{1,2,4}），要求模型同时召回所

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

RULER 基准中 Multi-needle retrieval 任务的具体定义：在 128K 上下文中嵌入 K 根针（K∈{1,2,4}），要求模型同时召回所有针的位置或内容，Recall@1 定义为正确召回至少一根针的概率，需区分 K=1 和 K>1 的不同难度等级

## Corrected Claim

RULER 基准中 Multi-needle retrieval 任务的具体定义：在 128K 上下文中嵌入 K 根针（K∈{1,2,4}），要求模型同时召回所有针的位置或内容，Recall@1 定义为正确召回至少一根针的概率，需区分 K=1 和 K>1 的不同难度等级

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RULER benchmark multi-needle retrieval task definition K needles recall at 1
