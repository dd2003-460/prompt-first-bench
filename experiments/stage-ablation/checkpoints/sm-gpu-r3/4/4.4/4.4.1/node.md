# N105: RTX 5090 显存带宽为 1792 GB/s (GDDR7, 32GB, 512-bit bus, 28 Gbps)。其 BF16 权重占用仍为 54GB 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

RTX 5090 显存带宽为 1792 GB/s (GDDR7, 32GB, 512-bit bus, 28 Gbps)。其 BF16 权重占用仍为 54GB (超出 32GB 显存)，因此单卡无法运行 BF16 全量模型，必须使用量化 (如 FP8 或 INT4) 或启用 CPU offload。

## Corrected Claim

RTX 5090 显存带宽为 1792 GB/s (GDDR7, 32GB, 512-bit bus, 28 Gbps)。其 BF16 权重占用仍为 54GB (超出 32GB 显存)，因此单卡无法运行 BF16 全量模型，必须使用量化 (如 FP8 或 INT4) 或启用 CPU offload。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1负责硬件规格验证（修正位宽），节点2分析BF16不可行性（问题场景），节点3分析FP8可行性（解决方案场景）。三者覆盖了父节点中关于显存带宽、BF16限制、量化/Offload必要性以及具体量化后性能估算的所有关键方面，且无内容重叠或矛盾。）

## Search Query

RTX 5090 GDDR7 bandwidth 1792 GB/s 32GB VRAM Qwen3-27B fit
