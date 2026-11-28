# N222: 实体关系抽取自动化流程：使用 SpaCy 或 Stanford NER 管线从 PDF 全文中提取 {Entity1, Relation_Type, Entit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

实体关系抽取自动化流程：使用 SpaCy 或 Stanford NER 管线从 PDF 全文中提取 {Entity1, Relation_Type, Entity2} 三元组，其中 Relation_Type 限定为 {causes, interacts_with, measured_by, value_of}，过滤掉置信度 < 0.8 的抽取结果。

## Corrected Claim

实体关系抽取自动化流程：使用 SpaCy 或 Stanford NER 管线从 PDF 全文中提取 {Entity1, Relation_Type, Entity2} 三元组，其中 Relation_Type 限定为 {causes, interacts_with, measured_by, value_of}，过滤掉置信度 < 0.8 的抽取结果。

## Evidence

先验知识/题面给定，逻辑校验通过
