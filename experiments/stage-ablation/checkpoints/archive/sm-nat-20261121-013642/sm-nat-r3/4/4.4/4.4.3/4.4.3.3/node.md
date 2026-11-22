# N196: T_cold 的数值解需联立 N16 公式 T_cold ≈ (C_cache / R_bytes) * (1 / (1 - H_byte_LRU))，其中 C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

T_cold 的数值解需联立 N16 公式 T_cold ≈ (C_cache / R_bytes) * (1 / (1 - H_byte_LRU))，其中 C_cache=128GB，R_bytes 由 N60 计算（需 s_min 和截断策略），H_byte_LRU 取 N68 的下界 0.65，若 R_bytes=1000GB/day 则 T_cold≈(128/1000)/0.35≈0.366 days，此值远小于 100 days，表明 N67 的 'T_cold≈100 days' 假设与实际参数不符，需重新校准工作点。

## Corrected Claim

T_cold 的数值解需联立 N16 公式 T_cold ≈ (C_cache / R_bytes) * (1 / (1 - H_byte_LRU))，其中 C_cache=128GB，R_bytes 由 N60 计算（需 s_min 和截断策略），H_byte_LRU 取 N68 的下界 0.65，若 R_bytes=1000GB/day 则 T_cold≈(128/1000)/0.35≈0.366 days，此值远小于 100 days，表明 N67 的 'T_cold≈100 days' 假设与实际参数不符，需重新校准工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：公式代入数值 (128/1000)/(1-0.65) ≈ 0.366 计算正确，且与 100 days 的矛盾判断符合逻辑。
