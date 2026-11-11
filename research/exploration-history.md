# PFB 探索路径全景（编号整理版）

> origin: ai · 2026-11-11 · 成璐指令「s5又是什么，忘了，所以还能重新整理编号和过往探索路径吗」
> 本文件是唯一的"编号→含义"权威映射。旧文档里的裸编号（vN/SN/TN/rN）以本文件为准解读。
> 配套：`numbering-audit-2026-11-11.md`（5 套编号系统的混乱现状 + 迁移清单）。

## 0. 三套编号体系速查

| 前缀 | 含义 | 命名空间 | 例子 |
|------|------|----------|------|
| **S** | 实验臂（ablation arm）——一种 prompt/管线策略 | S0–S8M，跨全部 bench 题共用 | S5 = 层级分解+核验管线臂 |
| **v** | S5 臂内部的 prompt/代码迭代版本 | v3–v17 → T53（连续线，不另起 v18） | v17 = 无限预算层级 INDEX 分解 |
| **T** | 任务 ID（goal 执行单元） | 全局递增，tasks/ 下唯一 | T53 = decomp 状态机重构 |
| **r** | 运行副本 / 迭代轮 | 两个不同命名空间（见 §4） | runs-s5-gpu-v13-r5.json 的 r5 = 第 5 个 rep |

**S5 定义**（最常被忘的一个）：pfb 消融实验里"带真实检索的多步研究管线"那一档。
S0 = 裸 CoT baseline；S1 = 单轮结构化；…；S5 = decompose→search→verify loop→synthesize 四阶段管道
（harness 层真调 research_hook 检索，每节点独立 LLM 校验，失败回炉 ≤K 轮）；S8/S8L/S8C = 质询循环变体。
代码入口 `experiments/stage-ablation/s5_pipeline.py`（P1–P4 线性管线），
层级化扩展 `s5_hierarchy.py`（v17），目标函数驱动重写 `s5_state_machine.py`（T53）。

## 1. 时间线主线（2026-11-06 → 11-11）

### Phase 0 · 建 bench + 四臂基线（11-06~07）
- 5 道事实题（nat/soc/gpu/hw/bio），gold 要点表，judge 口径定稿（rubric v2）。
- 四臂 n=30：**S0=0.5558, S1=0.5746, S5=0.7907**（B-face 跨族 judge 验证方向一致）。
- C-face 判官 FAIL；E3 机制 = 生成时预防。

### Phase 1 · S8 质询循环（11-07）
- S8 = S5 + 矛盾质询 loop；O6（矛盾发现）均值 0.876。
- self-judge vs B-face 对比暴露 self-judge 系统性偏高 ~0.14。
- S8L（长 prompt 发散前段）/ S8C（约束化模板）两轮 → #24 任务类型路由修正为"结构效应待确认"。
- 产出：`runs/s8-report.md`（完整四臂表）。

### Phase 2 · S5 管线硬化（11-08~09，v3→v15）
北极星：S5 稳定超过 S0（nat cov≥0.634, gpu depth≥0.50）→ 可发表消融报告。

| 版本 | 改动 | 结果 |
|------|------|------|
| v3 | 阶段分离原则立项（decomposition-goal-v3.md） | plan only |
| v3–v12 | P1 规则堆叠期（rule 6/7/8/9/9b 逐条加） | nat-v14 mean cov 0.578；gpu 一直 <0.4 |
| v13 | 50-rep 稳定性 runner | FAIL 0.395（gpu）；r5 截断失败 |
| v14 | nat 101 reps 量产 | nat 0.578（仍 < S0 0.637） |
| v15 | rule 9b 敏感性分析 + P4 分析层（阶段分离落地） | smoke 6/6 mean cov 0.361 → 判定"加 rule 是负收益" |

**Phase 2 结论**：prompt 层行为塑造有容量上限，继续加 rule 稀释基础覆盖（v15 + soc rule 7 两个独立证据）。杠杆换方向。

### Phase 3 · 状态机转向（11-09，v16→v16.3）
- v16：P1e 状态机臂——多轮回退分解 + confirmed-fact 注入 + S_α 边际停止（R1 饱和/R2 预算阀/R3 停滞）。
- v16.1：真无限回退（删固定轮数 cap）；v16.2：per-layer cap；v16.3：R2 降软约束 + R4 防御硬帽。
- smoke：nat 首超 S0（+0.03）；gpu 被 R2 硬停杀死。

