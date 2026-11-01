# RV3G1-semantic-rejudge — G1 语义级独立重判补数（arena 通道）

> 2026-11-01 · 分支 ralph/rv3g1-semantic-rejudge · Lead: Hermes keepalive (r158)
> 来源：G1-contradiction-audit.md §1「口径边界」——S1 只覆盖 h=1 方向，h=0 漏判方向标 unverified，补数路径 = arena 通道盲重判。

## 【目标】

对已落盘的 75 个样本 cell（`bench/rubric-v3/ablation/scripts/g1-sample-cells.json`，seed 20261030 确定性抽样，40×h=0 + 35×h=1）做 fresh-context 盲重判：judge 只看 run 原文 + 节点定义，独立给出 h∈{0,1}，与 hit-matrix.json 原标注比对，报**语义一致率**（重点覆盖 S1 未覆盖的 h=0 漏判方向）。

## 【阶段】

- 阶段 1（本轮已完成，仓库内）：输入材料冻结
  - `rejudge-g1b/node-defs.json` — 30 个不同节点的 gold-tree 定义抽取
  - `rejudge-g1b/judge-input.json` — 75 条 judge 输入（cell_id / run_file / run_sha256_16 / node / node_definition / prior_h）
  - **prior_h 仅供事后对照，judge prompt 中不得出现**（防锚定）
- 阶段 2（arena 通道）：派发盲重判 → 收 JSON 回执 → 落盘 `rejudge-g1b/`
- 阶段 3（仓库内）：一致性分析 + 回填 G1-contradiction-audit.md §1 + 回执 + queue 更新

## 【SOP 索引】

- `.claude/skills/arena-outsource/SKILL.md`（ego-browser 提交 arena agent mode，taskSpace `pfb-ralph-rv3g1-semantic-rejudge`）
- 降级阶梯：arena agent mode → arena Battle → ego-browser 直抓 → 本地自答（conf −0.2，标「arena 不可用 <日期> <原因>」）

## 【验收标准】

1. arena 产出 JSON：75 条 `{cell_id, h_judge, evidence_quote}`（evidence_quote = run 原文逐字片段或 "none"），落盘 `rejudge-g1b/rejudge-results.json`，sha256_16 记入回执
2. 一致性分析落盘 `rejudge-g1b/rejudge-analysis.json`：
   - 总一致率、h=1 子集一致率（复验 S1）、**h=0 子集一致率（本 goal 核心新增）**
   - 全部翻转清单（cell_id + 双方依据摘要）
   - κ（条目级二值）；若天花板效应（pe≥0.95）按 G1a/G1b 先例改报唯一翻转方向 + 敏感度判读
3. 回填 `G1-contradiction-audit.md` §1 口径边界段：unverified → 实跑数字
4. 回执 `rejudge-g1b/receipt-rv3g1-semantic-rejudge.md`（含 arena 会话/taskSpace 标识、降级记录、负结果声明）
5. 冻结件零触碰：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* 只读；七脚本回归全绿

## 【失败降级】

- arena 登录失效 → 按 SKILL.md 故障处置 SOP（先查工具和网络，别直接找用户扫码）
- arena 全程不可用 → 走降级阶梯末档本地自答：本会话盲重判（fresh context 约束 = 先写判定规则再逐条判，规则先行防锚定），conf −0.2 并在回执标注「arena 不可用」
- 单条 cell 原文超长（run_chars > 8000）→ 正常处理，不截断（8 run 全文均 < 3000 字符，无此风险）