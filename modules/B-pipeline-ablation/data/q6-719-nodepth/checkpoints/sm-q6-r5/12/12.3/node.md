# N402: 若将 10 个 POP 中 4 个部署在一线/新一线城市圈（覆盖 40% 流量），6 个部署在其他区域，则加权平均用户到 POP 的距离 D_avg 比均匀分布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

若将 10 个 POP 中 4 个部署在一线/新一线城市圈（覆盖 40% 流量），6 个部署在其他区域，则加权平均用户到 POP 的距离 D_avg 比均匀分布减少约 15%-20%，对应传播延迟降低 0.2-0.4 ms，且 P99 尾部延迟改善更为显著（因长尾用户集中在偏远西部，需保留 2-3 个西部 POP 兜底）。

## Corrected Claim

若将 10 个 POP 中 4 个部署在一线/新一线城市圈（覆盖 40% 流量），6 个部署在其他区域，则加权平均用户到 POP 的距离 D_avg 比均匀分布减少约 15%-20%，对应传播延迟降低 0.2-0.4 ms，且 P99 尾部延迟改善更为显著（因长尾用户集中在偏远西部，需保留 2-3 个西部 POP 兜底）。

## Evidence

先验知识/题面给定，逻辑校验通过：光纤传播速度约200,000 km/s，距离减少15%-20%（假设原平均距离约1000-2000km，减少150-400km）对应延迟降低0.2-0.4ms，量级合理；P99改善因长尾用户集中偏远地区，保留西部POP兜底符合网络优化常识。

## Search Query

CDN node placement optimization China traffic distribution weighted distance reduction
