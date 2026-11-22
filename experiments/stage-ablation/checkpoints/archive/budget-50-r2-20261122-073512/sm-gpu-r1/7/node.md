# N34: NVIDIA RTX 4090 显存带宽为 1008 GB/s (GDDR6X)，而 RTX 3090 为 936 GB/s (GDDR6X)，AMD RX 7

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA RTX 4090 显存带宽为 1008 GB/s (GDDR6X)，而 RTX 3090 为 936 GB/s (GDDR6X)，AMD RX 7900 XTX 为 960 GB/s (GDDR6)；基于带宽瓶颈模型，RTX 4090 在 BF16 下的理论生成速度上限约为 1008/56 ≈ 18 tokens/s，高于 RTX 3090 的 936/56 ≈ 16.7 tokens/s。

## Corrected Claim

NVIDIA RTX 4090 显存带宽为 1008 GB/s (GDDR6X)；基于带宽瓶颈模型，若模型占用 56GB 显存，RTX 4090 在 BF16 下的理论生成速度上限约为 18 tokens/s。

## Evidence

[质询]RTX 3090 和 AMD RX 7900 XTX 的显存带宽数值及具体对比未在提供的参考来源中直接证实，且 1008/56 的带宽瓶颈模型计算依赖于特定的模型参数量假设（56GB），属于经验性估算而非绝对物理事实。 | 来源 [1] 和 [2] 直接支持 RTX 4090 带宽为 1008 GB/s 及 GDDR6X 规格；但 RTX 3090 (936 GB/s) 和 RX 7900 XTX (960 GB/s) 的具体数值及基于 56GB 模型的 tokens/s 推算缺乏来源直接支持，属于经验事实且仅部分验证。

## Retrieval Sources

- {'url': 'https://gigagpu.com/rtx-4090-24gb-gddr6x-vram-bandwidth/&rut=e402d0c2a1903844cb346767a63d94aa3388810bf519e7d9844546ffc2bd5569', 'type': 'ddg', 'title': 'RTX 4090 24GB GDDR6X 1008 GB/s Bandwidth Explained'}
- {'url': 'https://www.pconline.com.cn/ask/317020.html&rut=2fb364cddcd769048ce468a90c49245b5d3b121b9d9bd0c3b27a929414355f60', 'type': 'ddg', 'title': '4090显卡参数带宽多少GB/s？ - 太平洋科技 - PC Online'}
- {'url': 'https://blog.csdn.net/weixin_42405592/article/details/152220873&rut=1c3878a3cd9944f584ba078655c3200d0321b55135d0a047787f4dbc48beb2ae', 'type': 'ddg', 'title': 'Rxt4090显卡的显存带宽有多强？ - Csdn博客'}
