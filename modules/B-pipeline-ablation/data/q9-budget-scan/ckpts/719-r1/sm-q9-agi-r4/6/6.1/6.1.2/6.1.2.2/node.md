# N252: GSM8K-CoT 长文变体的构造方法：将原始问题嵌入到 64k/128k/262k 长度的无关数学推导噪声文本中，保持关键实体不变；测量指标为 Exact M

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

GSM8K-CoT 长文变体的构造方法：将原始问题嵌入到 64k/128k/262k 长度的无关数学推导噪声文本中，保持关键实体不变；测量指标为 Exact Match (EM) 准确率；对照组为无噪声原始 GSM8K，ΔAcc 定义为 (Acc_noisy - Acc_clean) / Acc_clean，预期随长度增加 EM 下降 5%-15%

## Corrected Claim

GSM8K-CoT 长文变体的构造方法：将原始问题嵌入到 64k/128k/262k 长度的无关数学推导噪声文本中，保持关键实体不变；测量指标为 Exact Match (EM) 准确率；对照组为无噪声原始 GSM8K，ΔAcc 定义为 (Acc_noisy - Acc_clean) / Acc_clean，预期随长度增加 EM 下降 5%-15%

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了64k和128k两个长度点，遗漏了父节点明确提到的262k长度点，导致覆盖不完备。此外，这两个子节点本质上是同一实验参数（噪声长度）的不同取值，属于典型的参数扫描冗余，而非结构性不同的独立任务模块。）

## Search Query

GSM8K long context noise injection evaluation protocol exact match accuracy drop benchmark
