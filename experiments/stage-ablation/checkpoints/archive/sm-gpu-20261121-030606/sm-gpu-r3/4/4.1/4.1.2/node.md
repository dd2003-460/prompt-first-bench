# N122: 修正N19与N7/N13的矛盾：FP8精度权重显存占用 W_FP8 = 27.0B × 1 byte = 27GB（非N19所述的27GB与N7/N13所述的1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

修正N19与N7/N13的矛盾：FP8精度权重显存占用 W_FP8 = 27.0B × 1 byte = 27GB（非N19所述的27GB与N7/N13所述的13.5GB冲突，需澄清：若N7/N13声称13.5GB，则其隐含假设是参数量减半或使用了4-bit量化，但标准FP8为1字节/参数。此处判定N19的27GB在纯FP8下更可信，N7/N13的13.5GB可能混淆了NVFP4或W4的数据，或错误地使用了13.5B参数量。鉴于N19明确区分了FP8(27GB)和NVFP4(13.5GB)，判定N19正确，N7/N13中关于FP8=13.5GB的表述为错误引用了NVFP4/W4的数值，需在后续节点修正工作点计算。

## Corrected Claim

修正N19与N7/N13的矛盾：FP8精度权重显存占用 W_FP8 = 27.0B × 1 byte = 27GB（非N19所述的27GB与N7/N13所述的13.5GB冲突，需澄清：若N7/N13声称13.5GB，则其隐含假设是参数量减半或使用了4-bit量化，但标准FP8为1字节/参数。此处判定N19的27GB在纯FP8下更可信，N7/N13的13.5GB可能混淆了NVFP4或W4的数据，或错误地使用了13.5B参数量。鉴于N19明确区分了FP8(27GB)和NVFP4(13.5GB)，判定N19正确，N7/N13中关于FP8=13.5GB的表述为错误引用了NVFP4/W4的数值，需在后续节点修正工作点计算。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8标准精度为1字节/参数，27.0B参数对应27GB显存，逻辑自洽且符合硬件常识，来源未直接覆盖但无矛盾。

## Search Query

FP8 weight size calculation 1 byte per parameter
