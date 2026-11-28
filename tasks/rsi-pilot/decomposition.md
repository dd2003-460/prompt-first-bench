# origin: ai
# RSI pilot: 用质疑状态机规划主线并产出可测量改进
# 来源: D 2026-11-28 "最便宜的是你直接开始分解规划我要的东西，然后拿这套做出来有实际提升的，那不就是rsi了"
# 关联: tasks/d-general-judgment/questioning-state-machine.md (机制), research-agi-budget (主线)

## 最终目标（不可改）
证明质疑状态机端到端可用：用它分解主线 → 缺口注册表第一实例 → 选最便宜缺口 → 产出可测量改进(A/B 判决) → 写回系统。
本 run 本身就是状态机的端到端验证（对应 G4：verdict 是否真的改变系统行为）。

## R1 记录（done, 判断-Lead, 2026-11-28）
对主线前提四刀质疑 + 自驳：
- 方向（预算控制移动前沿）→ 反驳不了（无数据）→ G1 (frontier, 实验④在队列)
- 前人（framing 级 prior art）→ 反驳不了（未调研）→ G2 (open, 检索)
- 更快（电池减域）→ 可反驳（预注册已 commit）→ 丢弃
- 性价比（电池值不值）→ 可反驳（D 指令给定）→ 丢弃
- 自身（T1 注入内容）→ 反驳不了（从未 A/B）→ G3 (open, 本 pilot 的 R3 定案)
- 自身（端到端效力）→ 反驳不了（无 run）→ G4 (open, 本 pilot 定案)
产出: gap-registry.yaml（4 gaps + 2 discarded）。

## 任务表
| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
|------|------|--------|--------|---------|------|
| R1 主线四刀质疑 → gap-registry.yaml | 无 | 200 | 60 | 1 | 判断-Lead ✅ |
| R3a A/B 探针: 旧 T1 文案 vs 缺口定位注入, n=3×2, 先 commit 预注册 | R1(G3) | 150 | 80 | 2 | sub-27b ✅ (6/6 成功, 8cb658ce6) |
| R3b 打分+判决 (specificity/actionability 0-2) | R3a | 100 | 40 | 1 | 判断-Lead ✅ (r3b-scores.md, N 4.0 vs O 1.0) |
| R4 写回: T1 注入升级决策 + 机制文档 + 信号台账 | R3b | 50 | 40 | 1 | 判断-Lead ✅ (stage-gate b8d6d17, APPROVALS #6) |
| sm-run3 G5 定案: q9 v2 幂等假阳性 是/否 + 根因 | 无(sm-run2 产生) | 200 | 30 | 1 | sub-27b (sa-0-5c54cfaf, 任务卡 sm-run3-g5-taskcard.md) |

## 预注册（R3a 数据生成前 commit；判据/材料/条件先落盘，红线）
- 场景（固定，不含"缺口"字样）："你在修一个脚本，同一个报错签名已经连续出现 5 轮，改了 5 次都没修好，任务还没完成。停下来想一想，接下来怎么办？"
- 臂 O（旧）：现行 T1 反思注入文案——sub 从 tools/stage-gate/stage_gate/adapters/stop_hook.py 提取原文（不信记忆），逐字使用
- 臂 N（新）："停下来：当前工作中，你具体在哪里反驳不了自己/不确定？给出 {具体陈述, 你为什么反驳不了, 什么证据能定案}。不要给泛泛的反思。"
- 模型: 127.0.0.1:8787 qwen3.8-27b-mtp, temp 0.7, n=3/臂, max_tokens 2048
- 抓取: content + reasoning 双字段（T2 实证: 27b 机制推理藏在 reasoning，只抓 content 系统性低估）
- 打分（0-2，判据先 commit，Lead 判）:
  - specificity: 2=指出与场景绑定的具体点(具体报错/文件/机制) 1=指了方向但不具体 0=泛泛元话语("应该更仔细")
  - actionability: 2=定案证据是具体可执行的检查/实验 1=给了证据类别不具体 0=无可执行证据
- 判决: mean(N)-mean(O) ≥1 → 缺口定位式胜，R4 升级 T1 注入; 0~1 → 不显著，G3 保持 open; <0 → 负结果，保留旧文案并记录
- 污染控制: 场景两臂相同; 臂 N 不泄露打分判据; 打分时 Lead 不知输出来自哪臂（先匿名编号再揭盲）

## 边界
- 不动 stop_hook.py（R4 判决后才决策; 框架源码改动=红线类，需 APPROVALS 留痕）
- 8787 上 K2/K3 在跑: 探针仅十余个短调用，可接受; 排队严重则顺延
- 本 pilot 不扩展状态机设计，只验证 G3（G2 检索另行派 arena）
