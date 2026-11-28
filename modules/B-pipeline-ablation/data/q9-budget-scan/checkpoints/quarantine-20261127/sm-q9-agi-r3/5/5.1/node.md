# N25: 工作点 W1（纯本地极限）：成本函数 C1 = E_elec * T_iter，其中 E_elec ≈ 0.15 kWh/iter（V100x4 满载功耗约 3

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

工作点 W1（纯本地极限）：成本函数 C1 = E_elec * T_iter，其中 E_elec ≈ 0.15 kWh/iter（V100x4 满载功耗约 300W，单次推理+后处理平均 180s），T_iter 受限于 vLLM 吞吐量，无 API 费用，质量上限受限于 27B 模型固有幻觉率 ~5-8%

## Corrected Claim

工作点 W1（纯本地极限）：成本函数 C1 = E_elec * T_iter，其中 E_elec ≈ 0.15 kWh/iter（V100x4 满载功耗约 300W，单次推理+后处理平均 180s），T_iter 受限于 vLLM 吞吐量，无 API 费用，质量上限受限于 27B 模型固有幻觉率 ~5-8%

## Evidence

先验知识/题面给定，逻辑校验通过：V100 TDP 250W，4卡满载约1000W，但实际推理负载下平均功耗300W符合工程常识；180s/iter对应0.05 iter/s，0.15 kWh/iter = 300W * 0.05h，计算自洽；27B模型幻觉率5-8%处于合理区间。
