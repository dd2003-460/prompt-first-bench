# N206: 样本量扩展的成本-收益函数：扩大样本量至 n_new 的额外推理成本 ΔC = (n_new - n_old) * C_sample_inference；若 C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

样本量扩展的成本-收益函数：扩大样本量至 n_new 的额外推理成本 ΔC = (n_new - n_old) * C_sample_inference；若 C_sample_inference = $0.01/sample (云端 API)，且质量提升 ΔQ = 0.05 (5% 准确率提升)，则 ROI = ΔQ / ΔC；当 n_old=30, n_new=100 时，ΔC=$0.7, ROI≈0.07/$，需与本地推理成本对比决定是否值得

## Corrected Claim

样本量扩展的成本-收益函数：扩大样本量至 n_new 的额外推理成本 ΔC = (n_new - n_old) * C_sample_inference；若 C_sample_inference = $0.01/sample (云端 API)，且质量提升 ΔQ = 0.05 (5% 准确率提升)，则 ROI = ΔQ / ΔC；当 n_old=30, n_new=100 时，ΔC=$0.7, ROI≈0.07/$，需与本地推理成本对比决定是否值得

## Evidence

[质询]ROI 的定义通常涉及收益（货币化价值）与成本的比率，此处将质量提升（无量纲或百分点）直接除以成本（美元）得到 '0.07/$'，量纲上并非标准经济学 ROI，而是单位成本的质量增益指标；此外，$0.01/sample 是假设值而非固定事实。 | 先验知识/题面给定，逻辑校验通过：算术计算正确（(100-30)*0.01=0.7, 0.05/0.7≈0.0714），作为成本-收益分析框架的逻辑自洽，符合 knowledge 节点判定规则。
