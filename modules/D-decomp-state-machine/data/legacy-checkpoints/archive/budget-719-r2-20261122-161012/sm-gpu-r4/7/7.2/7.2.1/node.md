# N268: 在 BF16 精度下，RTX 4090 双卡 (TP=2) 方案因总显存 48GB < 模型需求 55GB，该工作点显存溢出，吞吐量理论值为 0 tokens/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

在 BF16 精度下，RTX 4090 双卡 (TP=2) 方案因总显存 48GB < 模型需求 55GB，该工作点显存溢出，吞吐量理论值为 0 tokens/s，属于不可行工作点，必须通过量化或 Offload 修正。

## Corrected Claim

在 BF16 精度下，RTX 4090 双卡 (TP=2) 方案因总显存 48GB < 模型需求 55GB，该工作点显存溢出，吞吐量理论值为 0 tokens/s，属于不可行工作点，必须通过量化或 Offload 修正。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且互不重叠。节点1负责定量诊断（计算溢出量），节点2和节点3分别针对两种独立的修正路径（量化 vs Offload）进行可行性与性能评估，三者共同完整覆盖了父节点中‘显存溢出’、‘不可行’及‘必须修正’的核心论点，且修正方案A和B在技术实现上属于正交的解决维度，不存在冗余。）
