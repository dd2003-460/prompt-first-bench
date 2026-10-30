# 阶段 03 — RV3G3cdx-queue-format-contract · 动作分解（r151）

> 输入：stages/02.5 终局裁定（X1-X6）。执行顺序 A1→A5，每步可独立验证。

| # | 动作 | 对象 | 验证方式 |
|---|---|---|---|
| A1 | 契约文本落盘 `tasks/queue-format-contract.md`：八条款 C1-C8（X2 表）+ 证据索引（02 S6 表）+ §升级路径（R1/R2 规格 + R3 观察项）+ 存量状态节（15 简写行 / 4 标记变体 = 备料不改写）+ 矛盾登记节（C5 变体漂移按多数派+最新轮次裁定） | tasks/queue-format-contract.md（新建） | 人工对照 02.5 X2 逐条；每条规则带 file:line 或先例 commit 证据 |
| A2 | queue L3 加一行契约指针（blockquote，非 goal 行） | tasks/goal-queue.md L3 后 | assert-queue-lint 实跑仍 48 行 / 0 FAIL / 3 SIGNAL exit 0（指针行不被解析为 goal 行——行数不变即证） |
| A3 | (b) 备料清单落盘 `loop-artifacts/stages/04/RV3G3cdx-qfmt-stock-inventory.md`：15 简写行 + 4 标记变体逐行表（行号 + 形态摘录 + 改写预览），吸收登记行 4 处单独标高风险 | stages/04/ 新文件 | 行数与 02 S2/S3 实数对账（15+4，交集空）；双正则+awk 三角验证（X6） |
| A4 | 回归取证：assert-queue-lint 实跑 + 八脚本基线 + 冻结面 diff | 仓库根 | 48 行 / 0 FAIL / 3 SIGNAL exit 0；[0,0,0,1,0,0,0,0]；git diff main -- 三冻结件 = 0 行 |
| A5 | 收口 | queue + branch | 本 goal 行 `[ ]`→`[x]` + 元数据 + `**结果**：` 注记（按 C5 标准形态书写——本行即契约首秀）+ 追加候选 ≥1【(b) 存量改写执行候选，措辞含成璐裁定范围】；merge main |

**改动面白名单**：{tasks/queue-format-contract.md（新建）, tasks/goal-queue.md（L3 指针 + 收口行翻转 + 候选追加）, loop-artifacts/stages/{02,02.5,03,04,04.5}/*, current-goal.md}。
**禁区复核**：assert-queue-lint.py **零改动**（current-goal (c) 字面：本轮只写规格）；其余七脚本零触碰；冻结数据零修改。

## 预期风险与预案

- A2 指针行若误用 `- [ ]` 前缀会被 lint 当 goal 行 ⇒ 用 `>` blockquote 前缀（与 L3 既有格式说明行同族），实跑行数 48 不变即证安全。
- A3 改写预览涉及 4 个吸收登记行（L50-L53）：预览只做「五段式化」展示，不触碰「吸收」声明字样位置——若预览会移动声明位置则该行只列现状不列预览（防备料清单本身误导未来执行轮）。
- A5 本 goal 收口行自身须满足 C3/C5/C8（五段式 + 标准结果标记 + 元数据）——契约落盘轮的首个受检实例，04.5 攻击面必查此项（自指一致性）。