# N22: KV Cache 显存占用量化：KV_Size = 2 * Num_Layers * Num_Heads * Head_Dim * Precision_Bits

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

KV Cache 显存占用量化：KV_Size = 2 * Num_Layers * Num_Heads * Head_Dim * Precision_Bits * Seq_Len，Qwen3-27B 若采用 GQA (Grouped Query Attention) 需确认 Num_KV_Heads 具体值以计算 32K 上下文下的额外显存开销，该值直接决定单卡最大并发 Batch Size。

## Corrected Claim

KV Cache 显存占用量化：KV_Size = 2 * Num_Layers * Num_Heads * Head_Dim * Precision_Bits * Seq_Len，Qwen3-27B 若采用 GQA (Grouped Query Attention) 需确认 Num_KV_Heads 具体值以计算 32K 上下文下的额外显存开销，该值直接决定单卡最大并发 Batch Size。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且正交：从单token基础计算（子1）推导到单请求总量（子2），再定义通用计算公式（子3），最后给出具体硬件场景下的实例化计算（子4）。各节点分别覆盖参数定义、单位量级、通用逻辑和具体案例，无重复或矛盾。）

## Search Query

Qwen3-27B architecture GQA Num_KV_Heads head_dim

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1668044&rut=1b109d08b5ca1e4a4f5eb0243eb8a595032fa2da34bde32e5865bd0828b1421f', 'type': 'ddg', 'title': '估算大模型推理KVCache显存占用与计算量-开发者社区-阿里云'}
- {'url': 'https://blog.csdn.net/weixin_30952479/article/details/171068400&rut=07b88c5f9c7721440e438ed34053748e335379bd19fb70ea603500c0defab424', 'type': 'ddg', 'title': 'KV Cache 原理与显存优化：从结构、生命周期到6GB卡跑8B模型-CSDN博客'}
- {'url': 'https://blog.csdn.net/muyao987/article/details/140364179&rut=3bdd32818b6d8a8661311d18c1c1148459e7b485e814fed65e957d29b04a194b', 'type': 'ddg', 'title': '大模型中 KV Cache 原理及显存占用分析 - CSDN博客'}
