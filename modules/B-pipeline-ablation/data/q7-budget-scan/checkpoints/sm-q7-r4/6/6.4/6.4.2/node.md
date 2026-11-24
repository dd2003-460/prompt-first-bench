# N335: 扩展HDD池的年化新增运营支出计算：ΔC_op_new = (Power_Cost_Increment + Maintenance_Labor_Incremen

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

扩展HDD池的年化新增运营支出计算：ΔC_op_new = (Power_Cost_Increment + Maintenance_Labor_Increment + Rack_Space_Increment)；假设12块HDD新增功耗约60W，电费增量 = 0.06kW * 1.4(PUE) * 0.8(¥/kWh) * 8760h ≈ ¥584/年；新增维护人力假设0.1 FTE，成本 = 0.1 * ¥200,000 = ¥20,000/年；合计约¥20,584/年。

## Corrected Claim

扩展HDD池的年化新增运营支出计算：ΔC_op_new = (Power_Cost_Increment + Maintenance_Labor_Increment + Rack_Space_Increment)；假设12块HDD新增功耗约60W，电费增量 = 0.06kW * 1.4(PUE) * 0.8(¥/kWh) * 8760h ≈ ¥584/年；新增维护人力假设0.1 FTE，成本 = 0.1 * ¥200,000 = ¥20,000/年；合计约¥20,584/年。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算 0.06*1.4*0.8*8760=584.64≈584，人力成本 0.1*200000=20000，合计 20584，数值量级与逻辑均合理。
