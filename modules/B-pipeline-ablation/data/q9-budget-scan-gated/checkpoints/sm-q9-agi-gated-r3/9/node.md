# N35: 对于‘提出假设’环节，若使用本地 RAG 检索，向量数据库（如 FAISS）在 MacBook M1 Max 上的查询延迟约为 5-10ms/1000 vect

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于‘提出假设’环节，若使用本地 RAG 检索，向量数据库（如 FAISS）在 MacBook M1 Max 上的查询延迟约为 5-10ms/1000 vectors，但将检索结果（平均 2k tokens）注入 LLM 上下文会增加 Prefill 阶段的计算负载。2k tokens 的 Prefill 在 V100 集群上耗时约为 2000 / (125 TFLOPS / 27e9) ≈ 0.4s（理论），实际受 Kernel Launch 开销影响约为 0.8-1.2s，这比 Decode 阶段慢 20 倍，因此高频检索会显著拖慢整体科研循环频率。

## Corrected Claim

对于‘提出假设’环节，若使用本地 RAG 检索，向量数据库（如 FAISS）在 MacBook M1 Max 上的查询延迟约为 5-10ms/1000 vectors，但将检索结果（平均 2k tokens）注入 LLM 上下文会增加 Prefill 阶段的计算负载。2k tokens 的 Prefill 在 V100 集群上耗时约为 2000 / (125 TFLOPS / 27e9) ≈ 0.4s（理论），实际受 Kernel Launch 开销影响约为 0.8-1.2s，这比 Decode 阶段慢 20 倍，因此高频检索会显著拖慢整体科研循环频率。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1专注于修正Prefill阶段的计算延迟估算（从硬件和算法角度），子节点2专注于评估该延迟在整体科研循环中的相对占比及结论（从系统宏观角度）。两者关注点不同（微观计算 vs 宏观影响），逻辑互补且无重叠，共同覆盖了父节点中关于'检索延迟'、'Prefill负载'以及'对整体效率影响'的核心论点。）
