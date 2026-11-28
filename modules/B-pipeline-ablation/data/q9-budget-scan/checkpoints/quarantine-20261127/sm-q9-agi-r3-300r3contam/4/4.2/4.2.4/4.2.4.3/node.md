# N170: T_aggregation 并非固定 0.5s，而是取决于投票算法复杂度，若采用加权多数表决，T_agg = O(N * C_token_comparison)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

T_aggregation 并非固定 0.5s，而是取决于投票算法复杂度，若采用加权多数表决，T_agg = O(N * C_token_comparison)，需实测在 N=5 时对 512-token 输出的语义相似度比对耗时。

## Corrected Claim

T_aggregation 并非固定值，其耗时取决于投票算法复杂度及单次语义相似度比对的开销；若采用基于LLM判断的加权多数表决，复杂度通常与候选数量N及单次比对成本正相关，具体耗时需根据实际模型规模和输入长度实测确定。

## Evidence

[质询]该陈述包含具体的工程实现细节（如“512-token”、“N=5”的具体耗时预期及特定复杂度公式），这些属于经验事实或特定系统配置，无法从第一性原理严格推导，且参考来源中未提供对应的实测数据或具体参数支持。 | 来源[2]间接支持了聚合框架涉及LLM比较（LLM-as-a-judge）及加权聚合方法，证实了复杂度依赖于比较操作这一逻辑方向，但未提供N=5、512-token下的具体耗时或精确复杂度公式，属于经验事实缺来源直接支持。

## Search Query

llm voting aggregation latency cost semantic similarity comparison time

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2027122063182185573&rut=907d51a5a6d291589a55955006ec6a1964e4fd39354d96a30eaadfeac075af2b', 'type': 'ddg', 'title': '长文总结：近两年大模型 Test-Time-Scaling 的八大主流方向'}
- {'url': 'https://arxiv.org/pdf/2605.06219&rut=2ab6b7bc9c2ffdef12425108f927bf00e81c166029b062046ce1d8adf7dd053b', 'type': 'ddg', 'title': 'Joint Consistency: A Unified Test-Time Aggregation Framework via Energy ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/2056510824508815297&rut=15c21be6af6b71f5ef11e22f80b2f31ff46cc83298386a99ee0ad87726666238', 'type': 'ddg', 'title': 'Test-Time Scaling 与推理时计算：搜索、验证器、反思和自一致性'}
