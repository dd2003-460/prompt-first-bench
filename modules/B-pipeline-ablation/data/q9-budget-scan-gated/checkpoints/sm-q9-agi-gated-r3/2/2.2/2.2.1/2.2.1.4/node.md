# N67: 上下文累积效应：第i次迭代时的prompt长度为2k + (i-1)*1.5k，第i次迭代的prefill延迟与prompt长度成正比，总prefill延迟 =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

上下文累积效应：第i次迭代时的prompt长度为2k + (i-1)*1.5k，第i次迭代的prefill延迟与prompt长度成正比，总prefill延迟 = Σ_{i=1}^{k} c*(2k+(i-1)*1.5k)，c为每token prefill成本

## Corrected Claim

上下文累积效应：第i次迭代时的prompt长度为2k + (i-1)*1.5k，第i次迭代的prefill延迟与prompt长度成正比，总prefill延迟 = Σ_{i=1}^{k} c*(2k+(i-1)*1.5k)，c为每token prefill成本

## Evidence

先验知识/题面给定，逻辑校验通过：公式正确表达了线性累积长度的求和过程，量纲与逻辑自洽。
