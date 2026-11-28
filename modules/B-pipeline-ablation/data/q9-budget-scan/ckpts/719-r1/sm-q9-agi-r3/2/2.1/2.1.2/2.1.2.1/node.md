# N145: BGE-large-en-v1.5 在科研摘要上的 Embedding 质量基线：在 MTEB 基准的 Retrieval 子集上，BGE-large 的 nD

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

BGE-large-en-v1.5 在科研摘要上的 Embedding 质量基线：在 MTEB 基准的 Retrieval 子集上，BGE-large 的 nDCG@10 约为 0.55-0.60；针对 Nature/Science 摘要定制微调（LoRA）后，nDCG@10 可提升至 0.65-0.70，对应 Recall@5 提升约 5-8 个百分点

## Corrected Claim

BGE-large-en-v1.5 在 MTEB 基准的 Retrieval 子集上表现良好（具体数值需查阅官方MTEB排行榜）；理论上，针对 Nature/Science 摘要进行 LoRA 微调有望提升检索效果，但具体的 nDCG@10 和 Recall@5 提升幅度需依据实际实验结果确定，现有公开资料未提供确切的 0.65-0.70 区间数据。

## Evidence

[质询]陈述中关于‘针对Nature/Science摘要定制微调（LoRA）后’的具体性能提升数值（nDCG@10提升至0.65-0.70，Recall@5提升5-8个百分点）属于特定实验条件下的经验数据，参考来源仅提供了模型发布和通用微调代码更新信息，未包含任何针对该特定场景的微调实验结果或基准测试数据，存在将通用模型能力或假设性优化效果当作既定事实的风险。 | 来源[1][2]确认了BGE-large-en-v1.5模型的存在及其旨在增强检索能力的特性，间接支持了基线部分的可信度，但完全缺失关于Nature/Science摘要定制微调后具体指标提升的数据支持，属于经验事实且缺乏直接来源佐证。

## Search Query

BGE-large-en-v1.5 MTEB retrieval performance scientific domain fine-tuning nDCG

## Retrieval Sources

- {'url': 'https://huggingface.co/BAAI/bge-large-en&rut=69df175fef0416c35457fef0bc180f5198d2718b4560792a61fe6a3b06048516', 'type': 'ddg', 'title': 'BAAI/bge-large-en · Hugging Face'}
- {'url': 'https://huggingface.co/BAAI/bge-large-en-v1.5&rut=d0dc141fa83dcd008781fcb8c6ac523b5b8b6a2ef3e8a1a4040e1f517a8e8844', 'type': 'ddg', 'title': 'BAAI/bge-large-en-v1.5 · Hugging Face'}
