# N136: RTX 4060 Ti 16GB 显存不足 (需求 20GB vs 容量 16GB) 导致必须 Offload 约 4GB 数据；若 Offload 的是 KV

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

RTX 4060 Ti 16GB 显存不足 (需求 20GB vs 容量 16GB) 导致必须 Offload 约 4GB 数据；若 Offload 的是 KV Cache 的一部分，由于 KV Cache 在自回归生成中是顺序读取，Offload 部分的带宽瓶颈 (PCIe 32GB/s) 会导致每生成一个 token 增加 ~125us 延迟 (4GB/32GB/s)，对总吞吐影响显著

## Corrected Claim

RTX 4060 Ti 16GB 显存不足导致必须 Offload 约 4GB 数据。若 Offload 的是 KV Cache，由于自回归生成中 KV Cache 需累积读取，PCIe 带宽瓶颈（32GB/s）会导致每生成一个 token 的延迟随序列长度增加而显著增加，而非固定增加 ~125us。

## Evidence

[质询]陈述中关于延迟增加的物理模型存在严重逻辑错误：KV Cache 在自回归生成中是累积读取（每生成一个 token 需读取当前所有历史 KV），而非一次性顺序读取 4GB 数据。若 Offload 4GB 数据，每生成一个 token 的额外延迟并非固定的 4GB/32GB/s，而是随着序列长度增加而线性增加（因为需要反复从 PCIe 读取已 Offload 的历史 KV 部分）。此外，4GB/32GB/s = 125ms (而非 125us)，量级计算错误（125ms 是 125,000us）。 | 逻辑校验失败：1. 单位换算错误，4GB/32GB/s = 0.125s = 125ms，而非 125us；2. 物理模型错误，KV Cache 的读取量随生成步数累积，Offload 导致的延迟是动态累积的，而非每 token 固定增加 125us（或 125ms）。

## Search Query

RTX 4060 Ti 16GB offload KV cache latency impact PCIe bandwidth
