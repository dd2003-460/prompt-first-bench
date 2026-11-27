# N11: 混合架构（如 CPU 内存卸载 + GPU 加速）的可行性取决于 PCIe 带宽瓶颈，需计算 KV Cache 或权重卸载后的延迟增加量是否可接受 [待核验]

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

混合架构（如 CPU 内存卸载 + GPU 加速）的可行性取决于 PCIe 带宽瓶颈，需计算 KV Cache 或权重卸载后的延迟增加量是否可接受 [待核验]

## Corrected Claim

混合架构（如 CPU 内存卸载 + GPU 加速）的可行性取决于 PCIe 带宽瓶颈，需计算 KV Cache 或权重卸载后的延迟增加量是否可接受 [待核验]

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对权重静态卸载、KV Cache动态访问、以及层间激活传输三种不同场景进行延迟分析，维度互斥且无重复。它们共同覆盖了混合架构中主要的PCIe带宽瓶颈场景，逻辑自洽且数据支撑了父节点的可行性判断。）

## Search Query

quantitative latency overhead of KV cache offloading PCIe vs NVLink

## Retrieval Sources

- {'url': 'https://github.com/ollama/ollama/issues/18186&rut=5f6fb2911319a5f61f307c2a58a2f2416389a600bd17d53c8733456e9309db02', 'type': 'ddg', 'title': 'QWEN3.8 27b plus MTP settings cause offloading to CPU'}
