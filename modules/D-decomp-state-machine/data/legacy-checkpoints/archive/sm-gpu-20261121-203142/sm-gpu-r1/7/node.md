# N30: 消费级GPU显存瓶颈：RTX 4090/3090 Ti (24GB) 和 RTX 5090 (32GB) 在BF16下无法加载27B模型权重(54GB)，必须依

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

消费级GPU显存瓶颈：RTX 4090/3090 Ti (24GB) 和 RTX 5090 (32GB) 在BF16下无法加载27B模型权重(54GB)，必须依赖量化(INT8/FP8)或CPU Offload；RTX 5090 32GB在INT8下(27GB权重+KV Cache)勉强可行但无余量，在FP8下(27GB权重)可行。

## Corrected Claim

消费级GPU显存瓶颈：RTX 4090/3090 Ti (24GB) 在BF16下无法加载27B模型权重(54GB)，必须依赖量化(INT8/FP8)或CPU Offload；RTX 5090 (32GB) 在INT8下(27GB权重+KV Cache)显存占用接近上限，可行性取决于具体KV Cache大小及优化策略，在FP8下(约13.5GB权重)则较为宽裕。

## Evidence

[质询]RTX 5090 的显存规格（32GB）及具体量化后的显存占用数值属于经验事实，且参考来源仅覆盖 RTX 3090，未提供 RTX 5090 或 27B 模型在 BF16/INT8/FP8 下的具体显存占用数据，无法通过现有来源直接验证 5090 的可行性结论。 | 逻辑推导成立：27B 模型 BF16 权重约 54GB，超过 24GB/32GB 显存，必须量化或 Offload；INT8 权重约 27GB，加上 KV Cache 后在 32GB 显存中确实紧张但理论可行。来源 [1] 仅证实 3090 为 24GB 且用于本地推理，未覆盖 5090 及具体量化数值，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2076733988736189931&rut=7d5e45cca7eb58e75daf958da31495bceb1dc0b77c937a535302c682638167c3', 'type': 'ddg', 'title': 'Rtx 3090 的 24gb 显存到底能做什么？为什么3090过了这么多年，做ai仍然有人用？ - 知乎'}
