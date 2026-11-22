# N165: 任务类型特异性下的最优硬件切换阈值：定义 Batch_Size_Threshold 和 Seq_Len_Threshold，当 batch_size > 8 或

- **status**: pending
- **level**: L3
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

任务类型特异性下的最优硬件切换阈值：定义 Batch_Size_Threshold 和 Seq_Len_Threshold，当 batch_size > 8 或 seq_len > 16K 时，显存需求超过 24GB，RTX 4090 需量化 (INT8/W4) 或多卡。若强制 BF16，RTX 4090 不可行，A100/H100 成为唯一选择。若允许 INT8，RTX 4090 可行 (27GB 权重 + 2.15GB KV < 24GB? No, 29.15GB > 24GB，仍需 Offload 或 W4)。W4 下 RTX 4090 可行 (14.57GB < 24GB)，但质量损失 5-10%。需根据用户对质量的容忍度确定是否切换至数据中心卡。

## Corrected Claim

对于约5.4B参数的模型，在Batch_Size > 8或Seq_Len > 16K时，BF16显存需求超过24GB，RTX 4090不可行；INT8下显存需求约29.15GB，仍超过24GB，需Offload或W4量化；W4下显存需求约14.57GB，RTX 4090可行但存在5-10%质量损失。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2存在严重内容重叠和逻辑矛盾。子节点1已明确指出BF16不可行且INT8权重(27.3GB)>24GB不可行，必须量化至W4；子节点2重复了INT8不可行的结论并再次推导W4的可行性，两者在'INT8不可行'这一结论上重复，且子节点2关于W4的计算（13.5GB权重）与子节点1中提到的W4(13.5GB)一致，导致信息冗余。此外，子节点1中提到的KV Cache每token 0.52MB（BF16）与子节点2中W4下的0.26MB（假设量化后KV也减半或类似逻辑）未明确说明KV是否随权重量化而改变，存在隐含假设不一致的风险，但主要问题是1和2的高度冗余。）
