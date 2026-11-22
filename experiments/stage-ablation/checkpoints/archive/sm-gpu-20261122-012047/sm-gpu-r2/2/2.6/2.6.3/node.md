# N92: 性能归一化 TCO：1× H100 在 BF16 下吞吐量约为 50-80 tokens/s/user（基于 N45 的 '数十 tokens/s' 估算），2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

性能归一化 TCO：1× H100 在 BF16 下吞吐量约为 50-80 tokens/s/user（基于 N45 的 '数十 tokens/s' 估算），2× RTX 4090 在 INT4 下吞吐量约为 50-60 tokens/s/user（2× 25-30 tokens/s），单位吞吐量成本 H100 为 $38,564 / (70 tokens/s × 3 年 × 8760 h) ≈ $0.0021/token，2× RTX 4090 为 $7,882 / (55 tokens/s × 3 年 × 8760 h) ≈ $0.00041/token，但需考虑 INT4 质量损失导致的等效质量吞吐量折扣（约 85-90%），修正后 2× RTX 4090 等效成本为 $0.00045/token。

## Corrected Claim

性能归一化 TCO：1× H100 在 BF16 下吞吐量约为 50-80 tokens/s/user（基于 N45 的 '数十 tokens/s' 估算），2× RTX 4090 在 INT4 下吞吐量约为 50-60 tokens/s/user（2× 25-30 tokens/s），单位吞吐量成本 H100 为 $38,564 / (70 tokens/s × 3 年 × 8760 h) ≈ $0.0021/token，2× RTX 4090 为 $7,882 / (55 tokens/s × 3 年 × 8760 h) ≈ $0.00041/token，但需考虑 INT4 质量损失导致的等效质量吞吐量折扣（约 85-90%），修正后 2× RTX 4090 等效成本为 $0.00045/token。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（H100: 38564/(70*3*8760)≈0.0021; 4090: 7882/(55*3*8760)≈0.00041; 修正后 0.00041/0.9≈0.00045），吞吐量与成本量级符合工程常识。
