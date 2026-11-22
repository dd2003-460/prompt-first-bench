# N9: 消费级单卡候选集筛选：显存容量必须 >= 24 GB 以支持 4-bit 量化 + 32K 上下文。候选包括 RTX 3090 (24GB), RTX 4090

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

消费级单卡候选集筛选：显存容量必须 >= 24 GB 以支持 4-bit 量化 + 32K 上下文。候选包括 RTX 3090 (24GB), RTX 4090 (24GB), RTX 4090D (24GB), RTX 5090 (32GB) [待核验: 5090 实际显存大小]。

## Corrected Claim

消费级单卡候选集筛选：显存容量必须 >= 24 GB 以支持 4-bit 量化 + 32K 上下文。候选包括 RTX 3090 (24GB), RTX 4090 (24GB), RTX 4090D (24GB)。RTX 5090 因显存规格未在参考来源中证实，暂不列入确定候选或需进一步核验。

## Evidence

[质询]RTX 5090 的显存容量为 32GB 属于经验事实（硬件规格），参考来源中未包含该具体数值，且无法仅凭逻辑推导得出，存在来源缺失风险。 | 来源[1]和[2]直接支持了24GB显存（如RTX 4090）在4-bit量化下运行大模型的可行性及显存需求逻辑，但所有来源均未提及RTX 5090的具体显存大小，该部分为经验事实且缺乏直接来源支持。

## Search Query

RTX 5090 VRAM size release date price

## Retrieval Sources

- {'url': 'https://juejin.cn/post/7683779777371897908&rut=f5f68ceb4271b4bc09247a1388b418905a782b9c706197290530192eb4bc706f', 'type': 'ddg', 'title': '4-bit 量化"几乎无损"？把它放进 Agent 循环里再试一次一、先把账算清楚：一张 24 GB 显卡里到底住了谁 - 掘金'}
- {'url': 'https://developer.aliyun.com/article/1754339&rut=c09abb4a10517404b914d95dfdaa18dee750cb48dfbff585280e9b30dadc6c33', 'type': 'ddg', 'title': 'RTX4090单卡跑Qwen3-32B实践：4bit量化+Transformers与vLLM双方案部署差异.193'}
- {'url': 'https://blog.csdn.net/weixin_29253711/article/details/158443977&rut=7c3f4eaa9b20ac555b39bf48342fca0788425a8bb6ab4b60e5a04be40086d580', 'type': 'ddg', 'title': 'MLC-LLM模型量化实战：用4-bit量化在消费级显卡运行7B大模型'}
