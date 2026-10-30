# 阶段 04：执行与验证日志 — RV3B1-jaccard-adjudicate（材料准备）

> 分支 ralph/rv3b1-jaccard-adjudicate-materials · 2026-10-30 · 依据 03 行动表
> goal 性质：runner 只备料不代裁——本 goal 交付决策材料，裁定本身是成璐的人工动作

## §1 · 行动执行记录

| # | 行动 | 实跑结果 | evidence |
|---|------|----------|----------|
| A1 | finding #20 原文溯源落盘 | ✅ `bench/rubric-v3/jaccard-m5-adjudication-materials.md` §1：ISSUE + FIX 全文 byte-exact 引用（含四条判据 (a)-(d) 与低先验操作化定义）；源 = `receipts/adversarial-check-rubric-v3.json` → `responses[0].findings[19]`（Q4, severity=major，即 AUDIT 编号 #20「维度自选退化」） | 材料 §1 + 本日志 §2 机判 |
| A2 | 双口径语义分析落盘 | ✅ 材料 §2：#20 fix (c) 原文语义唯一 = 跨维度去重（档位区分度读法）；「run 间稳定性」读法无 #20 原文支撑——引入路径三层溯源表（#20 原文 → AUDIT L77 压缩转述丢限定语 → DRAFT v2 L38 双口径兜底） | 材料 §2 |
| A3 | 三选项对照表落盘 | ✅ 材料 §3：A 仅档位区分度 / B 仅 run 间稳定性 / C 维持双口径，六维对照（本意还原度 / 可机判性 / 防刷分覆盖 / 误伤风险 / pilot 影响 / diff 面） | 材料 §3 |
| A4 | 推荐与理由落盘 | ✅ 材料 §4：推荐 A（本意还原 > pilot 可行 > 误伤控制），附折中出口（run 间稳定性降为 SIGNAL 诊断信号，需另行预注册）+ 三处裁定权声明 | 材料 §4/§6 |
| A5 | 裁定后执行清单落盘 | ✅ 材料 §5：A/B/C/折中四分支改写模板（DRAFT v2 L38 + L311 + revision-log M5，diff 面 ≈3 行），供成璐勾选后 runner 执行 | 材料 §5 |
| A6 | 04.5 反方复核 | ✅ `loop-artifacts/stages/04.5/RV3B1jaccard-review.md`：7 攻击（1 部分成立已修复 / 6 驳回），总体 PASS | 04.5 工件判定表 |
| A7 | queue 状态更新 | ⏳ 收口时执行（L41 条目改「材料已备，待成璐裁定」——**不划掉**，验收标准第 6 条） | — |

## §2 · 机判输出（原样摘录）

**byte-exact 验证**（python 直接比对材料引用块 ↔ receipt JSON 字符串，剥离 markdown blockquote 前缀与说明括注后逐字符相等）：

```python
import json, re
d = json.load(open("receipts/adversarial-check-rubric-v3.json"))
f = d["responses"][0]["findings"][19]
mat = open("bench/rubric-v3/jaccard-m5-adjudication-materials.md").read()
def extract(anchor, stop):
    seg = mat.split(anchor)[1].split(stop)[0]
    lines = [l[2:].strip() if l.startswith("> ") else (l[1:].strip() if l.startswith(">") else l.strip()) for l in seg.splitlines()]
    return "\n".join(l for l in lines if l).strip()
fix_q   = re.sub(r'^（[^）]*）：\s*', '', extract("**FIX 原文**", "\n## "))
issue_q = re.sub(r'^（[^）]*）：\s*', '', extract("**ISSUE 原文**", "\n\n**FIX 原文**"))
print(issue_q == f["issue"])   # True
print(fix_q   == f["fix"])     # True
```

两项均 True。注：ISSUE 引用块首字符 `「` 因 markdown blockquote 渲染省略（材料 §1 已显式声明此偏差并给出补回规则），剥离说明括注后的正文与 JSON 逐字一致。

**冻结面检查**：

```
$ git status --short
 M tasks/current-goal.md                                    （覆写为本 goal 五字段格式）
?? bench/rubric-v3/jaccard-m5-adjudication-materials.md     （新建，本 goal 交付物）
?? loop-artifacts/stages/04.5/RV3B1jaccard-review.md        （新建，04.5 工件）
```

receipts/adversarial-check-rubric-v3.json / AUDIT-report.md / DRAFT-rubric-v3-v2.md / revision-log-batch1.md / 全部冻结 JSON **零触碰**。

## §3 · 诚实声明（负结果与不确定性）

1. **web-llm 未实际执行**（登录态失效，非工具故障）：本轮唤醒实测 `ralph prompt-first web-llm` 可正常启动（RV3B1-webllm-tool-fix r126/r127 修复生效），但三 provider（perplexity/chatgpt/gemini）playwright 登录态全部 error（prompt box unavailable，需人工一次性 `ralph web-llm-login`）。本 goal 证据链仓库内闭合（byte-exact 比对 + 三层文本溯源），外部在线复核边际贡献 ≈ 0，记 **unverified（登录失效）**，不阻塞。运行产生的共享回执覆写已还原（git checkout），per-goal 约定沿用。
2. **「作者本意」的指涉对象**：材料 §2 裁定的是 #20 finding 作者（arena adversarial-check judge）的意图，载体 = receipt 原文。AUDIT-report 是转述层，转述失真时以原文为准（U3 口径裁定同款逻辑，04.5 攻击 1 已复核该路径合法）。
3. **推荐 ≠ 裁定**：材料 §4 的单点推荐（A）附三条理由与折中出口，裁定效力来源是成璐确认——该判据约束未来所有 pilot run 的 O1 计分，属实验协议层决定（04.5 攻击 2/6 已复核）。

## §4 · 验收标准对照（current-goal【验收标准】）

- [x] finding #20 原文 byte-exact 引用（issue + fix 全文，含四条判据 (a)-(d) 与低先验操作化定义）→ §2 机判两项 True
- [x] 关键发现落盘：#20 fix (c) 原文语义 = 跨维度去重；「run 间稳定性」无 #20 原文支撑（系 AUDIT L77 压缩转述引入的二义性）→ 材料 §2
- [x] 三选项对照表（A/B/C：语义 / 可机判性 / 防刷分覆盖 / 对 pilot 的影响 / 风险）→ 材料 §3（六维）
- [x] 推荐与理由落盘（单点推荐 A + 权重排序 + 折中出口 + 裁定权声明）→ 材料 §4/§6
- [x] 裁定后执行清单（A/B/C/折中四分支模板，精确到行号与 diff 面）→ 材料 §5
- [ ] queue 条目状态更新为「材料已备，待成璐裁定」（不划掉）→ 收口 commit 执行（A7）

## §5 · 04 判定

pass——五项内容验收标准全部满足 + 冻结面零触碰 + byte-exact 机判实证；queue 状态更新随收口 commit 落地。goal 终态 = **材料已备，待成璐裁定**（不划掉、不 merge 销账，等人工裁定后按 §5 清单执行 ~3 行 diff 再收口）。