# N296: 外部状态存储的存储容量 S_total = N_hypotheses * N_params_per_hyp * Bytes_per_param；假设单条假设包含

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105, N106, N107

## Claim

外部状态存储的存储容量 S_total = N_hypotheses * N_params_per_hyp * Bytes_per_param；假设单条假设包含 50 个关键参数，每个参数序列化后约 1KB，运行 100 个假设时 S_total = 100 * 50 * 1KB = 5MB，远低于 FAISS 索引或 Neo4j 的单机内存限制 (16GB+)，因此存储瓶颈可忽略，主要瓶颈在检索效率。

## Corrected Claim

外部状态存储的存储容量 S_total = N_hypotheses * N_params_per_hyp * Bytes_per_param；假设单条假设包含 50 个关键参数，每个参数序列化后约 1KB，运行 100 个假设时 S_total = 100 * 50 * 1KB = 5MB，远低于 FAISS 索引或 Neo4j 的单机内存限制 (16GB+)，因此存储瓶颈可忽略，主要瓶颈在检索效率。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（100*50*1KB=5MB），5MB远小于16GB内存限制，结论符合工程常识。

## Search Query

vector database storage capacity estimation scientific hypothesis tracking
