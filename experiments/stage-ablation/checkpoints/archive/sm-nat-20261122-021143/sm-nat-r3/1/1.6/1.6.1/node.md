# N33: 扫描效应偏差 Δ 的量化模型：基于 Belady 算法的最优命中率 H_opt 与 LRU 命中率 H_LRU 的差值，需引入‘工作集波动率’指标，定义为 K 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

扫描效应偏差 Δ 的量化模型：基于 Belady 算法的最优命中率 H_opt 与 LRU 命中率 H_LRU 的差值，需引入‘工作集波动率’指标，定义为 K 随时间变化的方差，Δ ≈ Var(K) / E[K] * (1 - H_ideal)

## Corrected Claim

扫描效应偏差 Δ 的量化可参考基于 Belady 算法的最优命中率 H_opt 与 LRU 命中率 H_LRU 的差值，在特定工作负载下，该差值与工作集波动率（K 随时间变化的方差）及理想命中率存在正相关关系，具体量化模型需结合负载特征校准。

## Evidence

父节点级核验未通过：不完备（子节点1仅处理了稳态特例（Var(K)=0），未覆盖父节点中一般非稳态情况下基于工作集波动率的量化模型；子节点2提出了替代性解释（重引用距离），虽与子节点1在特定假设下不矛盾，但两者共同未能完整构建父节点所述的‘基于Var(K)的量化模型’，反而暗示父节点公式本身可能存在理论缺陷，导致分解未涵盖父节点核心逻辑的通用情况。）

## Search Query

LRU scan effect penalty model
