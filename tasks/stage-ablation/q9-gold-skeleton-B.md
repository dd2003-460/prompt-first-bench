# Q9 D2 gold 骨架 B（交叉验证，arena 独立产出）

> 独立性声明：未读 experiments/stage-ablation/tasks/q9-gold-skeleton-A.md（卡 A 交付物）；本文是对任务卡 A 同一问题（5 因子分解树）的独立回答，按 GitHub 开源实现 → arXiv/见刊 → 交叉验证 → 自己推的顺序调研。
> 核验纪律：arXiv ID 逐个 abs 页核验（2604.19809、2605.14186、2310.19791 均通过）；凭记忆 ID：无使用、无被证伪记录；论文/社区自报数字标 [待交叉验证]；无法核验项标「未验证」。
> 节点格式：[因子] claim | 测量口径 | 来源 URL | conf(0-1)。三条硬规则：①各参数定值或显式声明“模型自选且 gold 按模型选的值重算”；②各因子均在题面可见；③定稿后冻结，改动需 D 确认。

## 根节点（排序键：单位预算闭环成功率）
[根] 排序键=单位预算闭环成功率=gap 标记→补全→补全后 verified/(verified+contradicted) 占比（metacog_axis post_acc；unverifiable 与 ambiguous 不进分母）；预算硬上限 150 节点（定值，非下限） | 口径：每条根-叶路径累计节点数≤150；闭环漏斗=启动数→标记 gap 数→补全数→verified 数；分母仅 verified+contradicted | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-agi-question-v0.md（题面 v1 @8a9c45bfa，已读取核验） | conf 0.92

## 因子 1：模型能力轴
[模型能力轴] 基模型=Qwen3-27B NVFP4，硬件=4× V100-SXM2-16GB（cc 7.0，TP=4），vLLM 服务 max_model_len=262144，不改权重仅用 prompt+外部工具 | 口径：与题面硬件/模型一致；按节点计数统计推理消耗 | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-agi-question-v0.md | conf 0.92
[模型能力轴] 单流生成吞吐社区自报：4× V100-16G Qwen3-27B NVFP4 ≈353 tok/s；单 V100-SXM2-32GB NVFP4（Lapilli）生成 ≈88 tok/s、prefill ≈697 tok/s（均为社区自报，未经本方复现） | 口径：tok/s 与 TTFT，折算每研究节点 wall-clock 上限 | https://www.reddit.com/r/LocalLLM/comments/1wsyl8e/v100_qwen_38_27b/ | conf 0.5 [待交叉验证]
[模型能力轴] LLM 具备元认知监测信号（FOK/JOL 与正确率相关），但不自行将监测转为控制动作（重试/验证/停止），监测-控制闭环需外部 harness 完成 | 口径：AUROC/ECE 监测质量；外部控制前后 CFR 变化 | https://arxiv.org/abs/2605.14186 | conf 0.85
[模型能力轴] 外部元认知控制将 Confident Failure Rate 从 0.600 降至 0.143（-76% @ temperature 0；5 模型/4 实验室均值 -70% @ 0.7）；告知模型自身校准分数无显著改善（p>0.05）；组合自预测普遍失败（校准误差 0.500-0.943） | 口径：CFR 前后对比；Exp3 组合校准误差 | https://arxiv.org/abs/2604.19809 | conf 0.88
[模型能力轴] 元认知增益随模型规模的曲线本方不可测（仅 27B 一款模型，无 7B/70B 对照，标为能力边界）；temperature=0 作定值，模型自选则 gold 按模型选值重算 | 口径：参数定值声明；增益曲线标记为本方能力边界 | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-gold-skeleton-arena-taskcard.md（硬规则①） | conf 0.9 「未验证」（本方无对照模型）

## 因子 2：预算轴
[预算轴] 总预算 150 研究节点（定值，非下限）；节点=一次检索/生成/验证的原子研究单元，超预算即强制终止 | 口径：节点计数器累计≤150；终止原因统计（预算耗尽 vs 闭环达标） | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-agi-question-v0.md | conf 0.92
[预算轴] 节点成本异质性：prefill 远快于 decode（单 V100-SXM2-32GB NVFP4 prefill ≈697 tok/s vs 生成 ≈88 tok/s，Lapilli 自报）；262K 长上下文 prefill 成本更高 | 口径：每节点 token 数与 wall-clock 计入节点成本 | https://llamaperf.com/model/qwen3-8 | conf 0.5 [待交叉验证]
[预算轴] 在排序键最大化约束下，节点优先分配给“gap 标记→补全→验证”闭环，边际收益递减后停止，不做无差别检索扩展 | 口径：单位预算闭环成功率随节点分配的边际收益曲线 | 推导（未验证） | conf 0.6 「未验证」
[预算轴] 可复用 claim/缓存命中可避免重复发现节点；任务卡背景陈述跨 rep claim 重叠仅 4.7%（库机制可直接攻击浪费），该数字为背景段陈述，未独立复核 | 口径：库命中率 vs 避免的重复发现节点数 | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-gold-skeleton-arena-taskcard.md（记忆轴背景锚点） | conf 0.5 「未验证」

