# N88: 在 4x V100 上启用 vLLM 的 Logprobs 返回功能以计算 HR 指数，额外增加的 GPU 显存占用约为 2-4 GB（取决于 batch si

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

在 4x V100 上启用 vLLM 的 Logprobs 返回功能以计算 HR 指数，额外增加的 GPU 显存占用约为 2-4 GB（取决于 batch size 和序列长度），且导致推理吞吐量下降约 5-10%，需在 max-num-seqs=8 配置下实测对端到端延迟的影响。

## Corrected Claim

在 4x V100 上启用 vLLM 的 Logprobs 返回功能会增加额外的 GPU 显存占用并导致推理吞吐量下降，具体数值取决于 batch size、序列长度及模型规模，建议在 max-num-seqs=8 配置下实测对端到端延迟的影响。

## Evidence

父节点级核验未通过：不完备（子节点分别关注显存占用和通信/计算延迟，维度正交且不重叠。但父节点明确要求'实测对端到端延迟的影响'，而子节点仅提供了理论估算（显存公式和PCIe传输时间），未涵盖'实测'这一关键执行步骤或验证方法，导致覆盖不全。）

## Search Query

vLLM logprobs overhead memory usage inference latency impact throughput

## Retrieval Sources

- {'url': 'https://github.com/vllm-project/vllm/discussions/1203&rut=d82ce73adb3ae0861a9a80c0ff7d4e250eeed2542deb631f6105fd894be6d354', 'type': 'ddg', 'title': 'How to use logprobs hyperparameters? · vllm-project vllm · Discussion ...'}
