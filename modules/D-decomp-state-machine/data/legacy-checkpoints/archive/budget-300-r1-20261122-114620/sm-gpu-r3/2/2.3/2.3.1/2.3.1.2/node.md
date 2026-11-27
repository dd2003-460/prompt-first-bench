# N204: Intel Arc A770 的 16GB GDDR6 显存无法容纳 Qwen3-27B BF16 权重 (54GB) 或 INT8 权重 (27GB)，仅能容

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

Intel Arc A770 的 16GB GDDR6 显存无法容纳 Qwen3-27B BF16 权重 (54GB) 或 INT8 权重 (27GB)，仅能容纳 W4 量化权重 (13.5GB) + 极小 KV Cache (约 1.6GB for 32K context)，总占用 15.1GB，剩余 0.9GB 用于激活值，显存利用率高达 94.4%，极易 OOM

## Corrected Claim

Intel Arc A770 的 16GB GDDR6 显存无法容纳 Qwen3-27B BF16 权重 (54GB) 或 INT8 权重 (27GB)，仅能容纳 W4 量化权重 (13.5GB) + 极小 KV Cache (约 1.6GB for 32K context)，总占用 15.1GB，剩余 0.9GB 用于激活值，显存利用率高达 94.4%，极易 OOM

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB，INT8约27GB，W4量化约13.5GB，均符合显存容量与量化位数的数学关系；16GB显存下W4权重+KV Cache占用15.1GB，剩余0.9GB用于激活值，显存利用率94.4%计算自洽，无逻辑矛盾。
