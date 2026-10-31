# origin: ai — C3 v3 对抗核验回执落盘 + 处置表（r59 · 2026-10-31）

## 背景
arena 会话（origin/arena/78602cd5-prompt-first-bench tip 5a525c7）对 tasks/T8-C3-v3-adversarial-check.md 的 6 个质询方向出了核验回执 `receipts/c3-v3-adversarial-check.json`（142 行），总判定 **PASS-with-fixes**：无根本缺陷，但确认性开跑前有 3 条 blocking fixes。该 commit 在 arena 分支上、未进 main；本回执内容此前从未被消费——R4 主分析收口（r47）与 rubric v11（r44-r46）都是在它之前完成的，本轮首次对齐。

## 落盘动作
1. 从 5a525c7 检出回执到 `receipts/c3-v3-adversarial-check.json`（byte-exact，sha256 对账）。
2. 新增处置表 `loop-artifacts/stages/04.5/C3v3-adversarial-disposition.md`：逐条对照 R4 已执行事实 + r54 G1a backfill，给出「已覆盖 / 部分覆盖 / 未覆盖」三态判定。

## 六漏洞处置摘要
| id | 判定(arena) | 严重度 | 现状 |
|---|---|---|---|
| R1 三道地板 | 部分成立 | 中 | 已覆盖大半——C1 本次不跑、排序表述已降级为探索性；n=4 Spearman 仅作诊断。残余：不得声称「R1 已校正 top-k」（现有文档均未做此宣称，零改动） |
| R4 功效/estimand | 成立 | 高 | **部分覆盖**——F-sham 排除出 factorial 拟合 ✓（r47 结论只报 cell 均值对比）；4 角点 estimand 误称风险 ✓（r47 明确「描述层不做推断」）；**未覆盖**：任务块聚类模型/MDE 反推题数从未预注册 → R4 结果只能定位「探索性/方向性」（r47 已按此口径声明，等效达成但缺书面预注册件） |
| R5 judge 校准 | 成立 | 高 | **部分覆盖**——κ 单位/量尺问题已由 G1a 二值化方案解决（M8-truth 按条目 pass/fail 切分，非 run 分数切 0.5）✓；CALM 阈值有实测记录 ✓；**未覆盖**：异源 judge 身份冻结 = G1b blocked-on-human（queue L25 既有登记，非新缺口） |
| M8-truth/cover 机会集 | 成立 | 高 | **未覆盖（真缺口）**——「核验机会集由谁定义、何时冻结、空分母处理、新旧 M8 口径版本化」四子项无一落盘成文。R4 实际用的分母 = 各 run 自身产出的条目数（即修正 4 想消灭的可变分母！）→ 这是 R4 结论的一个未声明局限：B-noevidence 类配置若减少条目产出，truth 率天然被抬高。**需补：机会集冻结协议 + R4 结论加限定语** |
| selection_validation_isolation | 部分成立 | 中 | 已覆盖——两域限定声明存在（r47「结论上限=同族方向性证据」+ hold-out 域缺失已登记）；第三域外推无人宣称 |
| C2 compensation proxy | 低 | 低 | 已覆盖——C2 保持描述性定位，编码文档在 runs-r4 receipt |

## 关键发现（本轮新认知）
**R4 的分母问题比 arena 指出的更实**：arena 说「机会集完整性须在 G1 前解决」，而 R4 已经跑完且用了 per-run 可变分母——这意味着 B-noevidence 0.954 > A-full 0.781 这个「删组件反而更高」的结果，有一部分可能来自分母收缩而非真实质量提升。r47 结论里 evidence「对 M8 判分无正向贡献」的表述需要加限定：**在未固定机会集的前提下，该比较混淆了条目产出量与条目质量**。freeze 负效应（B-nofreeze -0.35）受影响较小（freeze 删除主要影响行为而非条目数量，待机会集协议落地后复算确认）。

## 导出候选
- `T8-C3-v3-opportunity-set-freeze`：机会集冻结协议设计（定义主体=Lead 盲法前置 / 冻结时点=run 启动前 / 空分母规则 / 新旧 M8 口径版本化）+ 对 R4 36 run 的事后机会集重建可行性评估（从 run 输入题面机械提取应核验清单，标 unverified 边界）+ R4 结论限定语回填。**纯仓库内可执行，~5 回合**。