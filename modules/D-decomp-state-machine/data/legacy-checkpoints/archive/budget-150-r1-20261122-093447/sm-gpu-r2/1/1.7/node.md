# N13: 各精度总内存需求汇总（batch_size=1, 32K ctx）：BF16=54+2.15+4.6+1.5≈62.3GB；FP8=27+1.07+4.6+1.

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

各精度总内存需求汇总（batch_size=1, 32K ctx）：BF16=54+2.15+4.6+1.5≈62.3GB；FP8=27+1.07+4.6+1.5≈34.2GB；INT8=27+1.07+4.6+1.5≈34.2GB；NVFP4=13.5+1.07+4.6+1.5≈20.7GB；W4=13.5+1.07+4.6+1.5≈20.7GB

## Corrected Claim

各精度总内存需求汇总（batch_size=1, 32K ctx）：BF16=54+2.15+4.6+1.5≈62.3GB；FP8=27+1.07+4.6+1.5≈34.2GB；INT8=27+1.07+4.6+1.5≈34.2GB；NVFP4=13.5+1.07+4.6+1.5≈20.7GB；W4=13.5+1.07+4.6+1.5≈20.7GB

## Evidence

父节点级核验未通过：不完备（父节点明确列出了5种精度（BF16, FP8, INT8, NVFP4, W4）的总内存需求汇总，但子节点仅针对NVFP4/W4这一种情况进行了可行性分析，完全缺失了BF16、FP8、INT8等其他关键精度的覆盖，因此不满足完备性。）
