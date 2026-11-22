# N31: 替代方案切换阈值：当上下文长度从 32K 增加到 128K 时，KV Cache 显存增加 4 倍，导致 24GB 消费级显卡即使使用 INT4 也可能溢出（1

- **status**: pending
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

父节点级核验未通过：有冗余（子节点在硬件架构上正交且覆盖了24GB不可行、48GB可行、80GB高配三个关键层级，完备性良好。但存在明显的结构性冗余：子节点1中关于'2x 4090仍不足'的论述与子节点2中'2x 4090可行'的论述存在逻辑冲突或数据不一致（子节点1称需3x或2x5090，子节点2称2x4090可行），且子节点1后半部分已提前覆盖了子节点2的内容，导致信息重叠。此外，所有子节点的核心逻辑均为'权重+KV Cache vs 显存'的计算，属于同一计算模型在不同硬件参数下的实例化，可压缩。）

## Search Query

long context inference memory requirement 128k tokens KV cache overflow consumer GPU