## 因子 3：检索质量轴
[检索质量轴] 外部检索作为可扩展记忆，检索质量直接决定 gap 标定精确度（false positive 将“已知”错标缺口，false negative 漏真缺口） | 口径：检索命中率 vs gap 标定 FP/FN 率 | 推导（未验证） | conf 0.6 「未验证」
[检索质量轴] 检索-补全-验证每轮消耗节点；检索召回率低导致补全盲区，反复检索同一缺口浪费预算 | 口径：每轮节点消耗 vs 补全覆盖率；重复检索次数 | 推导（未验证） | conf 0.6 「未验证」
[检索质量轴] 检索 top-k/相似度阈值为模型自选参数，按硬规则①显式声明，gold 按模型选值重算 | 口径：参数定值声明 | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-gold-skeleton-arena-taskcard.md（硬规则①） | conf 0.9

## 因子 4：记忆轴
[记忆轴] 跨 session/跨 rep 状态保持：verified claim 抽取→相似度注入→省重新发现节点（沿 LILO/DreamCoder 库学习范式搬到研究 claim 库） | 口径：claim 库命中率；避免的重复发现节点数 | https://arxiv.org/abs/2310.19791 | conf 0.78
[记忆轴] 库内仅存 verified claim，contradicted/ambiguous 不入库，防止库污染 post_acc 分母与相似度注入 | 口径：入库过滤规则；库内 verified 占比 | 推导（未验证） | conf 0.65 「未验证」
[记忆轴] LILO 证实库学习显著提升解题率（REGEX +33.14 vs DreamCoder），但迁移至“150 节点研究预算”场景的增益未测 | 口径：库前/库后闭环成功率对比 | https://arxiv.org/abs/2310.19791 | conf 0.7 [待交叉验证]

## 因子 5：自我认识闭环
[自我认识闭环] 三段闭环：gap 标记（判断信息是否足够）→ 主动补全（检索/代码获取缺失信息）→ 补全后 verified 判断；元认知监测不自转控制，需外部 harness 控制重试与停止 | 口径：闭环完成数/启动数；verified/(verified+contradicted) | https://arxiv.org/abs/2605.14186 | conf 0.85
[自我认识闭环] post_acc 分母口径：verified+contradicted 计入分母，unverifiable（查完知道“查不到”）与 ambiguous 不进分母；unverifiable 是健康缺口不算自我认识失败 | 口径：分母构成计数；漏斗每段通过率 | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-agi-question-v0.md（题面 v1 排序键段） | conf 0.9
[自我认识闭环] 可中止条件：verified 达阈值或节点耗尽即停，避免 over-verify 浪费预算；阈值为模型自选参数，按硬规则①声明 | 口径：每条路径终止原因统计 | 推导（未验证） | conf 0.6 「未验证」
[自我认识闭环] 在 150 节点内无法验证的因子标为能力边界：模型规模元认知增益曲线（仅 27B 对照缺失）、跨 rep claim 重叠 4.7%（背景段未独立复核） | 口径：能力边界清单随执行记录附记 | https://github.com/dd2003-460/prompt-first-bench/blob/thinkmech-review/experiments/stage-ablation/tasks/q9-gold-skeleton-arena-taskcard.md | conf 0.8 「未验证」

## 附录：因子间依赖/交互表（本方推导，「未验证」）
| 因子对 | 耦合方式 | 对单位预算闭环成功率的影响 |
| 预算×检索质量 | 检索越频繁越耗节点；召回不足导致反复检索同一缺口 | 下降（节点被非闭环轮次消耗） |
| 记忆×预算 | claim 库命中避免重复发现，节省节点用于闭环 | 上升（库命中率越高收益越大） |
| 模型能力×自我认识闭环 | 元认知监测不自转控制，需外部 harness 才能触发重试/验证 | 决定闭环完成率与 verified 占比 |
| 检索质量×自我认识闭环 | gap 标定精度直接影响补全是否命中真缺口 | 决定 verified/(verified+contradicted) 的分子 |
| 预算×记忆 | 库维护本身消耗节点，与命中节省存在盈亏平衡 | 命中率低于盈亏点时净下降 |
