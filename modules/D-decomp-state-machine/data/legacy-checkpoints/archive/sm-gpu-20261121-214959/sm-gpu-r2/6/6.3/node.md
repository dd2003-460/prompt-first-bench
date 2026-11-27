# N31: 替代方案切换阈值：当上下文长度从 32K 增加到 128K 时，KV Cache 显存增加 4 倍，导致 24GB 消费级显卡即使使用 INT4 也可能溢出（1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

替代方案切换阈值：当上下文长度从 32K 增加到 128K 时，KV Cache 显存增加 4 倍，导致 24GB 消费级显卡即使使用 INT4 也可能溢出（13.5GB 权重 + 10GB KV Cache > 24GB），此时必须切换至 48GB+ 显存的方案（如 2x 3090/4090 或单卡 A6000），导致性价比排序反转。

## Corrected Claim

替代方案切换阈值：当上下文长度从 32K 增加到 128K 时，KV Cache 显存增加 4 倍，导致 24GB 消费级显卡即使使用 INT4 也可能溢出（13.5GB 权重 + 10GB KV Cache > 24GB），此时必须切换至 48GB+ 显存的方案（如 2x 3090/4090 或单卡 A6000），导致性价比排序反转。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对三种不同的硬件架构路径（24GB单卡不可行性、48GB双卡消费级方案、80GB+专业/数据中心方案）进行了验证，彼此独立且无重叠。父节点中提到的‘性价比排序反转’在子节点2和3的成本与可行性对比中得到了体现，覆盖了阈值切换前后的关键决策点。）

## Search Query

long context inference memory requirement 128k tokens KV cache overflow consumer GPU
