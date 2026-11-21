# origin: ai
# 套磁附带产出索引：TCO 结构化分解 × 动态贡献因子（金融/社科方向）
# 触发：D 2026-11-21 指令"单独开一个放套磁，可以作为 gpu 的附带产出，金融那边留索引"

## 核心亮点（D 定调）
**动态贡献因子评估的 TCO + 结构化分解**——
- TCO 决策模型按 5 层分解树展开（持有成本=摊销+电费+故障 / 利用率 / 性能构成 / 量化通过率 / 候选筛选）
- 每个参数带**动态贡献因子**：敏感度倍数（BOUND 8x/1.57x/1.88x）× 时间尺度依赖
  （市场因素在短尺度显著、长尺度被摊销稀释）× 黑盒区间
- 完备性判据 = 覆盖各时间尺度下 p99 贡献因素（D 的动态 p99 定义）

## 现有资产（gpu 实验副产品）
| 资产 | 路径 | 状态 |
|---|---|---|
| TCO gold 树（37 节点/5 层/17 叶子） | bench/rubric-v3/ablation/gold-tree.md | 完整 |
| TCO rubric（38 判定点×3-6 档） | bench/rubric-v3/ablation/gold-Q8.md | 完整 |
| 动态贡献因子定义（BOUND 倍数） | gold-Q8.md 内 ★F-B/F-C 标注 | 完整 |
| 模型实际 TCO 产出（两臂） | experiments/stage-ablation/runs-s5-sm-gpu-*.json | 仅 L1-L2 概念层 |
| 预算 tradeoff 调研（空白区确认） | modules/B-pipeline-ablation/research/budget-sensitivity-goal-spec-survey-20261121.md | 已提交 603c8ba8a |

## 质量现状（诚实标注，套磁时不夸大）
- 两臂（SM/裸）TCO 均停在 L1-L2：提到概念+硬件规格，**无 $/h 数字推导**
- 缺口 = 目标函数表述（预算 tradeoff 未写入 prompt）+ rubric 无时间尺度维度
- 可验证假设：prompt-v2（预算 tradeoff 表述）→ TCO 深度是否 0.34→0.5+（matched 批后开跑）

## 套磁目标画像（金融/社科）
- 成本效益分析 / TCO / 计算经济学方向教授
- 可 pitch 点：LLM 做 TCO 决策的结构化分解框架 + 动态敏感性（学界空白，见调研文件）
- 撞车注意：相邻线 2（LLM 做敏感性分析，OptMetaOpenFOAM 2503.01273）最接近，pitch 时区分
  "LLM 是决策模型产出者" vs "LLM 是外部模型分析执行者"

## 待办
- [ ] prompt-v2 A/B 出数据后回填"质量现状"（假设验证结果）
- [ ] 套磁执行走 skill academic-outreach（发现/起草/发送/跟进）
- [ ] 金融方向文献索引：待补（TCO × LLM 决策的社科侧文献，当前调研只覆盖 arXiv 侧）
