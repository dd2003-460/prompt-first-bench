# N151: Qwen3-27B 在 MMLU 基准测试中，BF16 基线准确率为 82.5%，INT8 量化后准确率为 81.8%（下降 0.7%），W4A16 量化后准确

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

Qwen3-27B 在 MMLU 基准测试中，BF16 基线准确率为 82.5%，INT8 量化后准确率为 81.8%（下降 0.7%），W4A16 量化后准确率为 79.2%（下降 3.3%），证实 INT8 损失可忽略，但 4-bit 损失显著，需根据业务容忍阈值（如 <2%）排除 W4A16 方案。

## Corrected Claim

Qwen3-27B 在 MMLU 基准测试中，INT8 量化通常带来可忽略的精度损失（约 <1%），而 4-bit 量化（如 W4A16）通常导致显著精度下降（约 3% 左右），具体数值需依据特定量化算法和评测集确认。

## Evidence

[质询]参考来源[2]提到的模型版本为'Qwen3.8-27B'且量化方法为'GSQ-RCO'（2.75bpw），与陈述中的'Qwen3-27B'及标准'INT8/W4A16'量化方案在版本和具体技术细节上存在不一致，且来源未提供MMLU单项基准的具体数值，无法直接证实82.5%、81.8%、79.2%这些精确数值。 | 逻辑上INT8精度损失小于4-bit符合量化常识，但来源[2]仅提及综合评测得分反超BF16，未提供MMLU具体准确率数值，且模型版本号（Qwen3.8 vs Qwen3）存在差异，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B MMLU benchmark accuracy BF16 vs INT8 vs W4A16 quantization drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00746/article/details/168243374&rut=b94390f20870f7a819ad544a532561155af080c6b32f62a0ec6f1c43c07bb370', 'type': 'ddg', 'title': 'Qwen3.8-27B-MTP-bf16推测解码实战：MTP草稿模型到底快多少？完整基准测试对比指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=8d101b892bffb46b87003cdc8ef3a4d74fd9cad312ea5acd751e7c426bb2b5fe', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
