# N246: Qwen3-27B 的 FFN 中间维度 (d_ff) 需从模型配置文件中确认，通常约为 d_model 的 2.7 倍（如 4096 * 2.7 ≈ 1100

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

Qwen3-27B 的 FFN 中间维度 (d_ff) 需从模型配置文件中确认，通常约为 d_model 的 2.7 倍（如 4096 * 2.7 ≈ 11008），该参数直接决定 FFN 激活内存大小，是计算 Act_Mem 的关键缺失变量，原公式中未包含 d_ff 导致估算偏差。

## Corrected Claim

Qwen3-27B 的 FFN 中间维度 (d_ff) 需从模型配置文件中确认，通常约为 d_model 的 2.7 倍（具体数值需查证），该参数直接决定 FFN 激活内存大小，是计算 Act_Mem 的关键变量。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于参数确认与合理性验证（事实层面），子节点2聚焦于参数错误导致的后果量化（影响层面），两者维度不同，无重复或矛盾。父节点强调了'确认参数'和'关键缺失变量导致偏差'两个核心点，两个子节点分别对应了这两点，覆盖完整。不存在多个子节点描述同一参数不同取值导致的冗余。）

## Search Query

Qwen3-27B model config d_ff intermediate size
