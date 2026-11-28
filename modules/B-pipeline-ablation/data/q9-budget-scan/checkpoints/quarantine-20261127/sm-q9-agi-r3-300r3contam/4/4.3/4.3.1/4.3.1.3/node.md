# N173: 27B 模型在 Research-AGI 任务上的未校准 ECE 基线值需通过构建 500 个 (query, ground_truth, confidence

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

27B 模型在 Research-AGI 任务上的未校准 ECE 基线值需通过构建 500 个 (query, ground_truth, confidence) 三元组实测获得，若 ECE_unadjusted > 20%，则校准前的阈值 τ 失效风险极高。

## Corrected Claim

27B 模型在 Research-AGI 任务上的未校准 ECE 基线值需通过构建 500 个 (query, ground_truth, confidence) 三元组实测获得；若 ECE_unadjusted 显著偏高（如超过 20%），则表明模型置信度校准较差，直接使用原始置信度作为阈值 τ 的风险较高。

## Evidence

[质询]该陈述包含具体的经验性阈值（ECE > 20% 导致阈值失效风险极高）和特定的实验设置（500个三元组），这些属于经验事实，无法从第一性原理推导，且参考来源完全未涉及校准误差（ECE）或 Research-AGI 任务的具体指标。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅讨论政治倾向评分，与ECE校准无关）

## Search Query

qwen 27b calibration error ece baseline research tasks

## Retrieval Sources

- {'url': 'https://huggingface.co/NousResearch/Arete-27B/discussions/64&rut=de007f67b17be26a5967ff2fb6184ec72ab11d38dd5c0d8716d6aef1828b9bc6', 'type': 'ddg', 'title': 'NousResearch/Arete-27B · Introducing FuckNous-27B: Arete-27B, post ...'}
