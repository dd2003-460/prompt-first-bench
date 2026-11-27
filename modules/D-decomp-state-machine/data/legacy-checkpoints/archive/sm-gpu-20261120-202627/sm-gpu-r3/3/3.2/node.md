# N17: 数据中心级显卡候选集：A100 (40GB/80GB)、H100 (80GB)、A30 (24GB)、L40S (48GB)，需列出各自显存、带宽、价格 [待核

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

数据中心级显卡候选集：A100 (40GB/80GB)、H100 (80GB)、A30 (24GB)、L40S (48GB)，需列出各自显存、带宽、价格 [待核验：最新市场价格及可用性]

## Corrected Claim

数据中心级显卡候选集：A100 (40GB/80GB, 带宽~1.5-2TB/s)、H100 (80GB, 带宽~3TB/s) 有来源支持；A30 (24GB) 和 L40S (48GB) 规格需进一步核验；最新市场价格及可用性缺乏来源支持，需单独查询。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 不完备：父节点明确要求列出 A30 (24GB) 的显存、带宽及价格，但子节点中完全缺失了 A30 的相关信息。2. 冗余：子节点 1、2、3 结构高度重复（均为：型号+带宽+价格+TDP），且都引入了父节点未要求的上下文（Qwen3-27B 和 TDP 细节），这属于同一类参数（硬件规格）的不同取值，应合并为表格或参数化描述，而非拆分为三个独立的叙述性子节点。）

## Search Query

NVIDIA A100 H100 A30 L40S VRAM bandwidth price 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2092271469376161383&rut=9e08a6fd3239af2080f3fe2a4ae027f9ab58aa70fd7d87e340ee88b5e3717755', 'type': 'ddg', 'title': '2026年A100、H800、H20、4090 GPU榜单：大模型Token推理性能、显存、带宽与架构评测'}
- {'url': 'https://zhuanlan.zhihu.com/p/650583966&rut=0f8d21c66362cee9884cb22940142ff48d579c08d9cf4aecf5e6d14a2c35f809', 'type': 'ddg', 'title': '一文看懂英伟达A100、A800、H100、H800各个版本有什么区别？'}
