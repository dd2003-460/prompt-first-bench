# N160: 替代方案：RTX 3090 (24GB) 与 4090 在单卡 INT8 场景下的对比：3090 显存同为 24GB，但带宽为 936 GB/s（低于 4090

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

替代方案：RTX 3090 (24GB) 与 4090 在单卡 INT8 场景下的对比：3090 显存同为 24GB，但带宽为 936 GB/s（低于 4090 的 1008 GB/s），Decode 速度慢 7%。两者均无法在 32K 上下文下运行 INT8 27B 模型（显存不足），故均被排除。唯一可行的单卡消费级方案是 RTX 6000 Ada (48GB) 或 RTX 5090 (32GB, 若价格合适且支持 32K 上下文 INT8 部署)。

## Corrected Claim

替代方案：RTX 3090 (24GB) 与 4090 在单卡 INT8 场景下的对比：3090 显存同为 24GB，但带宽为 936 GB/s（低于 4090 的 1008 GB/s），Decode 速度慢 7%。两者均无法在 32K 上下文下运行 INT8 27B 模型（显存不足），故均被排除。唯一可行的单卡消费级方案是 RTX 6000 Ada (48GB) 或 RTX 5090 (32GB, 若价格合适且支持 32K 上下文 INT8 部署)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090/4090显存均为24GB，带宽数值（936/1008 GB/s）符合硬件规格，27B INT8模型在32K上下文下显存需求远超24GB，逻辑自洽。

## Search Query

RTX 3090 vs 4090 vs 5090 single card 27B INT8 32K context feasibility