### Phase 4 · v17 层级 INDEX 分解 + Goodhart 诊断（11-09）
- v17：整题拆大树换成逐层 INDEX 分解（父节点=文件夹，子节点清单=INDEX.md），无限预算。
- 跑出来 1930 节点 / 10 轮 / 有效维度仅 6-8 → 成璐质询后定性：**Goodhart 刷分**——
  S_α 只奖规模不罚冗余，模型学会堆同义节点刷分。修法 = 冗余惩罚 + 边际信息增益停止。
  （commit d5bb7d06，`research/v17-hier-decomposition-blowup.md`）

### Phase 5 · T53 目标函数驱动状态机（11-09~11，当前）
- T53 = v17 的下一版（同一改进路线，非换名重启）。
- s5_state_machine.py：{IDLE, DECOMPOSE, VERIFY, REWORK, STOP}，J_necessary/J_verify/J_stop 机器裁决。
- 停止判据从 n-gram gain 改为 necessary pass_rate < 30% × 2 轮（中文 n-gram 不可靠）。
- smoke v5：**75 nodes / 2 rounds / natural stop / 0 leaks**（vs v17 的 1930/10/crash）。
- 下一步：开源 deepresearch 框架 baseline（criteria v2）+ 5 题泛化 bench。

## 2. 旁支（与主线正交，各自收口）

| 任务 | 内容 | 状态 |
|------|------|------|
| T-PR-13 | persona 激活调研（paradigm-routing 仓） | RESOLVED：双重稀释假说 |
| T-PR-14 | reasoning-as-search 调研 | arena 在跑 |
| T-PR-15 | 文字目标函数 Goodhart 雪球调研 | COMPLETED（回执已落盘） |
| T52 | 生产加固计划 | done（见 goal-pfb-hardening-v2.md） |
| T53C | bench 派发 + SOTA 调研 | 部分完成，SOTA 框架 TBD |
| 自判噪声实验 | H1/H2/H3 对照设计 | 设计完未跑 |

## 3. runs-* 目录 → 版本映射（stage-ablation/ 下 30+ 目录）

| 目录 | 对应版本/事件 |
|------|--------------|
| runs-s5-smoke | 早期 S5 管线冒烟（含 -v2 后缀 = 第二轮重跑） |
| runs-s5-gpu-v3 … v12 | Phase 2 规则堆叠期各版 gpu 单域 run |
| runs-s5-nat-v14 / runs-s5-soc-v14 | v14 量产（nat 101 reps） |
| runs-s5-gpu-v13 / runs-s5-nat-v13 / runs-s5-soc-v13 | v13 50-rep 稳定性 |
| runs-s5-prod | 早期 prod 数据（S0-gpu r1-r10 等） |
| runs-s5-v16.3-smoke / runs-s5-v17-hier-smoke | v16.3 / v17 冒烟 |
| runs-s5-sm-gpu(-r3/-r4) | T53 状态机 smoke（sm = state-machine, gpu 域） |
| runs-t53 / runs-t53b | T53 早期 run（t53b = b 批次） |
| runs-s8b / runs-s8b-a3 / runs-s8b-a4 | S8B 四臂（a3/a4 = A3/A4 臂复测） |
| runs-d1-c1 / runs-d1-c1-scored / runs-d1score | D1 题 C1 臂 + 打分（d1score = 重复目录，待清） |
| runs-r293 | r293 = 当时主仓迭代轮号快照（S5 n=3/题 scores-final） |
| runs-baseline / runs-prod / runs-prod-s3 / runs-prod-temp0 | S0 baseline / prod 各配置 |

## 4. "r" 的两个命名空间（易混点）

1. **run 内 rep/round**：`{ARM}-{Qn}-r{k}.json` 的 k = 第 k 个独立运行副本（rep）或管线内部第 k 轮
   （v17 层级分解的 r1-r10 = 逐层展开轮次）。scorer 硬编码此格式，**不改**。
2. **工程迭代轮**：`sm-modification-log.md` 的 r1-r6 = 跨 run 的代码修改批次。
   历史遗留：runs-r293 的 293 = 主仓全局迭代轮号（ralph-loop 时代），仅此一处。

## 5. 编号纪律（今后新增东西按这个来）

- 新实验臂 → 下一个 S 编号（S9 起），在 s8-report.md 同级加一行定义。
- S5 线代码大改 → 跟任务 ID 走（T53、T54…），不再发明 vN；需要版本锚点时在
  sm-modification-log.md 加一行 "vN = rX+rY merged release"。
- 新 run 目录 → `runs-{arm}-{domain}-{version}/`，version 用任务 ID 或版本号，禁止无后缀裸目录。
- 新任务 → tasks/ 全局递增 T 编号；stage-ablation/tasks/ 内的 T54+ 并入主序列前先查重。