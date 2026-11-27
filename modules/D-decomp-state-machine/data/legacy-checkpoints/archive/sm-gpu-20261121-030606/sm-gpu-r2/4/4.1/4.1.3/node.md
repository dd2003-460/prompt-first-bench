# N123: 修正N19与N12的矛盾：INT8精度权重显存占用 W_INT8 = 27.0B × 1 byte = 27GB（非N12所述的13.5GB。N12声称13.5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

修正N19与N12的矛盾：INT8精度权重显存占用 W_INT8 = 27.0B × 1 byte = 27GB（非N12所述的13.5GB。N12声称13.5GB同样混淆了4-bit量化数据。标准INT8为1字节/参数，故27GB为正确值。这意味着N12中RTX 4090 (24GB) 部署INT8 Qwen3-27B是不可行的，因为仅权重就需27GB > 24GB显存。

## Corrected Claim

修正N19与N12的矛盾：INT8精度权重显存占用 W_INT8 = 27.0B × 1 byte = 27GB（非N12所述的13.5GB。N12声称13.5GB同样混淆了4-bit量化数据。标准INT8为1字节/参数，故27GB为正确值。这意味着N12中RTX 4090 (24GB) 部署INT8 Qwen3-27B是不可行的，因为仅权重就需27GB > 24GB显存。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化标准为1字节/参数，27B参数对应27GB显存占用，逻辑自洽且数值量级合理。

## Search Query

INT8 weight size calculation 1 byte per parameter
