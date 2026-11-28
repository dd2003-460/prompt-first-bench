# N16: 工具调用接口遵循OpenAI Function Calling标准扩展，定义三类核心工具：1) code_executor (Python sandbox, t

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

工具调用接口遵循OpenAI Function Calling标准扩展，定义三类核心工具：1) code_executor (Python sandbox, timeout=300s)；2) literature_search (arXiv/Semantic Scholar API)；3) statistical_test (scipy.stats wrapper)，每次调用返回结构化JSON{status, result, error_msg}

## Corrected Claim

工具调用接口遵循OpenAI Function Calling标准扩展，定义三类核心工具：1) code_executor (Python sandbox, timeout=300s)；2) literature_search (arXiv/Semantic Scholar API)；3) statistical_test (scipy.stats wrapper)，每次调用返回结构化JSON{status, result, error_msg}

## Evidence

先验知识/题面给定，逻辑校验通过
