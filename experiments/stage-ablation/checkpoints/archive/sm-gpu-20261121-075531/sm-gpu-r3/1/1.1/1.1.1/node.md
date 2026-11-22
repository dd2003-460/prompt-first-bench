# N35: Qwen3-27B 的精确参数总量（Total Parameters）需从 HuggingFace 模型卡或 config.json 中提取，以修正 27B 的

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Qwen3-27B 的精确参数总量（Total Parameters）需从 HuggingFace 模型卡或 config.json 中提取，以修正 27B 的近似值（例如实际可能是 26.8B 或 27.2B），从而精确计算各精度下的权重字节数（Bytes = Params * Bits/8）。

## Corrected Claim

Qwen3-27B 的近似参数总量为 27B（270亿），精确参数总量需查阅 HuggingFace 模型卡或 config.json 中的 total_parameters 字段以获取确切数值（例如 26.8B 或 27.2B），进而精确计算各精度下的权重字节数。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了配置参数提取、参数量计算逻辑、以及基于该参数量的存储字节数计算，三者逻辑递进且内容互不重叠，完整实现了父节点关于'提取-修正-计算'的目标。）

## Search Query

Qwen3-27B huggingface config.json num_parameters total

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2055287697623856945&rut=9eeddf0f14c1c269f39d9ab19c2f4848dd4aa0eac931137b38cbe095a39ec949', 'type': 'ddg', 'title': 'Qwen 3.6 27B深度评测：27B参数单挑397B，本地跑AI编程的时代来了'}
