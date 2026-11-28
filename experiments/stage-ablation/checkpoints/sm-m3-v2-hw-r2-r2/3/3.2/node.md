# N18: 长程依赖管理采用‘滑动窗口摘要’机制：每 1000 tokens 生成一次压缩摘要，存入短期记忆池；当上下文超过 16k tokens 时，自动替换早期原始内容

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

长程依赖管理采用‘滑动窗口摘要’机制：每 1000 tokens 生成一次压缩摘要，存入短期记忆池；当上下文超过 16k tokens 时，自动替换早期原始内容为摘要，确保关键信息保留率 >95%。

## Corrected Claim

长程依赖管理采用‘滑动窗口摘要’机制：每 1000 tokens 生成一次压缩摘要，存入短期记忆池；当上下文超过 16k tokens 时，自动替换早期原始内容为摘要，确保关键信息保留率 >95%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sliding window summarization LLM long context dependency management
