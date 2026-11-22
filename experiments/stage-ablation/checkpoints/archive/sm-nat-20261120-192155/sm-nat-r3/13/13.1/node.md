# N150: 折扣因子 D 的精确计算依赖于 T_res_avg 的实际数值，该值由缓存容量 C=128GB 与缓存内驻留对象的总字节吞吐量 R_bytes_cached 决

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

折扣因子 D 的精确计算依赖于 T_res_avg 的实际数值，该值由缓存容量 C=128GB 与缓存内驻留对象的总字节吞吐量 R_bytes_cached 决定，公式为 T_res_avg = C / R_bytes_cached，需代入 N8 确定的 k 值计算 R_bytes_cached。

## Corrected Claim

折扣因子 D 的精确计算依赖于 T_res_avg 的实际数值，该值由缓存容量 C=128GB 与缓存内驻留对象的总字节吞吐量 R_bytes_cached 决定，公式为 T_res_avg = C / R_bytes_cached，需代入 N8 确定的 k 值计算 R_bytes_cached。

## Evidence

先验知识/题面给定，逻辑校验通过：平均驻留时间等于容量除以吞吐量符合基本物理/数学定义（T = Volume / Rate），量纲一致（GB / (GB/s) = s），且明确指出了依赖关系（需代入N8的k值），逻辑自洽。
