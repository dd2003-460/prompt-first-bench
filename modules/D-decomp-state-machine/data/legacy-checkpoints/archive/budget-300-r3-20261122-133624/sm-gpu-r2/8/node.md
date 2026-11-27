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

父节点级核验未通过：不完备（子节点1仅覆盖H100性能及硬件特性，子节点2仅覆盖对比比值及TCO分析。父节点中关于RTX 4090在BF16下显存溢出无法运行、以及RTX 4090在INT8下的具体吞吐量数值（15-20 tokens/s Decode, 800-1000 tokens/s Prefill）在子节点中均未直接陈述，仅通过比值间接体现，导致关键事实缺失。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=8fa78de888ac263b600c3c76a2f605da5d22c3a9ac7bbded9dfaedc0352e1d96', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
