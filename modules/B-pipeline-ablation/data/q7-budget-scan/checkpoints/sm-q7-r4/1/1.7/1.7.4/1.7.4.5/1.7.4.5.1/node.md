# N430: 泊松分布参数 λ 的推导公式：λ = (N_objects_cold * f_scan_daily * p_hit_rate) / 24，其中 N_object

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N189

## Claim

泊松分布参数 λ 的推导公式：λ = (N_objects_cold * f_scan_daily * p_hit_rate) / 24，其中 N_objects_cold 为冷数据对象总数，f_scan_daily 为每日全量扫描次数（1-2次），p_hit_rate 为单次扫描命中的对象比例（通常<1%）。若假设 500TB 冷数据由 500M 个 1KB 对象组成，每日扫描 1 次，命中率 0.1%，则 λ = (500,000,000 * 1 * 0.001) / 24 ≈ 20,833 次/小时，远超 N189 声称的 0.1 次/小时，表明 N189 的 0.1 次/小时仅适用于极端稀疏访问或大对象（如 1TB/对象）场景，需根据实际对象粒度修正。

## Corrected Claim

泊松分布参数 λ 的推导公式：λ = (N_objects_cold * f_scan_daily * p_hit_rate) / 24，其中 N_objects_cold 为冷数据对象总数，f_scan_daily 为每日全量扫描次数（1-2次），p_hit_rate 为单次扫描命中的对象比例（通常<1%）。若假设 500TB 冷数据由 500M 个 1KB 对象组成，每日扫描 1 次，命中率 0.1%，则 λ = (500,000,000 * 1 * 0.001) / 24 ≈ 20,833 次/小时，远超 N189 声称的 0.1 次/小时，表明 N189 的 0.1 次/小时仅适用于极端稀疏访问或大对象（如 1TB/对象）场景，需根据实际对象粒度修正。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（500M * 1 * 0.001 / 24 ≈ 20,833），量纲与推导逻辑自洽，符合泊松分布参数定义。
