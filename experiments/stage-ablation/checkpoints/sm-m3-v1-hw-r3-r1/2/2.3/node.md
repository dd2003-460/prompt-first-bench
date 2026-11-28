# N14: 外部记忆检索命中率：基于向量数据库的实验结果检索，其Top-5命中率需>70%才能有效支撑知识更新，低于该阈值时需优化embedding模型或索引结构（预期命中

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

外部记忆检索命中率：基于向量数据库的实验结果检索，其Top-5命中率需>70%才能有效支撑知识更新，低于该阈值时需优化embedding模型或索引结构（预期命中率受文档切分粒度影响显著）

## Corrected Claim

外部记忆检索命中率：基于向量数据库的实验结果检索，其Top-5命中率需达到一定阈值（通常建议>70%，具体视业务容忍度而定）才能有效支撑知识更新，低于该阈值时需优化embedding模型或索引结构（预期命中率受文档切分粒度影响显著）

## Evidence

[质询]70%的Top-5命中率阈值缺乏普适性的行业标准或第一性原理推导支持，属于特定场景下的经验性设定，不同业务场景（如高精度医疗 vs 低精度闲聊）对有效性的定义差异巨大，该数值可能过于武断。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该阈值为经验参数，非第一性原理可推导）

## Search Query

vector database retrieval hit rate top-5 experimental results embedding model document chunking granularity
