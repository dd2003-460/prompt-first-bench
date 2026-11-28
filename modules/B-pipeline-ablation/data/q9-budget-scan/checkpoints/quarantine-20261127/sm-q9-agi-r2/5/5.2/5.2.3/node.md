# N78: 本地嵌入相似度匹配算法的具体实现：使用 sentence-transformers/all-MiniLM-L6-v2 (384维) 对生成引用标题与RAG库中标

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

本地嵌入相似度匹配算法的具体实现：使用 sentence-transformers/all-MiniLM-L6-v2 (384维) 对生成引用标题与RAG库中标题进行余弦相似度计算；判定为'正确引用'的阈值阈值 θ_match = 0.92；误报率 FPR(θ=0.92)≈2% (基于10k样本测试集)，漏报率 FNR≈1.5%；单次计算耗时 T_comp≈2ms (M1 Max CPU)，50条引用全量匹配耗时 T_local_match≈100ms。

## Corrected Claim

本地嵌入相似度匹配算法使用 sentence-transformers/all-MiniLM-L6-v2 (384维) 计算余弦相似度，通常设定较高阈值（如0.92）以平衡误报与漏报；在M1 Max CPU上，单次计算耗时通常在毫秒级，50条引用全量匹配耗时在百毫秒级。

## Evidence

[质询]具体性能指标（T_comp≈2ms, T_local_match≈100ms）和误差率（FPR≈2%, FNR≈1.5%）属于高度依赖硬件环境、数据分布及具体实现的经验事实，缺乏通用性，且不同环境下波动较大，难以作为固定事实陈述。 | source=knowledge，逻辑自洽（MiniLM-L6-v2维度384正确，余弦相似度阈值0.92在语义匹配中合理，耗时量级符合CPU推理预期），但具体数值为经验参数，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

sentence-transformers all-MiniLM-L6-v2 cosine similarity threshold false positive rate
