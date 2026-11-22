# N78: 工作点A（FP8量化/24GB显存）：1×RTX 4090运行Qwen3-27B FP8，权重27GB+KV Cache 4.3GB(GQA)+Buffer 2

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

工作点A（FP8量化/24GB显存）：1×RTX 4090运行Qwen3-27B FP8，权重27GB+KV Cache 4.3GB(GQA)+Buffer 2GB≈33.3GB，显存不足，需INT8或GQA+FP8混合；若INT8(权重27GB+KV 4.3GB)，显存31.3GB仍超24GB，故FP8/INT8单卡4090不可行，必须INT4。

## Corrected Claim

工作点A（FP8量化/24GB显存）：1×RTX 4090运行Qwen3-27B，FP8/INT8量化下权重均约为27GB，加上KV Cache和Buffer后总显存需求远超24GB，因此8-bit量化（FP8/INT8）在单卡24GB上不可行，必须采用INT4等更低比特量化方案。

## Evidence

[质询]数值量级与口径混淆：Qwen3-27B 的参数量约为 270 亿，FP8 权重体积约为 27GB，INT8 权重体积也约为 27GB（1字节/参数），而非陈述中隐含的 INT8 比 FP8 更省显存的逻辑（实际上 FP8 和 INT8 在权重存储上体积相同，均为 1 字节/参数，除非 FP8 指代的是某种特殊的 4-bit 混合或陈述者混淆了 FP8 与 FP16/INT4 的概念）。此外，27GB 权重本身已接近 24GB 显存上限，加上 KV Cache 和 Buffer，任何 8-bit 量化（FP8/INT8）在单卡 24GB 上确实不可行，但陈述中关于 INT8 权重 27GB 的描述虽数值正确，却未指出 FP8 与 INT8 在权重体积上无差异这一关键逻辑漏洞，导致“需 INT8 或 GQA+FP8 混合”的建议在纯权重体积上无效（因为 INT8 并不比 FP8 省空间，除非是动态量化或特定框架优化，但通常 8-bit 量化体积一致）。更核心的攻击点是：如果 FP8 权重是 27GB，那么 INT8 权重也是 27GB，陈述中“若 INT8(权重27GB...)”的表述虽数值对，但暗示 INT8 是一种替代方案，而实际上对于 27B 模型，8-bit 量化（无论 FP8 还是 INT8）在 24GB 卡上通常都因权重+KV 溢出而不可行，必须 4-bit。陈述的逻辑结论“必须 INT4”是正确的，但中间推导对 INT8 的讨论略显冗余且未澄清 FP8/INT8 体积等价性，存在轻微逻辑不严谨。 | 来源 [1] 标题提及 RTX 4090D (24GB) 部署 Qwen3.8-27B（注：Qwen3 目前无 3.8 版本，可能为笔误或指 Qwen2.5/3 系列，但 27B 规格匹配），摘要提到“实测数据”和“最终方案”，间接支持 24GB 显存部署 27B 模型需要特定量化策略（如 4-bit）的事实，但未直接提供 FP8/INT8 的具体显存占用数值对比，故为间接支持。

## Search Query

Qwen3 27B FP8 INT8 memory usage 24GB GPU

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=3500097cb3ed29c7b1bd2fc0071f208d076cac111c37de4fb03e30bdc07669c3', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
