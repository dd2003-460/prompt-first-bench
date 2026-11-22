# N131: 精度容忍任务（对话/摘要）下的硬件约束：若采用 INT8 精度 (27GB) + 32K KV Cache (1.6GB) + 框架开销 (5GB) ≈ 33.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

精度容忍任务（对话/摘要）下的硬件约束：若采用 INT8 精度 (27GB) + 32K KV Cache (1.6GB) + 框架开销 (5GB) ≈ 33.6GB，单卡 RTX 4090 (24GB) 仍显存不足，需双卡 RTX 4090 (48GB) 或单卡 L40S (48GB, $8000)；若采用 W4 精度 (13.5GB) + 32K KV Cache (1.6GB) + 框架开销 (5GB) ≈ 20.1GB，单卡 RTX 4090 (24GB) 可行且性价比最高。

## Corrected Claim

精度容忍任务（对话/摘要）下的硬件约束：若采用 INT8 精度 (27GB) + 32K KV Cache (1.6GB) + 框架开销 (5GB) ≈ 33.6GB，单卡 RTX 4090 (24GB) 仍显存不足，需双卡 RTX 4090 (48GB) 或单卡 L40S (48GB, $8000)；若采用 W4 精度 (13.5GB) + 32K KV Cache (1.6GB) + 框架开销 (5GB) ≈ 20.1GB，单卡 RTX 4090 (24GB) 可行且性价比最高。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8模型(27GB)+KV(1.6GB)+开销(5GB)=33.6GB > 24GB (RTX 4090)，故需双卡或48GB卡；W4模型(13.5GB)+KV(1.6GB)+开销(5GB)=20.1GB < 24GB，故单卡4090可行。数值量级与硬件规格符合常识。
