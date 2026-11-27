# N165: 单卡RTX 5090 (FP8)在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1792 GB/s / (13.5GB权重 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N79

## Claim

单卡RTX 5090 (FP8)在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1792 GB/s / (13.5GB权重 + 5.2GB KV Cache + 2.5GB激活) ≈ 89.5 tokens/s，基于RTX 5090 GDDR7 1.79TB/s带宽

## Corrected Claim

单卡RTX 5090 (FP8)在32K上下文、batch_size=1下的理论带宽受限推理吞吐量上限约为89.5 tokens/s，实际吞吐量受内存访问效率和计算延迟影响，通常低于此理论值。

## Evidence

父节点级核验未通过：非正交（子节点2在计算总显存和吞吐量时，直接使用了子节点1修正后的KV Cache数值（1.99GB）以及修正后的权重数值，导致子节点2严重依赖子节点1的结论。两者存在明显的逻辑依赖和数值重叠（均涉及显存构成的修正），并非完全独立正交。此外，父节点中的权重数值（13.5GB）与子节点2中的权重数值（27.0GB）存在巨大差异，暗示父节点本身可能存在严重错误（Qwen3-27B FP8权重通常远大于13.5GB，若为27B模型，FP8权重约27GB），子节点2修正了权重但子节点1未提及，导致分解逻辑链条不完整或父节点前提错误。）

## Search Query

RTX 5090 memory bandwidth GB/s

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2062928081980072755&rut=49bc8e8c89c7838d3642b90c83fe2489e9185702b221db690d43f108a0f13ce5', 'type': 'ddg', 'title': 'Rtx 5090算力到底多少？Fp16/Fp8/Int8算力实测与解读 - 知乎'}
