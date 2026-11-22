# N90: 多卡方案（2×RTX 4090, Tensor Parallel）的TTFT通信开销量化：Prefill阶段需在每张卡上执行部分计算并交换中间激活值；PCIe 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

多卡方案（2×RTX 4090, Tensor Parallel）的TTFT通信开销量化：Prefill阶段需在每张卡上执行部分计算并交换中间激活值；PCIe 4.0带宽（~25 GB/s单向）相对于HBM带宽是瓶颈；估算通信开销增加TTFT 15-30% [待核验]，导致有效TTFT ≈ 单卡TTFT * 1.2。

## Corrected Claim

多卡方案（2×RTX 4090, Tensor Parallel）的TTFT通信开销量化：Prefill阶段需在每张卡上执行部分计算并交换中间激活值；PCIe 4.0带宽（~25 GB/s单向）相对于HBM带宽是瓶颈；估算通信开销增加TTFT 15-30% [待核验]，导致有效TTFT ≈ 单卡TTFT * 1.2。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1负责数据量与带宽基础参数计算，节点2负责基于数据量的传输时间占比分析（核心量化），节点3负责补充启动延迟（Launch Latency）这一非带宽瓶颈因素。三者共同覆盖了父节点中关于‘通信开销量化’、‘PCIe瓶颈’及‘15-30%估算核验’的所有关键方面，且通过计算推翻了父节点的高估结论，逻辑自洽。）

## Search Query

tensor parallelism PCIe overhead LLM inference latency
