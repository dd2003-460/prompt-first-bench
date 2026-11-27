# N27: 候选硬件全集筛选基准：消费级高端（RTX 4090 24GB, RTX 3090 24GB, RTX 4080 16GB），数据中心入门（A100 40GB/8

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件全集筛选基准：消费级高端（RTX 4090 24GB, RTX 3090 24GB, RTX 4080 16GB），数据中心入门（A100 40GB/80GB, H100 80GB, L40S 48GB），以及高显存工作站卡（A6000 48GB, A6000 Ada 48GB）。筛选逻辑基于显存容量下限（N9）与互联能力（N24），排除显存不足36GB（W4方案最低需求）或无多卡互联支持且单卡显存不足50GB（INT8方案）的型号。

## Corrected Claim

候选硬件全集筛选基准：消费级高端（RTX 4090 24GB, RTX 3090 24GB, RTX 4080 16GB），数据中心入门（A100 40GB/80GB, H100 80GB, L40S 48GB），以及高显存工作站卡（A6000 48GB, A6000 Ada 48GB）。筛选逻辑基于显存容量下限（N9）与互联能力（N24），排除显存不足36GB（W4方案最低需求）或无多卡互联支持且单卡显存不足50GB（INT8方案）的型号。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 765)
