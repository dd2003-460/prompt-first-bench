# N67: OOM 失败的主导因素是内存峰值而非平均内存：在 PyTorch 任务中，GPU/内存峰值利用率 P_peak 与 OOM 概率 P_oom 呈 Sigmoid

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

OOM 失败的主导因素是内存峰值而非平均内存：在 PyTorch 任务中，GPU/内存峰值利用率 P_peak 与 OOM 概率 P_oom 呈 Sigmoid 关系，P_oom = 1 / (1 + exp(-(P_peak - 0.85) / 0.05))，当 Mem_max=4GB 时，若模型加载后静态占用 2.5GB，动态激活值超过 1.5GB 即触发 OOM，需将 Mem_max 提升至 6GB 或限制 batch_size 以降低 P_peak。

## Corrected Claim

OOM 失败的主导因素是内存峰值而非平均内存：在 PyTorch 任务中，GPU/内存峰值利用率与 OOM 概率通常呈正相关（近似 Sigmoid 关系），当静态占用加动态激活值超过显存上限时即触发 OOM，需提升显存限制或降低 batch_size 以控制峰值。

## Evidence

[质询]Sigmoid 函数的具体参数（中心点 0.85，斜率 0.05）及特定内存阈值（2.5GB/1.5GB）属于高度依赖具体硬件、PyTorch 版本及模型结构的经验数据，并非普适的物理或数学定律，缺乏通用性支撑。 | source=knowledge，逻辑自洽（峰值决定OOM符合内存管理基本原理），但具体拟合参数和数值阈值属于经验事实，无来源支持且非第一性原理可严格推导，故降级。

## Search Query

PyTorch memory peak vs average OOM probability sigmoid model
