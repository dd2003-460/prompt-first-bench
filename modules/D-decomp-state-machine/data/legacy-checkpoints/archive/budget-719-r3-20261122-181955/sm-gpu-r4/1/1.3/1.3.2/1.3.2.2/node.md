# N179: RX 7900 XT 的显存带宽 800 GB/s 在 Decode 阶段的实际利用率：受限于 PCIe 4.0 x16 总线带宽（64 GB/s）和内存控制器

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N53

## Claim

RX 7900 XT 的显存带宽 800 GB/s 在 Decode 阶段的实际利用率：受限于 PCIe 4.0 x16 总线带宽（64 GB/s）和内存控制器效率，实际有效带宽通常在 85-90% 范围内；需结合 Qwen3-27B 的 KV Cache 大小（32.77 GB BF16）计算理论 Decode 吞吐量上限。

## Corrected Claim

RX 7900 XT 的显存带宽 800 GB/s 在 Decode 阶段的实际利用率受限于硬件架构和内存控制器效率，实际有效带宽通常低于理论峰值；需结合 Qwen3-27B 的 KV Cache 大小（32.77 GB BF16）计算理论 Decode 吞吐量上限。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性差：子节点2完全重复了父节点中关于“实际利用率/有效带宽”的结论（0.85-0.90系数），而子节点1直接使用了该结论进行计算，两者在信息内容上高度重叠。2. 完备性不足：父节点明确提到“PCIe 4.0 x16 总线带宽”作为限制因素之一，但两个子节点均未涉及PCIe带宽对Decode阶段（特别是模型权重首次加载或长上下文KV缓存传输）的影响，仅讨论了显存带宽。3. 冗余：子节点2本质上只是父节点中“有效带宽”这一参数的展开解释，并非独立的正交维度。）

## Search Query

AMD RX 7900 XT memory bandwidth efficiency LLM inference
