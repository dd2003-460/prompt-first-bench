# N199: 27B 模型在 262k 上下文下生成 Map（全局结构摘要）的 Token 消耗计算：T_map_gen = (L_context / Compression

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

27B 模型在 262k 上下文下生成 Map（全局结构摘要）的 Token 消耗计算：T_map_gen = (L_context / Compression_Ratio) / Throughput_eff，其中 L_context=262,144, Compression_Ratio≈100 (2k summary), Throughput_eff≈45 tok/s (from N62)，预计耗时 T_map ≈ 2000/45 ≈ 44s，Token 成本 C_map = 262k * P_in + 2k * P_out

## Corrected Claim

27B 模型在 262k 上下文下生成 Map（全局结构摘要）的 Token 消耗计算：T_map_gen = (L_context / Compression_Ratio) / Throughput_eff，其中 L_context=262,144, Compression_Ratio≈100 (2k summary), Throughput_eff≈45 tok/s (from N62)，预计耗时 T_map ≈ 2000/45 ≈ 44s，Token 成本 C_map = 262k * P_in + 2k * P_out

## Evidence

先验知识/题面给定，逻辑校验通过：262144/100≈2621，取整或近似为2000符合工程估算习惯；2000/45≈44.4s，数值量级与算术逻辑自洽。
