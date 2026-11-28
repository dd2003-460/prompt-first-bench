# N22: 显存带宽与容量参数溯源：记录每个候选GPU的HBM/GDDR显存大小（GB）、带宽（GB/s）、位宽，标注来源；对于非主流卡（如MI300X）需单独检索官方规格

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

显存带宽与容量参数溯源：记录每个候选GPU的HBM/GDDR显存大小（GB）、带宽（GB/s）、位宽，标注来源；对于非主流卡（如MI300X）需单独检索官方规格页，置信度<0.8标[待核验]

## Corrected Claim

显存带宽与容量参数溯源：记录每个候选GPU的HBM/GDDR显存大小（GB）、带宽（GB/s）、位宽，标注来源；对于非主流卡（如MI300X）需单独检索官方规格页，置信度<0.8标[待核验]

## Evidence

该节点为方法论/流程指令，逻辑自洽；参考来源[1][2][3]提供了显存带宽计算基础及HBM/GDDR技术背景，支持该流程中涉及的参数定义与检索必要性，虽未直接包含MI300X具体数值，但作为操作指南其逻辑成立且无矛盾。

## Search Query

NVIDIA RTX 4090 VRAM bandwidth GB/s spec, AMD MI300X HBM3 capacity bandwidth official spec

## Retrieval Sources

- {'url': 'https://blog.csdn.net/essencelite/article/details/166794254&rut=51c3da4ff06c696719a8186d35031a07bd554efde4ca420d9212fc7079cef30f', 'type': 'ddg', 'title': '显存与内存带宽全景解析：从DDR/GDDR到HBM，再到NVLink/PCIe数据搬运_显存带宽和内存带宽-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29102619/article/details/164892995&rut=b283f6557e5ec11645d6a538ef4204fd09730b5a5b140fcbb90e0953e24dae08', 'type': 'ddg', 'title': 'Gpu显存带宽瓶颈深度解析：Lpddr/Gddr/Hbm实战对比 - Csdn博客'}
- {'url': 'https://geek-doc.cn/chip-design/intermediate/gpu-memory-hbm-gddr&rut=c0f77b8961c8d8b83999420c586f025e2c2972faa70763bba46e30288393e9e0', 'type': 'ddg', 'title': 'Hbm Gddr 显存：Gpu 带宽之争，两条封装路线的数字对比'}
