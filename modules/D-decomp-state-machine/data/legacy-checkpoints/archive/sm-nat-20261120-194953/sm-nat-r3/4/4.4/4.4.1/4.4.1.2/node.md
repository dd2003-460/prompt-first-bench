# N131: 冷对象驻留时间 T_cold 的解析解：在全量驻留且无容量驱逐下，T_cold 由更新率主导而非访问频率，T_cold ≈ 1/u = 100 天，而非 1/f

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

冷对象驻留时间 T_cold 的解析解：在全量驻留且无容量驱逐下，T_cold 由更新率主导而非访问频率，T_cold ≈ 1/u = 100 天，而非 1/f_cold ≈ 0.0057 天；N58 原假设 T_cold=720h（30天）既不等于 1/u 也不等于 1/f_cold，需修正为 T_cold = 100 天

## Corrected Claim

冷对象驻留时间 T_cold 的解析解：在全量驻留且无容量驱逐下，T_cold 由更新率主导而非访问频率，T_cold ≈ 1/u = 100 天，而非 1/f_cold ≈ 0.0057 天；N58 原假设 T_cold=720h（30天）既不等于 1/u 也不等于 1/f_cold，需修正为 T_cold = 100 天

## Evidence

先验知识/题面给定，逻辑校验通过：在稳态下，对象驻留时间由更新率决定（T=1/u），数值量级合理（1/0.01=100天），且明确指出了原假设与解析解的不一致。
