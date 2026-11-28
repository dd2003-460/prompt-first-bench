# N109: 验证开销模型：定义单步验证成本 C_verify = T_prefill_batch_size * T_forward_pass_per_token，其中 ba

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

验证开销模型：定义单步验证成本 C_verify = T_prefill_batch_size * T_forward_pass_per_token，其中 batch_size 为草稿 token 数（此处为 4），T_forward_pass_per_token 为 V100 上处理单个 token 的前向传播耗时（需实测，预计 ~10-20ms/token for 27B on 4xV100）

## Corrected Claim

验证开销模型：定义单步验证成本 C_verify = T_prefill_batch_size * T_forward_pass_per_token，其中 batch_size 为草稿 token 数（此处为 4），T_forward_pass_per_token 为 V100 上处理单个 token 的前向传播耗时（需实测，预计 ~10-20ms/token for 27B on 4xV100）

## Evidence

先验知识/题面给定，逻辑校验通过：验证开销模型定义符合自回归解码中批量前向传播的计算逻辑，batch_size=4对应草稿token数，V100集群处理27B模型单token耗时10-20ms的量级在工程实践中合理（取决于并行策略和精度），无内部矛盾。

## Search Query

speculative decoding verification overhead cost model
