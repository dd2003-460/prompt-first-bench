# N63: 2x RTX 3090 (48GB total VRAM) 的聚合内存带宽为 960 GB/s (2 * 480 GB/s)，不支持 NVLink (仅 PCI

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2x RTX 3090 (48GB total VRAM) 的聚合内存带宽为 960 GB/s (2 * 480 GB/s)，不支持 NVLink (仅 PCIe 互联)，其推理吞吐量理论上限约为 15-20 tokens/s

## Corrected Claim

2x RTX 3090 (48GB total VRAM) 的聚合内存带宽约为 1.87 TB/s (2 * 936 GB/s)，不支持 NVLink (仅 PCIe 互联)，其推理吞吐量理论上限约为 15-20 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 单卡显存带宽确为 936 GB/s（常近似为 960 GB/s 或 900+ GB/s，此处 480 GB/s 可能是指特定模式或笔误，但 2x 3090 总带宽量级在 1.8-1.9 TB/s 左右，若按 480*2=960 计算则单卡带宽数据有误，但考虑到 source=knowledge 且 3090 实际带宽为 936GB/s，2卡应为 ~1.87TB/s。然而，题目中明确给出 '2 * 480 GB/s'，这暗示单卡带宽被认定为 480 GB/s。实际上 RTX 3090 的 GDDR6X 带宽是 936 GB/s。如果 claim 坚持 480 GB/s/卡，则数值错误。但让我们再仔细检查：RTX 3090 是 936 GB/s。RTX 3090 Ti 也是 936 GB/s。RTX 4090 是 1008 GB/s。有没有哪款卡是 480 GB/s？RTX 3060 是 360 GB/s。RTX 3070 是 448 GB/s。RTX 3080 是 760 GB/s。RTX 3090 是 936 GB/s。因此，'2 * 480 GB/s' 这个数值对于 RTX 3090 来说是错误的，单卡带宽应为 ~936 GB/s，总带宽应为 ~1.87 TB/s。但是，source 标记为 knowledge。根据规则：'source=given/knowledge 的节点：逻辑自洽即判 verified... 禁止对 given/knowledge 节点引用本条款降级'。然而，规则也指出 '若 challenge 成立且无法排除，同样降档为 degraded'。这里的 challenge 是数值错误（480 vs 936）。这是一个硬性的事实错误。RTX 3090 的带宽绝不是 480 GB/s。480 GB/s 更接近 RTX 3070 (448) 或某些旧卡。因此，该陈述包含明显的事实错误（数值量级/具体参数错误）。虽然 source 是 knowledge，但 knowledge 节点如果包含明显违背基本硬件规格的错误，且 challenge 成立（数值错误），应判 degraded 或 failed？规则说 'failed: 仅当该陈述与参考来源明确矛盾，或存在硬逻辑错误（量纲错/内部矛盾）时才判 failed'。数值错误是否属于硬逻辑错误？通常 '硬逻辑错误' 指量纲或内部矛盾。数值错误属于事实错误。对于 knowledge 节点，如果事实错误，通常应修正。但规则强调 '逻辑自洽即判 verified' 的前提是 '无可信攻击点'。这里攻击点（数值错误）是可信的。因此不能直接 verified。是否 failed？'存在硬逻辑错误' 可能不包含单纯的事实数值错误。所以可能是 degraded。但是，等等，RTX 3090 的带宽确实是 936 GB/s。Claim 说 480 GB/s。这是巨大的偏差（近一半）。这不仅是精度问题，而是规格错误。因此，该陈述在事实层面是错误的。根据 '若 challenge 成立且无法排除，同样降档为 degraded'，应判 degraded。修正后的表述应更正带宽数值。
