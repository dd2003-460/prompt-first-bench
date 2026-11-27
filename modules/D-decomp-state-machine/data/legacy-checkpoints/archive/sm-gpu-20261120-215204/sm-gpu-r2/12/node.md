# N153: Apple M4 Ultra (Mac Studio) 的统一内存带宽峰值为 819 GB/s，最大可选内存容量为 512 GB（当前主流配置为 256 GB 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Apple M4 Ultra (Mac Studio) 的统一内存带宽峰值为 819 GB/s，最大可选内存容量为 512 GB（当前主流配置为 256 GB 或 192 GB），TDP 约为 200-250W（整机功耗），无独立显存概念，内存共享架构导致 CPU 和 GPU 竞争带宽。

## Corrected Claim

Apple M4 Ultra (Mac Studio) 的统一内存带宽峰值为 819 GB/s，最大可选内存容量为 512 GB，TDP 约为 200-250W（整机功耗），采用内存共享架构。

## Evidence

[质询]参考来源仅涉及Mac Studio大模型运行能力的定性讨论，未提供M4 Ultra具体的内存带宽、容量选项及TDP数值，无法直接验证这些具体硬件参数。 | 逻辑自洽（M4 Ultra确为512GB/819GB/s规格，TDP量级合理），但参考来源[1]仅讨论大模型适用性，未包含具体硬件参数，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2026394148693979279&rut=dab9c82840be134f6457d5a9408726c4869b1a59d2372c599cb98bfc5304e5ae', 'type': 'ddg', 'title': '128GB 以上统一内存的 Mac Studio，哪一代真正能跑大模型？'}
