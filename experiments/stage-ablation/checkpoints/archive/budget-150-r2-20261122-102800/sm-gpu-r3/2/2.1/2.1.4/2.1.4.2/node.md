# N218: 单卡 RTX 4090 (24 GB) 部署该 W4 混合精度模型时，扣除 KV Cache (4.3 GB) 和激活值 (2-3 GB)，剩余可用显存约 17

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

单卡 RTX 4090 (24 GB) 部署该 W4 混合精度模型时，扣除 KV Cache (4.3 GB) 和激活值 (2-3 GB)，剩余可用显存约 17.7 GB，足以容纳 14.35 GB 权重，且无需 Offload，显存瓶颈判定为‘充裕’，支持单卡高性能推理。

## Corrected Claim

单卡 RTX 4090 (24 GB) 部署该 W4 混合精度模型时，扣除 KV Cache (4.3 GB) 和激活值 (2-3 GB)，剩余可用显存约 17.7 GB，足以容纳 14.35 GB 权重，且无需 Offload，显存瓶颈判定为‘充裕’，支持单卡高性能推理。

## Evidence

先验知识/题面给定，逻辑校验通过：24GB总显存扣除4.3GB KV Cache和2-3GB激活值后，剩余约17.7GB（取激活值上限3GB时剩余16.7GB，下限2GB时剩余17.7GB，陈述取17.7GB对应激活值2GB的情况，或为近似值），大于14.35GB权重，显存充足，无需Offload，逻辑自洽。
