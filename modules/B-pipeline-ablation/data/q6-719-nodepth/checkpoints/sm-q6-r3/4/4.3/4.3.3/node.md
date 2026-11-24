# N111: 混合策略路由决策逻辑函数：Route(user_ip, object_id) = IF (GeoIP(user_ip) IN Core_Zones AND Q_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

混合策略路由决策逻辑函数：Route(user_ip, object_id) = IF (GeoIP(user_ip) IN Core_Zones AND Q_obj_24h(object_id) > H_threshold) THEN Self_POP ELSE Public_CDN，该逻辑决定了 P_core 的实际取值及流量分配比例。

## Corrected Claim

混合策略路由决策逻辑函数：Route(user_ip, object_id) = IF (GeoIP(user_ip) IN Core_Zones AND Q_obj_24h(object_id) > H_threshold) THEN Self_POP ELSE Public_CDN，该逻辑决定了 P_core 的实际取值及流量分配比例。

## Evidence

父节点级核验未通过：不完备（子节点分别聚焦于地理边界定义、定位误差影响和热度计算开销，彼此独立且无重叠，正交性良好。但父节点核心在于“流量分配比例”及“P_core实际取值”的最终决策逻辑，现有子节点仅拆解了输入参数（GeoIP, Q_obj）和约束（Core_Zones），缺失了核心判断条件（H_threshold）的确定机制以及最终路由决策（Self_POP vs Public_CDN）的具体执行逻辑或成本收益权衡模型，导致对父节点关键决策过程的覆盖不完备。）
