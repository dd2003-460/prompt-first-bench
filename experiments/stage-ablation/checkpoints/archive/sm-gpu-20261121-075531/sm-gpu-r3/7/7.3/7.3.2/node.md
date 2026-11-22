# N336: 在 INT8 双卡 (TP=2) 工作点下，每层 AllReduce 通信量约为 hidden_size * 2 * batch_size bytes (27B

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

在 INT8 双卡 (TP=2) 工作点下，每层 AllReduce 通信量约为 hidden_size * 2 * batch_size bytes (27B 模型 hidden_size=4096, 每层约 8KB/step)，在 PCIe 4.0 x8 (有效带宽 ~3.5GB/s) 下，每层通信延迟约 2.3us，总延迟占比低，但 ROCm 后端对多卡同步的优化程度低于 NCCL，实测 TPS 可能比理论值低 15-25% [待核验]。

## Corrected Claim

在 INT8 双卡 (TP=2) 工作点下，每层 AllReduce 通信量约为 hidden_size * 2 * batch_size bytes (27B 模型 hidden_size=4096, 若 batch_size=1 则每层约 8KB/step)，在 PCIe 4.0 x8 (有效带宽 ~3.5GB/s) 下，每层通信延迟约 2.3us (batch_size=1 时)，总延迟占比低，但 ROCm 后端对多卡同步的优化程度低于 NCCL，实测 TPS 可能比理论值低 15-25% [待核验]。

## Evidence

[质询]数值量级存在严重矛盾：27B模型hidden_size=4096，batch_size通常远大于1，若按公式 hidden_size * 2 * batch_size 计算，每层通信量不可能仅为8KB（除非batch_size=1且数据类型为int8，但8KB对应的是4096*2*1，这与'每层约8KB/step'的表述在常规推理场景下量级不符，且2.3us延迟对于8KB数据在3.5GB/s带宽下计算正确，但8KB数据量对于27B模型的双卡AllReduce来说过小，通常AllReduce涉及的是激活值或梯度，量级应在MB级别，此处可能存在对'每层通信量'定义的错误理解或数值笔误）。 | 逻辑校验发现数值量级不合理：27B模型hidden_size=4096，若batch_size=1，INT8下每层AllReduce通信量约为4096*2=8KB，但实际推理中batch_size通常>1，且AllReduce通常针对整个hidden state，量级应随batch_size线性增长。若batch_size=1，8KB/3.5GB/s≈2.3us计算正确，但'每层约8KB/step'的表述暗示这是一个固定值，忽略了batch_size的影响，且对于27B模型，通常关注的是总通信量或每token通信量，此处表述易引起误解。此外，ROCm性能低于NCCL 15-25%是经验事实，缺乏来源支持，但主要问题在于通信量数值与模型规模的匹配性存疑。
