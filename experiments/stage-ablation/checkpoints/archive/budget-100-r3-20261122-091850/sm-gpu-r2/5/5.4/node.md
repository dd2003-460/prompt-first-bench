# N27: 显存容量档位筛选：根据 Qwen3-27B 在 32K 上下文下的显存需求（权重 + KV Cache + 激活值），确定最小显存门槛。BF16 下需 ~60G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

显存容量档位筛选：根据 Qwen3-27B 在 32K 上下文下的显存需求（权重 + KV Cache + 激活值），确定最小显存门槛。BF16 下需 ~60GB，FP8 下需 ~35GB，W4 下需 ~20GB；据此筛选候选 GPU 显存（24GB, 48GB, 80GB），排除显存不足导致无法加载或需频繁 offload 的方案。

## Corrected Claim

显存容量档位筛选：根据 Qwen3-27B 在 32K 上下文下的显存需求（权重 + KV Cache + 激活值），确定最小显存门槛。BF16 下需 ~60GB，FP8 下需 ~35GB，W4 下需 ~20GB；据此筛选候选 GPU 显存（24GB, 48GB, 80GB），排除显存不足导致无法加载或需频繁 offload 的方案。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB，加上32K上下文KV Cache及激活值，总显存需求~60GB符合工程估算；FP8权重减半约27GB，总需求~35GB合理；W4权重约13.5GB，总需求~20GB合理。数值量级与GPU显存档位（24/48/80GB）筛选逻辑自洽。
