# 阶段 03 — RV3G3cdx-crossdomain-lint-coverage-expand · 动作分解（r150）

> 输入：stages/02.5 终局判定语义。执行顺序 A1→A6，每步可独立验证。

| # | 动作 | 对象 | 验证方式 |
|---|---|---|---|
| A1 | load_batch2 加 (b) gold⊆nodes 键集检查（X1/X2：E6 后、per-node 循环前；缺省/显式统一） | assert-goldrank-crossdomain.py L218 后 | neg-gold-dangling-in-prior ⇒ exit 2 指名 N-9；pos-full/pos-no-blindtest 仍 exit 0 |
| A2 | load_batch2 加 prompt_version 存在性+非空 str 检查（X3：per-node 循环后） | 同上 | 构造缺失/空值临时样例 ⇒ exit 2 对应文案；既有 pos 样例含 "DRAFT-v2-frozen" 不受影响 |
| A3 | 主 docstring 更新（X6 lint 模式节 + X3/X4 schema 节 M1/M2 状态 + 检查链新序） | 同上 L1-60 | 人工对照 02.5 终局节逐条；byte-stable 面（w2_exact/build_schemes/(a)(b) 判定段）零 diff |
| A4 | 新增负样例 ×5 持久落盘（X5：neg-hitmatrix-missing / neg-unreadable-json / neg-nodes-not-dict / neg-gold-not-list / neg-gold-dangling-in-prior） | batch2-lint-samples/ | 9/9 FAIL 出口矩阵实跑全核对（exit 2 + 文案指名）；既有 5 neg + 2 pos 零漂移 |
| A5 | byte-exact 回归 + 基线 | 仓库根 | 无参调用 stdout+exit 与 /tmp/noarg.txt 基线逐字节一致；八脚本 [0,0,0,1,0,0,0,0]；冻结面 git diff = 0 |
| A6 | 收口 | queue + branch | L23 [ ]→[x] + 结果注记 + 新候选 ≥1（batch2-prompt-gold-map 登记表，X4 导出）；merge main |

**改动面白名单**：{assert-goldrank-crossdomain.py, batch2-lint-samples/neg-*×5, stages/{02,02.5,03,04,04.5}/*, current-goal.md, goal-queue.md}。
**禁区复核**：w2_exact / build_schemes / top10_gold_count / reachable_top10_gold_counts / brute_force / (a)(b) 判定段 / 无参主路径 stdout 三行 —— A1-A3 触碰前先 `git diff` 自检该区域零变化。

## 预期风险与预案

- A1 若误伤 pos-no-blindtest（其 prior 与 pos-full 同构，gold 全在 nodes 内）⇒ 不会，S2 已实证两 pos 的 gold⊆nodes 成立；实跑兜底。
- A2 文案「non-empty string」对含空白字符串（"  "）的处置 = strip 后判空 ⇒ FAIL（预注册于 docstring）。
- r147「5/8」勘误不在本 goal 改历史工件，仅收口注记说明（X5）。