# N72: 解析耗时的线性拟合公式：T_parse = T_base + α * N_pages + β * N_tables；基于 arXiv 数据集回归，T_base=

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

解析耗时的线性拟合公式：T_parse = T_base + α * N_pages + β * N_tables；基于 arXiv 数据集回归，T_base=0.5s, α=0.3s/page, β=1.2s/table；对于平均 15 页、3 个表格的论文，T_parse = 0.5 + 15*0.3 + 3*1.2 = 7.1s；若启用 GPU 加速 OCR（M1 Max 不支持，需云端），α 可降至 0.1s/page，T_parse 降至 4.1s，但引入网络延迟 T_net=0.5s，总耗时 4.6s。

## Corrected Claim

解析耗时的线性拟合公式形式为 T_parse = T_base + α * N_pages + β * N_tables。基于某数据集回归得到的示例参数下，对于平均 15 页、3 个表格的论文，计算耗时约为 7.1s；若启用云端 GPU 加速 OCR 并计入网络延迟，总耗时可能降至约 4.6s（具体数值取决于实际回归系数和网络状况）。

## Evidence

[质询]该陈述包含具体的经验回归系数（T_base=0.5s, α=0.3s/page, β=1.2s/table）及特定硬件（M1 Max）的性能假设，这些属于经验事实而非第一性原理可推导内容，且缺乏外部来源验证其准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PDF parsing time linear regression page count table count coefficient
