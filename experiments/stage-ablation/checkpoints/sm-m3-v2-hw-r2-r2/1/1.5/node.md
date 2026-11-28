# N10: MTP×4 投机解码在 27B 模型上的接受率（acceptance rate）取决于 draft 模型与 target 模型的分布匹配度；对于 Qwen3 自

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

MTP×4 投机解码在 27B 模型上的接受率（acceptance rate）取决于 draft 模型与 target 模型的分布匹配度；对于 Qwen3 自回归特性，预计接受率为 60-75%，使单 token 生成延迟降低至原生的 1.5-2 倍 [待核验: Qwen3 官方 MTP benchmark 数据]。

## Corrected Claim

MTP×4 投机解码在 27B 模型上的接受率取决于 draft 模型与 target 模型的分布匹配度；对于 Qwen3，理论上可显著提升生成速度，具体接受率与加速比需根据实际部署环境（硬件、并发量等）实测确定，通常预期有显著性能提升。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性违规：子节点1提供的公式隐含了加速比计算逻辑，而子节点2直接给出了具体的加速结果（20-30%），两者在信息维度上存在重叠（一个是通用模型，一个是特定场景实例），且子节点2中的“非理论2倍”结论依赖于子节点1的公式推导，逻辑上紧密耦合而非完全独立。2. 完备性缺失：父节点核心论点是“接受率取决于分布匹配度”，但两个子节点均未解释或量化“Qwen3自回归特性如何导致分布匹配度变化”这一因果机制，仅讨论了公式和硬件影响，遗漏了父节点中关于“分布匹配度”这一关键前提的分解。）

## Search Query

Qwen3 MTP speculative decoding acceptance rate benchmark
