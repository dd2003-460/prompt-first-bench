# N647: 输入Token数映射公式：Input_Tokens(T) = Base_Context(2000) + RAG_K(5) × Chunk_Size(512) +

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238, N239, N240

## Claim

输入Token数映射公式：Input_Tokens(T) = Base_Context(2000) + RAG_K(5) × Chunk_Size(512) + System_Prompt(500)，其中T为任务复杂度等级（1-5），RAG_K随T线性增加（K=T），Chunk_Size固定为512 tokens以适配128维嵌入检索

## Corrected Claim

输入Token数映射公式：Input_Tokens(T) = Base_Context(2000) + RAG_K(5) × Chunk_Size(512) + System_Prompt(500)，其中T为任务复杂度等级（1-5），RAG_K随T线性增加（K=T），Chunk_Size固定为512 tokens以适配128维嵌入检索

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM context length token calculation RAG chunk size
