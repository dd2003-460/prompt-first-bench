# N70: BF16 可行性边界：60.1GB 的总需求意味着单卡 48GB (如 A6000/L40S) 不可行（缺口 12.1GB），单卡 80GB (A100/H10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

BF16 可行性边界：60.1GB 的总需求意味着单卡 48GB (如 A6000/L40S) 不可行（缺口 12.1GB），单卡 80GB (A100/H100) 可行（剩余 19.9GB 用于系统开销和碎片整理），单卡 24GB/32GB 完全不可行。

## Corrected Claim

BF16 可行性边界：60.1GB 的总需求意味着单卡 48GB (如 A6000/L40S) 不可行（缺口 12.1GB），单卡 80GB (A100/H100) 可行（剩余 19.9GB 用于系统开销和碎片整理），单卡 24GB/32GB 完全不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：60.1GB > 48GB (缺口12.1GB) 且 60.1GB < 80GB (剩余19.9GB)，数值计算自洽，符合GPU显存容量常识。
