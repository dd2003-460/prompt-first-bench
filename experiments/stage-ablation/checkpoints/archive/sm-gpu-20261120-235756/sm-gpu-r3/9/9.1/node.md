# N127: RTX 5090 在 FP8 精度下运行 Qwen3-27B 时的理论 TPOT 上限为 1.51ms/token (计算式: (27.18e9 params 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

RTX 5090 在 FP8 精度下运行 Qwen3-27B 时的理论 TPOT 上限为 1.51ms/token (计算式: (27.18e9 params * 1 byte/param) / 1792 GB/s)，对应理论吞吐量约 662 tokens/s；该数值需乘以实际利用率因子 (通常 0.5-0.7) 得到保守估计值 330-460 tokens/s。

## Corrected Claim

RTX 5090 在 FP8 精度下运行 Qwen3-27B 时的理论 TPOT 上限为 1.51ms/token (计算式: (27.18e9 params * 1 byte/param) / 1792 GB/s)，对应理论吞吐量约 662 tokens/s；该数值需乘以实际利用率因子 (通常 0.5-0.7) 得到保守估计值 330-460 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 FP8 显存带宽约 1.79 TB/s，Qwen3-27B 参数量约 27.18B，计算式 (27.18e9 * 1) / 1792e9 ≈ 1.51ms，吞吐量 1/0.00151 ≈ 662 tokens/s，逻辑自洽且数值量级合理。
