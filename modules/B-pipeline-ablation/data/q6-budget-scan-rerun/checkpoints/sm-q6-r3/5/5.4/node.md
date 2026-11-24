# N32: T、s、geo_share 的联合敏感性分析范围：定义三维参数空间 (T, s, geo_share)，T ∈ [100ms, 500ms]，s ∈ [100K

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

T、s、geo_share 的联合敏感性分析范围：定义三维参数空间 (T, s, geo_share)，T ∈ [100ms, 500ms]，s ∈ [100KB, 5MB]，geo_share ∈ {均匀分布, Zipf(α=1.0), Zipf(α=1.5)}，共 5×5×3=75 个组合点，对每个组合点计算三种策略的每千请求 P99 成本 C_strategy(T, s, geo_share)，输出 75×3 的成本矩阵，用于判断哪个策略在大多数参数组合下最划算。

## Corrected Claim

T、s、geo_share 的联合敏感性分析范围：定义三维参数空间 (T, s, geo_share)，T ∈ [100ms, 500ms]，s ∈ [100KB, 5MB]，geo_share ∈ {均匀分布, Zipf(α=1.0), Zipf(α=1.5)}，共 5×5×3=75 个组合点，对每个组合点计算三种策略的每千请求 P99 成本 C_strategy(T, s, geo_share)，输出 75×3 的成本矩阵，用于判断哪个策略在大多数参数组合下最划算。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应敏感性分析的‘输入定义（采样网格）’、‘输出处理（决策规则）’和‘深入分析（耦合效应）’，逻辑上层层递进且互不重叠。子节点1严格对应父节点中的参数空间定义；子节点2对应‘用于判断哪个策略...最划算’的目标；子节点3补充了父节点隐含的‘高维参数空间’分析需求（虽然父节点未显式提及耦合，但在学术分解中，对连续变量的敏感性分析通常包含交互效应检查，且该节点未与前两者矛盾，而是提供了更深层的洞察维度，视为对‘分析范围’的深度补充而非冗余）。）

## Search Query

joint sensitivity analysis T s geographic distribution 75 combinations cost matrix CDN strategy comparison
