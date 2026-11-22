# N78: 工作点A（FP8量化/24GB显存）：1×RTX 4090运行Qwen3-27B FP8，权重27GB+KV Cache 4.3GB(GQA)+Buffer 2

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别验证了FP8、INT8和INT4三种量化方案在24GB显存下的可行性，彼此正交且无重复；父节点的核心结论（FP8/INT8不可行，INT4可行）被完整覆盖；虽然三个子节点结构相似，但针对不同的量化精度（参数取值不同），属于必要的枚举验证，不构成冗余。）

## Search Query

Qwen3 27B FP8 INT8 memory usage 24GB GPU

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=3500097cb3ed29c7b1bd2fc0071f208d076cac111c37de4fb03e30bdc07669c3', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
