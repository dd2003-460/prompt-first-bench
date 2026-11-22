# N94: 工作点 B2 (中性价比/平衡)：1x A100 80GB (HBM2e, 2039 GB/s) 运行 FP8 Qwen3-27B (27GB) + BF16 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

工作点 B2 (中性价比/平衡)：1x A100 80GB (HBM2e, 2039 GB/s) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.58GB) = 39.58GB < 80GB。理论 Decode 上限 ≈ 2039 GB/s / 27 GB ≈ 75.5 tokens/s。CapEx ≈ $15,000 (二手/现货)。

## Corrected Claim

工作点 B2 (中性价比/平衡)：1x A100 80GB (HBM2e, 2039 GB/s) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.58GB) = 39.58GB < 80GB。理论 Decode 上限 ≈ 2039 GB/s / 27 GB ≈ 75.5 tokens/s。CapEx ≈ $15,000 (二手/现货)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于硬件兼容性修正（技术/性能维度），子节点2聚焦于基于修正后性能的TCO与性价比分析（经济/决策维度）。两者逻辑上存在依赖关系（2依赖1的结论），但主题不重叠，无矛盾，且共同覆盖了父节点中关于性能上限和成本评估的两个核心方面。）
