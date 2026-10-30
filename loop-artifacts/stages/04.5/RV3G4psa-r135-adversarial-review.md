# 阶段 04.5 反方复核 — RV3G4-prior-source-assert（r135 核销轮 · 2026-10-30）

> 命名说明：本 goal 与 r130 同名（queue 候选名 = 交付物名）。r130 已落盘 `RV3G4psa-adversarial-review.md`（7 攻击，verdict pass），本文件为 **r135 核销轮的独立复核**，不覆盖 r130 工件。两文件并存 = 两轮审计链完整可追溯。

> verdict: **pass**（8 项攻击：4 败 / 3 部分成立已处置 / 1 成立已处置）

## 前置事实（范围发现复核）

r130 已交付：assert-prior-source.py（8/8 PASS exit 0）+ prior-estimates.json:p_tilde_provenance 双源登记 + r130 自己的 04.5（含 M1-M4 变异声明）。本 goal（r135）的增量定位 = **独立复验防失效能力 + 措辞瑕疵修复 + 队列原文四项核销表**——不是重做 r130。

## 攻击清单与裁定

| # | 攻击 | 裁定 |
|---|------|------|
| W1 | 「核销型 goal 产投比是否够格占一个 loop？会不会是凑数？」 | **部分成立，接受**。辩护：r130 commit message 声称 '变异测试 M1-M4'，但 r135 独立复跑三场景（M1 单源/M2 无块/M3 空列表）确认行为真实，且发现 r130 未覆盖的尾行措辞瑕疵（J4 修复）——核销产生了增量证据与增量修复，非盖章。若 r130 证据已完备，本 goal 应判 SKIP；实际不成立，pass 有效 |
| W2 | 「J4 措辞修复只 diff 了本次会话基线——r130 原始基线是否逐字核对过？」 | **败**。基线捕获于本分支任何改动前（main HEAD = 5fa2508，工作树 clean）；git log 实证该脚本自 0fedf42 后无其他改动 → 当前基线 ≡ r130 基线，逻辑闭合 |
| W3 | 「沙盒改 ROOT+PRIOR 两变量——若脚本有其他路径依赖，变异可能测的不是你以为的东西」 | **败**。BLINDTEST 派生自 ROOT（改绝对路径后仍指真实文件，M1/M3 不需要动它）；M2 删块后检查②走 sources=None 跳过分支，blindtest 顶层读取无条件执行——M2 实跑无 traceback，触发点与 04 表格一致 |
| W4 | 「N_MIN=2 + family-independent:false 下，用户看到 PASS 会不会以为独立性已保证？」 | **部分成立，残余风险登记**。header/docstring/provenance.note 三处限定语压低误读概率；彻底闭环需第三异族模型（外部依赖，R5.2-third-scorer 同阻塞源）。04 判定措辞与能力对齐（「让缺失可见」≠「证明独立」） |
| W5 | 「verdict 型 exit 1 阻断——未来加节点忘更新 provenance 就 CI 红，耦合太紧？」 | **败（方向正确）**。这正是 G4 S3 教训要的：登记义务机械化。检查③只数 judge_id 去重，正常加节点不改 source 计数，不误伤；会红的恰是「动了生成源却忘登记」的违规情形 |
| W6 | 「消费方 grep 只匹配完整片段——正则或截断匹配 "signal-only" 会漏」 | **部分成立，补测**。全仓 grep `signal-only`（不限定后缀）：命中仅本脚本 header 行（合法保留——结论边界声明）+ R5.2 系列脚本 docstring（独立语义，不消费本脚本尾行）。无动态消费方 |
| W7 | 「goal 标题暗示新建，实际是核销+一行修复——queue 注记不说清范围会误导下个 runner」 | **成立，已处置**。queue 更新注记明确写「核销型：交付物 r130 已存在，增量 = M1-M3 独立防失效实证 + 尾行措辞修复 + 四项核销表」 |
| W8 | 「provenance 改成非 dict（如 list）时检查②静默跳过，单源检测失效？」 | **败（fail-safe 方向正确）**。非 dict 先撞检查① isinstance 门 → FAIL exit 1，不存在静默放行路径。M2 实证的就是这条门 |

## 数字层独立重算

- assert-prior-source.py 基线：8/8 PASS exit 0 ✓（/tmp/ps-baseline.txt）
- 变异 M1（单源）：exit 1，FAIL 定位检查③ ✓
- 变异 M2（无 provenance）：exit 1，FAIL 定位检查①×2 ✓
- 变异 M3（空列表）：exit 1，FAIL 定位检查①+③ ✓
- J4 修复后：diff 面 = 1 行（尾行措辞），exit 0 维持，8/8 PASS 不变 ✓
- 冻结面：git status 仅 assert-prior-source.py 修改 + 新工件，prior-estimates.json 零触碰 ✓

## 与 r130 04.5 的关系

r130 04.5 A2 裁定「signal-only 标注四处显式声明，误读需同时无视四处」——r135 J4 修复后该裁定中「RESULT 行同样带标注」的载体从 "signal-only" 字样改为更精确的 "metadata gate — NOT a family-independence verdict"，A2 结论**加强**而非削弱（措辞歧义面缩小）。r130 04.5 无需修订。

## verdict

**pass**——无实质缺陷；W1/W4/W6 部分成立已处置（接受增量论证/残余风险登记/补测完成），W7 成立已处置（queue 注记明确核销范围）。

## 导出候选

- 无新增——W4 家族隔离属已知外部阻塞（R5.2-third-scorer 已覆盖），不重复立项。下一纯仓库内 goal = RV3G4-kappa-receipt-assert（已在队列）。