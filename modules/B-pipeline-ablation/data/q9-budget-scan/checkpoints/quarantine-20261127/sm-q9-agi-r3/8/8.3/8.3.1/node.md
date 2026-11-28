# N279: LLMLingua-2 在压缩比 2x 时，对 Qwen3.8-27B 生成的复杂推理链中逻辑连接词（如'因此'、'但是'、'鉴于'）的保留率为 92%，导致推

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

LLMLingua-2 在压缩比 2x 时，对 Qwen3.8-27B 生成的复杂推理链中逻辑连接词（如'因此'、'但是'、'鉴于'）的保留率为 92%，导致推理链断裂率上升约 3%，低于父节点估算的 5-10%。

## Corrected Claim

LLMLingua-2 在 2x 压缩比下能保持较高的任务性能，但关于其对特定模型（如 Qwen 系列）生成内容中逻辑连接词的具体保留率及推理链断裂率的精确数值，现有参考来源未提供直接证据。

## Evidence

[质询]该陈述包含极其具体的经验数据（Qwen3.8-27B模型、92%保留率、3%断裂率），这些具体数值和特定模型组合在提供的参考来源中完全缺失，且‘Qwen3.8-27B’这一型号本身存疑（通常Qwen系列有7B/14B/72B等，3.8B或27B非标准公开命名，可能是幻觉或笔误），属于高风险的经验事实断言。 | 参考来源[1][2][3]仅证实LLMLingua-2的存在及其通用压缩能力（2x-5x压缩比，性能保持），但未提供针对特定模型（Qwen3.8-27B）的逻辑连接词保留率或推理链断裂率的微观统计数据，属于经验事实且缺乏直接来源支持。

## Search Query

LLMLingua-2 compression ratio logical connector retention rate reasoning chain breakage

## Retrieval Sources

- {'url': 'https://github.com/microsoft/LLMLingua&rut=7f00da447690eee0b1548287cbb39f8e104cd476a20c42e7cc48218c131f0518', 'type': 'ddg', 'title': "GitHub - microsoft/LLMLingua: [EMNLP'23, ACL'24] To speed up LLMs ..."}
- {'url': 'https://zhuanlan.zhihu.com/p/688994499&rut=137dede0a38d60cb80c2b79508cf7d0228d7166836033e8a032e712623ce1211', 'type': 'ddg', 'title': '今日大模型论文 清华&微软联合打造LLMLingua2，速度提升达2.9倍'}
- {'url': 'https://arxiv.org/abs/2403.12968&rut=345e2560076d23636e98d1a9f8302852d49e13b9d1eb3a6e0ff10aef97275a31', 'type': 'ddg', 'title': '[2403.12968] LLMLingua-2: Data Distillation for Efficient and Faithful ...'}
