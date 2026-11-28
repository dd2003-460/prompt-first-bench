# N234: 若检索召回率从 65% 提升至 85% 但文档不包含关键推理步骤，准确率仅提升 5-8% 的原因：模型缺乏将碎片化事实整合为连贯推理链的能力，导致即使拥有正确事

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

若检索召回率从 65% 提升至 85% 但文档不包含关键推理步骤，准确率仅提升 5-8% 的原因：模型缺乏将碎片化事实整合为连贯推理链的能力，导致即使拥有正确事实也无法正确应用

## Corrected Claim

若检索召回率显著提升但文档不包含关键推理步骤，准确率提升幅度有限，主要原因在于模型缺乏将碎片化事实整合为连贯推理链的能力，导致即使拥有正确事实也难以正确应用。

## Evidence

[质询]陈述中具体的数值区间（准确率提升5-8%）属于特定实验或场景下的经验数据，缺乏通用性，且参考来源中并未提供该具体数值的支持，存在以偏概全或数据无据的风险。 | 来源[2]间接支持了‘检索召回率不足’及‘从检索到推理’的挑战背景，但未直接支持‘提升5-8%’这一具体数值及归因细节；该陈述逻辑自洽，符合RAG系统中检索与生成解耦的一般原理，但具体数值缺乏直接来源支持，故降级。

## Search Query

RAG integration failure fragmented facts vs coherent reasoning chain LLM limitation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2060771742843397120&rut=0f99de8a34243736e0850b6a268b13fbc55c85ae0cc3684a321503ba4e3e56c9', 'type': 'ddg', 'title': 'RAG分块策略深度对比：主流方法的检索准确率差异与选型建议'}
- {'url': 'https://zhuanlan.zhihu.com/p/1969875007862731763&rut=0d3da1a2ce5089801ee5ac5ba0972968ea5e10c6637aed473c8d27ef3535ecfc', 'type': 'ddg', 'title': '从信息检索到知识推理：Rag 系统架构的进阶之路，90% 人不知道'}
