# 03 — RV3G6-o3-claim-rejudge-evidence-audit · 行动分解

> goal: hit-matrix 98 个 h=1 evidence verbatim 合规审计 · 分支 ralph/rv3g6-o3-claim-rejudge-evidence-audit · 2026-10-30

## 行动表

| # | 行动 | 输入 | 输出 | 依赖 | 验证方式 |
|---|------|------|------|------|----------|
| A1 | assert-hitmatrix-evidence.py 落盘：docstring 预注册 C1-C5 判定语义（与 01 阶段表 byte-stable）+ 逐格审计 + V1 口径 gold-token 计数 + §3.2 mismatch 注记；路径解析用 `Path(__file__).resolve().parents[4]`（任意 cwd 可跑，不继承既有三脚本的 repo-root-only 限制） | hit-matrix.json + runs-C0-run1..8.md（只读）+ assert-o3-claim-list.py 的 `gold_numbers_per_node`/`_noise_exempt` 逻辑（同源引用） | `scripts/assert-hitmatrix-evidence.py` | — | docstring 判定表与 01 阶段 2 节逐行一致；实跑 exit code ∈ {0,1} |
| A2 | 实跑（live data）：产出 98 行 h=1 逐格审计表 + h=0 扫描计数 + V1 计数 vs 声明值 27 对照 + 汇总 verdict | A1 | 04 日志记录完整 stdout | A1 | exit code 与 F2 预判一致性核对（预判 PASS exit 0——若 FAIL 则为负面结果，如实落盘并触发失败降级条款 2） |
| A3 | 变异测试 ≥3 场景（临时 fixture JSON 写入 /tmp，测毕即删，不落仓库）：M1 篡改 evidence（改写一个词）→ C2 FAIL exit 1；M2 跨 run 张冠李戴（run1 cell 的 evidence 换成 run2 独有句）→ C4 FAIL exit 1；M3 超长 evidence（>40 字符且为合法子串）→ C3 SIGNAL、exit 仍 0；M4（加做）h=0 cell 塞 evidence → C5 SIGNAL exit 0 | A1 + hit-matrix 副本 | 04 日志各场景实测输出 | A1 | 各场景 exit code + stdout 关键行核对（FAIL 行含 (run, node) 定位；SIGNAL 行带 `[SIGNAL]` 前缀） |
| A4 | §3.2 声明 4「27/98」复算记录固化：V1/V2/V3 三口径计数 + 差异来源目视抽样（≥3 例具体 cell）落盘 04 日志 | o3-claim-list §3.2 + gold-tree.md + hit-matrix.json | 04 日志 F3 复核节 | A1 | 三口径数字与 02 阶段 F3 一致（脚本内 V1 实现与 assert-o3-claim-list.py 同函数逻辑，独立重算交叉验证） |
| A5 | 冻结面零修改验证 + 既有断言回归（assert-o3-claim-list.py / assert-goldrank-threshold.py / assert-gmr-recompute.py / assert-o3-claim-rejudge.py 重跑基线维持） | git status + 四脚本 | 04 日志记录 | A1-A4 | git status 冻结文件零 diff；回归脚本 exit code 与计数同 r141 基线 |
| A6 | queue 更新 + 候选导出：追加本 goal 完成条目；导出勘误候选（o3-claim-list §3.2 声明 4「27」不可复现 → V1=13，冻结件修改需 APPROVALS 登记）；视实跑结果决定是否导出修复候选 | goal-queue.md | queue diff | A1-A5 | queue 条目格式合规（五要素）；勘误候选注明「不代裁、备料模式」 |

## 预注册规则（04.5 攻击面预先声明）

1. **零 h 值红线**：本 goal 只判文本出处合规性（evidence 是否 verbatim 出自所属 run），不对任何 (run, node) 的命中语义下结论。审计表中的 PASS/FAIL 仅指 evidence 字段的形式合规。
2. **冻结件零修改**：hit-matrix.json / o3-claim-list.md / gold-tree.md / runs-C0-* 一律只读；发现违规或数字失实 → 只暴露事实 + APPROVALS 登记 + 导出候选，不在本 goal 动冻结面。
3. **fixture 不留痕**：变异测试用 /tmp 临时 JSON，测毕删除；git status 验证 scripts/ 目录最终只新增 assert-hitmatrix-evidence.py 一件。
4. **C4 触发条件锁定**（X2）：C4 仅在 C2 FAIL 时作为子类诊断报出，不做全局唯一性检查——防 11 组合法重复字符串误报。此逻辑在 docstring 显式写出。
5. **exit code 约定不变**：0 = 无 FAIL（含 SIGNAL）/ 1 = 存在 FAIL。无 exit 2 分支（本脚本消费的是冻结数据而非外部投递 schema，schema 违例归为 FAIL 处理——若 hit-matrix.json 本身结构损坏则 fail-loud 报错退出，不静默）。