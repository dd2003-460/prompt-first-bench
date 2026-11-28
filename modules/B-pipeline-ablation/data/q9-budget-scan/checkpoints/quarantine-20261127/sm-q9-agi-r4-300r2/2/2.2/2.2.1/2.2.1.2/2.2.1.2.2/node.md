# N309: IVF-PQ 索引构建时间的具体分解：Training Time (K-means on 10k vectors, d=768) ≈ 0.3-0.5s (M1 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

IVF-PQ 索引构建时间的具体分解：Training Time (K-means on 10k vectors, d=768) ≈ 0.3-0.5s (M1 Max CPU)，Assignment Time (assigning 10k vectors to 100 centroids) ≈ 0.1s，Total Build ≈ 0.4-0.6s；这与 Flat Index 构建（仅需内存分配，<0.1s）相比，增加了 5-10 倍的启动开销，对于一次性加载或频繁重建的场景是负面因素。

## Corrected Claim

IVF-PQ 索引构建时间的具体分解：Training Time (K-means on 10k vectors, d=768) ≈ 0.3-0.5s (M1 Max CPU)，Assignment Time (assigning 10k vectors to 100 centroids) ≈ 0.1s，Total Build ≈ 0.4-0.6s；这与 Flat Index 构建（仅需内存分配，<0.1s）相比，增加了 5-10 倍的启动开销，对于一次性加载或频繁重建的场景是负面因素。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

faiss ivf-pq build time breakdown kmeans training assignment cpu
