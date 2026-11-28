# N307: 16GB RAM 约束下的向量库容量上限：单个 768-dim float32 向量占用 3KB。16GB 可用内存约 12GB (预留 OS/Python)。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

16GB RAM 约束下的向量库容量上限：单个 768-dim float32 向量占用 3KB。16GB 可用内存约 12GB (预留 OS/Python)。最大可存储向量数 N_max = 12e9 / 3000 ≈ 4,000,000。若需支持 100 万级知识库，Flat IP 索引本身占 3GB，配合 IVF-PQ 压缩 (4x 压缩率) 可降至 0.75GB，但召回率会从 100% 降至 ~95%；鉴于 N=10k 远小于 N_max，Flat IP 在内存上完全可行，无需压缩。

## Corrected Claim

16GB RAM 约束下的向量库容量上限：单个 768-dim float32 向量占用 3KB。16GB 可用内存约 12GB (预留 OS/Python)。最大可存储向量数 N_max = 12e9 / 3000 ≈ 4,000,000。若需支持 100 万级知识库，Flat IP 索引本身占 3GB，配合 IVF-PQ 压缩 (4x 压缩率) 可降至 0.75GB，但召回率会从 100% 降至 ~95%；鉴于 N=10k 远小于 N_max，Flat IP 在内存上完全可行，无需压缩。

## Evidence

[质询]IVF-PQ 4x 压缩率下召回率降至 ~95% 的具体数值缺乏通用标准，可能因数据集分布而异，但在工程估算中属于合理量级。 | 先验知识/题面给定，逻辑校验通过：768*4=3072B≈3KB，12GB/3KB≈4M，1M*3KB=3GB，3GB/4=0.75GB，计算均正确且符合内存管理常识。

## Search Query

vector database memory capacity limit 16GB RAM FAISS flat vs IVF PQ tradeoff
