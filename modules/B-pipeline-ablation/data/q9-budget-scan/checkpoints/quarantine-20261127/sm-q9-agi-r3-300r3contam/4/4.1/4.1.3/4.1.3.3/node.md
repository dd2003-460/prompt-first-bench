# N167: 动态调度修正项：实际调度决策需引入置信度阈值 θ_conf；当模型自评估置信度 < θ_conf（如 0.6）时，无论 L 大小均强制切换至云端 API 或启用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

动态调度修正项：实际调度决策需引入置信度阈值 θ_conf；当模型自评估置信度 < θ_conf（如 0.6）时，无论 L 大小均强制切换至云端 API 或启用多 Agent 投票（N55）；θ_conf 的设定基于历史数据中置信度与最终正确率的相关性，通常取 P(correct|conf)<0.9 对应的置信度分位数

## Corrected Claim

动态调度修正项：实际调度决策需引入置信度阈值 θ_conf；当模型自评估置信度 < θ_conf（如 0.6）时，无论 L 大小均强制切换至云端 API 或启用多 Agent 投票（N55）；θ_conf 的设定基于历史数据中置信度与最终正确率的相关性，通常取 P(correct|conf)<0.9 对应的置信度分位数

## Evidence

先验知识/题面给定，逻辑校验通过
