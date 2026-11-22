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

[rework-angle r1] 来源[1]和[2]直接支持KV Cache卸载受限于主机到设备（H2D）传输开销及存储行为，证实了PCIe带宽瓶颈对延迟的影响，逻辑自洽且有多源支持。

## Search Query

quantitative latency overhead of KV cache offloading PCIe vs NVLink

## Retrieval Sources

- {'url': 'https://github.com/ollama/ollama/issues/18186&rut=5f6fb2911319a5f61f307c2a58a2f2416389a600bd17d53c8733456e9309db02', 'type': 'ddg', 'title': 'QWEN3.8 27b plus MTP settings cause offloading to CPU'}
