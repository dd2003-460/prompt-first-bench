# N279: 在张量并行（TP）推理中，单次All-Reduce通信的数据量 V_comm 计算公式为：V_comm = 2 * batch_size * hidden_si

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

在张量并行（TP）推理中，单次All-Reduce通信的数据量 V_comm 计算公式为：V_comm = 2 * batch_size * hidden_size * dtype_size * num_layers_per_step（针对Decode阶段每步每层），其中hidden_size=4096, dtype_size=2(BF16)，需代入具体batch_size和层数计算GB数值

## Corrected Claim

在张量并行（TP）推理中，单次All-Reduce通信的数据量 V_comm 计算公式为：V_comm = 2 * batch_size * hidden_size * dtype_size * num_layers_per_step（针对Decode阶段每步每层），其中hidden_size=4096, dtype_size=2(BF16)，需代入具体batch_size和层数计算GB数值

## Evidence

先验知识/题面给定，逻辑校验通过：张量并行中All-Reduce通信量公式符合分布式推理标准原理，参数量级合理。
