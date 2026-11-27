# N77: 修正后的 INT8 显存占用：若 Embedding (0.68B params) 保持 BF16 (1.36 GB)，其余 26.5B params 为 IN

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

修正后的 INT8 显存占用：若 Embedding (0.68B params) 保持 BF16 (1.36 GB)，其余 26.5B params 为 INT8 (26.5 GB)，总权重显存 ≈ 27.86 GB (略高于 N13 的 27 GB 估算)。

## Corrected Claim

修正后的 INT8 显存占用：若 Embedding (0.68B params) 保持 BF16 (1.36 GB)，其余 26.5B params 为 INT8 (26.5 GB)，总权重显存 ≈ 27.86 GB (略高于 N13 的 27 GB 估算)。

## Evidence

父节点级核验未通过：不完备（1. 数据矛盾：父节点明确给出 Embedding 为 0.68B params (1.36 GB)，总显存 27.86 GB；但子节点1修正为 0.62B params (1.16 GB)，总显存 27.54 GB。子节点与父节点在核心参数（Embedding 大小）和最终结果上不一致，违反了分解的一致性原则。2. 完备性缺失：父节点主要陈述‘显存占用’及与 N13 的对比，子节点1-2 扩展了部署可行性（KV Cache、单卡限制），这超出了‘显存占用’这一单一维度的范畴，引入了新的评估维度（可行性/延迟），虽然逻辑相关，但严格来说子节点引入了父节点未提及的额外假设（如 KV Cache 大小、PCIe 带宽），导致分解范围发散。）
