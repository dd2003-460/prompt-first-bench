# N10: 数据中心级单卡候选集筛选：显存容量必须 >= 40 GB 以支持 BF16/FP8 或大上下文。候选包括 A100 (40/80GB), H100 (80GB)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

数据中心级单卡候选集筛选：显存容量必须 >= 40 GB 以支持 BF16/FP8 或大上下文。候选包括 A100 (40/80GB), H100 (80GB), L40S (48GB), H200 (141GB)。

## Corrected Claim

数据中心级单卡候选集筛选：通常建议显存容量较大（如 40 GB 以上）以支持 BF16/FP8 或大上下文。常见候选包括 A100 (40/80GB), H100 (80GB), L40S (48GB), H200 (141GB) 等。

## Evidence

[质询]来源未直接提供 A100/H100/L40S/H200 的具体显存数值，且‘>= 40 GB’作为硬性门槛缺乏来源直接支持（例如 L40S 48GB 虽满足，但 24GB 卡在某些 FP8 场景下也可能通过优化运行，门槛设定可能过于绝对或特定于大上下文场景）。 | 经验事实，逻辑自洽但缺来源直接支持具体显存数值及硬性门槛；来源[1][2]提及相关卡型与精度，但未直接列出所有卡型的显存规格以证实‘>=40GB’的普适性。

## Search Query

NVIDIA H100 A100 L40S H200 VRAM specifications price

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00307/article/details/171100922&rut=ef4f3124a07f1ce77552f2ae913ac843ac66f966082ef4d283534504b0510459', 'type': 'ddg', 'title': 'DaisyRose-27B 量化部署指南：BF16 / FP8 / NVFP4 显存占用与单卡硬件选型完整清单-CSDN'}
- {'url': 'https://juejin.cn/post/7673866197453209619&rut=c1083e543cbcf868261dc6d234389d999366535a0143fa6dce71b2cb20a38abb', 'type': 'ddg', 'title': '大模型显卡需求速查表：推理、训练、微调显存公式与选型指南汇总大模型推理、预训练、微调三类场景的显存估算公式与实战选型建议 - 掘金'}
- {'url': 'https://wiki.hynx.com.cn/entries/llm-quantization-bf16-fp8-int8-int4/&rut=661359bcac57e138ed6c1f3ddce0295982921911ec96753f8c1383cf39fffd4d', 'type': 'ddg', 'title': '大模型推理精度与量化怎么选：BF16、FP8、INT8与INT4'}
