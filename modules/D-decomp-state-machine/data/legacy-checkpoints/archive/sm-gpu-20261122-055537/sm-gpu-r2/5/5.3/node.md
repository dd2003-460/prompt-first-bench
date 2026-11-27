# N26: 工作点2 (中性价比最优/平衡点)：使用单张 NVIDIA L4 (24GB) 或 A10 (24GB) 数据中心卡运行 FP8/INT8 量化。量化依据：L4

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点2 (中性价比最优/平衡点)：使用单张 NVIDIA L4 (24GB) 或 A10 (24GB) 数据中心卡运行 FP8/INT8 量化。量化依据：L4/A10 显存 24GB 同 4090，但功耗更低 (~75W-150W)，适合长期低负载运行。性能预估：~20-30 tokens/s，质量损失 Q_score ~0.98 (FP8/INT8 精度高于 INT4)，电力成本显著低于 4090。

## Corrected Claim

工作点2 (中性价比最优/平衡点)：使用单张 NVIDIA L4 (24GB) 或 A10 (24GB) 数据中心卡运行 FP8/INT8 量化。量化依据：L4/A10 显存 24GB 同 4090，但功耗更低 (~75W-150W)，适合长期低负载运行。性能预估：取决于模型规模，通常低于同显存消费级卡（如4090）的峰值吞吐，但能效比更高；质量损失 Q_score 通常接近 1.0 (FP8/INT8 精度高于 INT4)，电力成本显著低于 4090。

## Evidence

[质询]性能预估（~20-30 tokens/s）和量化质量损失（Q_score ~0.98）属于具体经验数据，缺乏通用性，且未指明具体模型规模（如7B/13B/70B），不同模型下数值差异巨大，存在以偏概全风险。 | 来源[1]仅确认L4为24GB AI推理卡，未提供功耗、具体性能数值或量化质量数据；该节点为search类型，包含具体硬件性能与成本经验事实，逻辑自洽但缺乏直接来源支持具体数值，故降级。

## Search Query

NVIDIA L4 A10 24GB Qwen 27B FP8 inference performance power consumption

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/652803924&rut=cf3c0067212f69b34dc411c46179226a8547ce0fa4789e48c238a0888af00b5a', 'type': 'ddg', 'title': 'Nvidia L4 24gb 评测 多功能 Ai 推理卡 - 知乎'}
