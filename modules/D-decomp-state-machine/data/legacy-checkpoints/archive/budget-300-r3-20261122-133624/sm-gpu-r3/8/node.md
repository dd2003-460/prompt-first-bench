# N41: Qwen3-27B 在 RTX 4090 (BF16, 24GB) 下因显存溢出无法直接运行；在 INT8 (GPTQ) 下，Decode 吞吐量约为 15-2

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 RTX 4090 (BF16, 24GB) 下因显存溢出无法直接运行；在 INT8 (GPTQ) 下，Decode 吞吐量约为 15-20 tokens/s (batch=1)，Prefill 吞吐量约为 800-1000 tokens/s；在 H100 (BF16, 80GB) 下，Decode 吞吐量约为 40-50 tokens/s，Prefill 吞吐量约为 3000-4000 tokens/s。

## Corrected Claim

Qwen3-27B（或同参数量级模型）在 RTX 4090 (24GB) 下因显存不足无法直接以 BF16 运行；在 INT8 量化下，Decode 吞吐量通常在 10-20 tokens/s 量级，Prefill 吞吐量在 800-1000 tokens/s 量级；在 H100 (80GB) 下，Decode 吞吐量约为 40-50 tokens/s，Prefill 吞吐量约为 3000-4000 tokens/s。

## Evidence

父节点级核验未通过：不完备（子节点存在明显的内容缺失。父节点明确指出 'Qwen3-27B 在 RTX 4090 (BF16, 24GB) 下因显存溢出无法直接运行'，但两个子节点均未包含这一关键事实（子节点1只讲了H100，子节点2只讲了比值对比）。此外，子节点2引入了父节点未提及的TCO和成本分析，虽然不矛盾，但属于额外信息；核心问题是漏掉了RTX 4090 BF16不可行的事实。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=8fa78de888ac263b600c3c76a2f605da5d22c3a9ac7bbded9dfaedc0352e1d96', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
