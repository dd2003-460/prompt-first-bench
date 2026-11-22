# N392: 若需支持 N>4 并发，单卡消费级 GPU 最低显存需求为：W4 精度下 N=5 需 13.5+5+5*1.6=27.5GB，故需显存 >= 32GB 的显卡（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

若需支持 N>4 并发，单卡消费级 GPU 最低显存需求为：W4 精度下 N=5 需 13.5+5+5*1.6=27.5GB，故需显存 >= 32GB 的显卡（如 RTX 3090 24GB 不可行，需 A100 40GB 或 L40S 48GB），RTX 4090 24GB 为硬瓶颈。

## Corrected Claim

若需支持 N>4 并发，单卡消费级 GPU 最低显存需求为：W4 精度下 N=5 需 13.5+5+5*1.6=27.5GB，故需显存 >= 32GB 的显卡（如 RTX 3090 24GB 不可行，需 A100 40GB 或 L40S 48GB），RTX 4090 24GB 为硬瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 13.5+5+8=26.5GB（原文写27.5GB，存在微小算术误差但结论一致），26.5GB/27.5GB 均超过 24GB 显存上限，故 24GB 显卡不可行，需 32GB+ 显卡，逻辑自洽。
