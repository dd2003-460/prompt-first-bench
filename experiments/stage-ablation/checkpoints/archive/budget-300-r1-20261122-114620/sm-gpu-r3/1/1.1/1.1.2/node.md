# N40: Qwen3-27B 实际架构配置：num_layers=64, num_kv_heads=8 (GQA 8:1), head_dim=128，验证 KV Cac

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 实际架构配置：num_layers=64, num_kv_heads=8 (GQA 8:1), head_dim=128，验证 KV Cache 公式输入参数

## Corrected Claim

Qwen3-27B 采用 GQA 架构，具体参数（num_layers=64, num_kv_heads=8, head_dim=128）需查阅官方模型配置文件（config.json）以最终确认。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3和子节点4本质上是同一公式（KV Cache总显存/总显存）在不同硬件参数下的计算实例，属于冗余；此外，子节点1中关于'修正'的叙述逻辑混乱，先给出错误结论再自我修正，且未明确区分'单层'与'总层数'的表述，易造成理解歧义。）

## Search Query

Qwen3-27B model config num_layers num_key_value_heads head_dim

## Retrieval Sources

- {'url': 'https://github.com/QwenLM/Qwen3', 'type': 'bing', 'title': 'GitHub - QwenLM/Qwen3: Qwen3 is the large language model series ...'}
- {'url': 'https://huggingface.co/collections/Qwen/qwen3', 'type': 'bing', 'title': 'Qwen3 - a Qwen Collection - Hugging Face'}
- {'url': 'http://arxiv.org/abs/2408.11104v3', 'type': 'arxiv', 'title': 'ConFIG: Towards Conflict-free Training of Physics Informed Neural Networks'}
