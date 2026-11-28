# N29: 双卡消费级方案（2x RTX 4090）通过 Tensor Parallelism 实现模型分片，其吞吐量提升受限于 PCIe 带宽（~16GB/s），预计总吞

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

双卡消费级方案（2x RTX 4090）通过 Tensor Parallelism 实现模型分片，其吞吐量提升受限于 PCIe 带宽（~16GB/s），预计总吞吐约为 80 tokens/s [待核验]

## Corrected Claim

双卡消费级方案（2x RTX 4090）通过 Tensor Parallelism 实现模型分片，其吞吐量提升受限于 PCIe 带宽及显存带宽，具体吞吐量需根据量化精度和模型大小实测确定，80 tokens/s 这一具体数值缺乏直接来源支持。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1聚焦硬件互联带宽瓶颈（物理层限制），子节点2聚焦通信开销与计算比例的量化分析（算法/协议层限制），子节点3聚焦最终性能预测及对父节点‘80 tokens/s’假设的修正（结果层）。三者分别从‘为什么慢’（带宽）、‘怎么算慢’（开销占比）、‘最终多快’（吞吐预估）三个不同维度展开，无重复或矛盾。）

## Search Query

dual RTX 4090 tensor parallelism LLM inference bandwidth bottleneck

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=3786150&rut=84f5360546c936b4ca017ec56168bae0c6673341b1f10c798bed063178331a5f', 'type': 'ddg', 'title': '单双卡RTX 4090挑战DeepSeek70B：本地大模型部署的极限探索与实测分析-百度开发者中心'}
