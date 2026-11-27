# N69: ±20% 扰动场景下的 Ranking 重计算：对于 H100 方案，若 Throughput 下降 20% 至 40 tokens/s，Ranking 从 3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

±20% 扰动场景下的 Ranking 重计算：对于 H100 方案，若 Throughput 下降 20% 至 40 tokens/s，Ranking 从 31.8k/50 = 636 变为 31.8k/40 = 795，排名可能从第 1 降至第 2（若 2×RTX 5090 方案 Ranking 为 750）；若 Throughput 上升 20% 至 60 tokens/s，Ranking 变为 530，优势扩大。此扰动分析需对每个候选方案重复执行。

## Corrected Claim

±20% 扰动场景下的 Ranking 重计算：对于 H100 方案，若 Throughput 下降 20% 至 40 tokens/s，Ranking 从 31.8k/50 = 636 变为 31.8k/40 = 795，排名可能从第 1 降至第 2（若 2×RTX 5090 方案 Ranking 为 750）；若 Throughput 上升 20% 至 60 tokens/s，Ranking 变为 530，优势扩大。此扰动分析需对每个候选方案重复执行。

## Evidence

先验知识/题面给定，逻辑校验通过：31.8k/40=795, 31.8k/60=530, 31.8k/50=636，数值计算准确，逻辑自洽。
