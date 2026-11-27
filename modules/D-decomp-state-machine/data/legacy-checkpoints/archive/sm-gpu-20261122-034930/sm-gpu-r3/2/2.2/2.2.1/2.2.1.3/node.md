# N222: 显存需求最终判定：若采用INT8 KV Cache，总显存36.35GB，单卡RTX 4090 (24GB) 仍不足，需2x 4090或A100 40GB。若采

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

显存需求最终判定：若采用INT8 KV Cache，总显存36.35GB，单卡RTX 4090 (24GB) 仍不足，需2x 4090或A100 40GB。若采用FP16 KV Cache，总显存41.7GB，单卡A100 40GB亦不足（40 < 41.7），需A100 80GB或2x 4090。因此，INT8 KV Cache策略是使2x 4090或A100 40GB成为可行选项的关键技术前提。

## Corrected Claim

显存需求最终判定：若采用INT8 KV Cache，总显存36.35GB，单卡RTX 4090 (24GB) 仍不足，需2x 4090或A100 40GB。若采用FP16 KV Cache，总显存41.7GB，单卡A100 40GB亦不足（40 < 41.7），需A100 80GB或2x 4090。因此，INT8 KV Cache策略是使2x 4090或A100 40GB成为可行选项的关键技术前提。

## Evidence

先验知识/题面给定，逻辑校验通过：数值比较（36.35>24, 41.7>40）及硬件配置逻辑自洽，无内部矛盾。
