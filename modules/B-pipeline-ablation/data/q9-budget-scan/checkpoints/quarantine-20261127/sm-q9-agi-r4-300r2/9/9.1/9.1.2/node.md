# N212: Experiment 节点的 protocol_steps[] 数组中，每一步必须包含 executable_code_ref（指向 Git 仓库的具体 com

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Experiment 节点的 protocol_steps[] 数组中，每一步必须包含 executable_code_ref（指向 Git 仓库的具体 commit hash）和 expected_runtime（秒），以确保实验的可复现性和超时控制。

## Corrected Claim

Experiment 节点的 protocol_steps[] 数组中，每一步必须包含 executable_code_ref（指向 Git 仓库的具体 commit hash）和 expected_runtime（秒），以确保实验的可复现性和超时控制。

## Evidence

先验知识/题面给定，逻辑校验通过
