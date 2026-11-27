# N340: 性价比指标定义为 $Value_{score} = \frac{Throughput_{eff}}{TCO_{annual}}$，其中 $Throughput_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N111

## Claim

性价比指标定义为 $Value_{score} = \frac{Throughput_{eff}}{TCO_{annual}}$，其中 $Throughput_{eff} = Throughput_{theory} \times \eta_{impl}$，$\eta_{impl} \in [0.6, 0.8]$ 为硬件实现效率系数（需针对具体框架如 vLLM/TensorRT-LLM 实测校准），$TCO_{annual} = TCO_5 / 5$。

## Corrected Claim

性价比指标定义为 $Value_{score} = \frac{Throughput_{eff}}{TCO_{annual}}$，其中 $Throughput_{eff} = Throughput_{theory} \times \eta_{impl}$，$\eta_{impl} \in [0.6, 0.8]$ 为硬件实现效率系数（需针对具体框架如 vLLM/TensorRT-LLM 实测校准），$TCO_{annual} = TCO_5 / 5$。

## Evidence

先验知识/题面给定，逻辑校验通过
