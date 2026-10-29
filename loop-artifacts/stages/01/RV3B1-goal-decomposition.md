# 阶段 01：目标分解 — RV3G6-draft-revision-batch1

> goal: rubric-v3 DRAFT 修订第一批 · 分支 ralph/rv3g6-batch1 · 2026-10-30
> 上游：`bench/rubric-v3/AUDIT-report.md` §9.1（R-01~R-15 清单）+ §9.3（batch1 = R-01~R-03 + R-06 + R-10，开跑前置条件）

## 1. 目标 → 因素分解

总目标 = 「让 rubric-v3 新版 DRAFT 满足正式实验开跑的前置条件」。拆成三个正交因素：

### F1 文本一致性（消除自相矛盾与答案注射）— AUDIT-report §9.1 第一批核心
| 子因素 | 内容 | 来源处置 |
|--------|------|----------|
| F1a O1 维度重写 | 拆账（覆盖行为 only）+ 二值条目计分 + 防刷分机械判据 | B1, B7, #20, #21 → R-01 |
| F1b 全维尺度统一 | yes/no 条目化 + 条目通过率 + κ 条目层 + 权重预注册写死 | B6, #26 → R-02 |
| F1c §4 题面去方向暗示 | 删「≥5 年」锚点 → 非默认可行区间；三问域无关占位；V1-align 对照组；Pr2/Pr3 判据替换 | B3, B11 → R-03 |
| F1d O3 宣称前置条件 | §6 S2 限定语原文写入 §1-O3 | B2 声明路径 → R-06 |
| F1e 变体矩阵冻结 | 同题面 + V2 精确 diff + V3 sham + V-sham + 每处差异标注 | B10, #27 → R-10 |

### F2 机判防护（纸面协议 → 可执行断言）— G5 C3/C4 导出
| 子因素 | 内容 |
|--------|------|
| F2a C4 w2 公式断言 | 双 judge 逐节点复算 w2 = 1 + min(−log₂p̃, log₂(1/ε))，p̃=null→1.0 |
| F2b C3 W3W4 复算断言 | hit-matrix + prior-estimates → W0-W4 × 8 run 分数 vs stats-w3w4.json |

### F3 交付物完整性（研究级质量线）
| 子因素 | 内容 |
|--------|------|
| F3a 六阶段工件 | stages/<N>/RV3B1-* 齐全，04.5 反方复核必做 |
| F3b revision-log | 每条修订带 AUDIT-report 出处 + 前后对照 |
| F3c 冻结数据零修改 | git status 验证 |
| F3d queue 更新 | 划掉 + 结果注记 + ≥1 新候选 |

## 2. 条件三分

**人类已提供**：
- batch1 范围 = R-01~R-03 + R-06 + R-10（queue 条目 + AUDIT-report §9.1 末段批次划分）
- 五项修订的具体方向（AUDIT-report §2 维度表 + §7 处置表已锁定，本 goal 不重新裁定方向）
- 分支名 `ralph/rv3g6-batch1`、commit+push+merge 流程（runner 协议）

**项目可推导**：
- R-06 限定语原文 = AUDIT-report §6 引用块逐字（验收标准 4 要求逐字一致）
- C4/C3 断言的输入文件与容差 = 冻结 JSON 结构（已勘察：prior-estimates.nodes[].{p_tilde,w2}，stats-w3w4.scores.{W0..W4}.{run1..8}，4 位小数舍入 → 容差 5e-5）
- 变体冻结表的 commit hash = 本 goal 收口 commit（冻结件随收口 commit 生效）
- assert 脚本模式 = `ablation/scripts/assert-g1-audit.py`（exit 0/1 语义 + SIGNAL 行不影响 exit code）

**仍需研究（空缺清单）**：
- Q1 V1-align 对照组的「只加结构规则不含价值判断」具体措辞 —— 需设计：保留四分区强制搜索的结构骨架，去掉 c 区准入条件中的价值判断词（保值性/性价比阈值）与三问中的方向性提示。设计原则在 02 定稿，无外部依赖。
- Q2 V3 sham 替换段的「等长中性」文本 —— 需构造与边界类型声明段落等长的中性过程指令（如通用记录规范），02 定稿。
- Q3 新版 DRAFT 文件名与版本标记约定 —— 仓库内无既有 v2 先例；取 `DRAFT-rubric-v3-v2.md` 并在文头标 v2 状态（草案·batch1 修订落地·待第二批+arena 核验后定稿）。原版 `DRAFT-rubric-v3.md` 保留不动（它是审计对象的历史快照）。
- Q4 O1 四条机械防刷分判据中「候选集 Jaccard<0.9」的计算基准 —— 两 run 候选集交集/并集？还是单 run 候选集 vs 某参照？AUDIT-report 未展开定义。降级处理：在 DRAFT 中按「相邻两档候选集 Jaccard < 0.9（同题不同档位产出的候选集合不得几乎相同）」落笔，并在 revision-log 登记此解释为**本 goal 的解释性补充**（非 AUDIT-report 原文），供人工裁决。
- Q5 条目通过率下 O2/O3/O4/P1-P4 各维的条目拆分 —— AUDIT-report §2 给了方向（O2 层级必要条件 / O4 结构正确性拆项 / P1P3 代理量）但 batch1 不含 R-07/R-08/R-12/R-13/R-14。边界裁定：**batch1 只做 R-02 要求的横切机制改写**（每维给出 yes/no 条目框架 + 条目通过率计分 + κ 条目层声明），条目内容沿用现 DRAFT 判据的二值化直译；深度重设计（R-07~R-14）留 batch2 并在 DRAFT 对应位置标 `[batch2: R-xx]` 占位。这是防止 batch1 越界实施 batch2 内容的必要切割。

## 3. 递归分解判定

- F1a-F1e：叶子 = 每个修订点在 DRAFT 中的落点段落，原子（改哪段、改成什么由 AUDIT-report 锁定）。
- F2a/F2b：叶子 = 脚本断言组（A1 结构完整性 / A2 逐节点复算 / A3 汇总计数），原子。
- F3a-F3d：叶子 = 工件文件存在性 + 运行 exit code，原子。

**分解完成判定**：全部叶子原子；Q1-Q5 五个无法假定条件已入空缺清单且均有 02 研究入口（Q1/Q2 纯文本设计、Q3-Q5 仓库内裁定）；阶段 02 可直接开始。

## verdict

**pass** — 因素分解覆盖 batch1 全部七项工作（五修订 + 两断言 + 交付完整性），五个空缺条件均已登记且有研究路径，无伪装已知。进入阶段 02。