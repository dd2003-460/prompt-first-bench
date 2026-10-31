# G1b 异源 judge 盲评任务书（C3 v3 · R5 门禁最后一块）

**状态**: ready（2026-10-31 keepalive 轮 · arena agent mode 派发）
**执行通道**: arena.ai/agent，连接仓库 `dd2003-460/prompt-first-bench`，分支 `ralph/g1b-hetero-judge-dispatch`
**目的**: 用**非 Qwen 家族**的模型对 C3 v3 校准集做独立盲评，完成「家族隔离」校验——裁决器不能和被测生成模型同源（被测 = qwen3.8-27b），否则裁判偏爱自家写法的偏差无法排除。

## 背景（≤10 行）

我们在做 prompt 组件消融实验：删掉 prompt 里的某个段（如"候选集冻结声明"），看最终核验质量指标 M8（核验真实性率）是否下降。M8 由 AI 裁决器打分，所以裁决器本身必须先过校准。G1a 已用同族模型（qwen3.8-27b）做完内部一致性校准（回执 `receipts/c3v3-g1a-judge-calibration.json`，verdict PARTIAL-PASS：严格版 J1 能识别植入退化、对措辞扰动稳定）。但同族校准证明不了「换一家模型的裁判结论一致」——这就是 G1b：让一个**你（arena 会话默认模型）**重打同一批工件，和 qwen3.8-27b 的判分对比。

## 你要做的事（严格按序）

### Step 1 · 读材料
1. `git clone -b ralph/g1b-hetero-judge-dispatch https://github.com/dd2003-460/prompt-first-bench.git`（或切换当前工作区到该分支）
2. 读评分协议（三测定义 + 判定规则 + 输出格式）：`experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts.json` 里 `prompts["J1-strict"]["text"]` 字段——**逐字照用，不要改写、不要加戏**
3. 读 5 份待评工件（盲法样本，你不知道它们来自哪个 prompt 配置，也不要去猜）：
   - `experiments/T8-matrix/runs/c3-v3/calibration/blind-A1.md`
   - `experiments/T8-matrix/runs/c3-v3/calibration/blind-A2.md`
   - `experiments/T8-matrix/runs/c3-v3/calibration/blind-B1.md`
   - `experiments/T8-matrix/runs/c3-v3/calibration/blind-B2.md`
   - `experiments/T8-matrix/runs/c3-v3/calibration/blind-P1.md`

### Step 2 · 逐份盲评
对每份工件，按 J1-strict 协议逐条审计其核验主张（X1..Xn / A1..An / U1..Un 等原始编号），产出严格 JSON：
```json
{"items":[{"id":"X1","verdict":"pass|fail","note":"≤30字"}],"summary":{"total":N,"passed":M}}
```
注意 P1 是一份**被刻意做过手脚**的工件（某条处置标记与证据不符）——协议要求发现即 fail 并在 note 点名。**不要试图反推哪条是植入的**，就按三测正常审；如果你恰好靠协议抓到了它，那是评分器敏感度的证据，不是作弊。

### Step 3 · 落盘（硬约束：文件不存在 = 任务未完成）
把 5 份结果写成 **一个** JSON 文件：
`experiments/T8-matrix/runs/c3-v3/calibration/g1b/hetero-judge-results.json`
结构：
```json
{
  "kind": "c3v3-g1b-hetero-judge",
  "judge_model": "<你实际用的模型全名，必须如实写>",
  "family_check": "<该模型是否属于 Qwen 家族：yes/no/unknown，一句话依据>",
  "date": "<YYYY-MM-DD>",
  "protocol_sha256_16": "15086eb4166b1884",
  "results": {
    "blind-A1": {"items": [...], "summary": {...}},
    "blind-A2": {"items": [...], "summary": {...}},
    "blind-B1": {"items": [...], "summary": {...}},
    "blind-B2": {"items": [...], "summary": {...}},
    "blind-P1": {"items": [...], "summary": {...}}
  }
}
```

### Step 4 · commit + push
```
git add experiments/T8-matrix/runs/c3-v3/calibration/g1b/hetero-judge-results.json
git commit -m "g1b: hetero-judge blind scoring (5 calibration docs, J1-strict protocol)"
git push origin ralph/g1b-hetero-judge-dispatch
```
push 成功后在会话里回一句「DONE + commit hash」。

## 红线
- 只新增 `g1b/hetero-judge-results.json` 这一个文件，其他任何文件零改动（冻结面：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / DRAFT-rubric-v3*.md）
- 不改 judge-prompts.json 的协议文本；不改 blind-*.md 工件
- 若你的模型自报为 Qwen 家族 → 仍然照常打分落盘，但在 `family_check` 里如实标 yes，Lead 侧会降级处理（不浪费这次跑分）
- 中文 note，每条 ≤30 字

## 验收（Lead 侧）
- 5 份 summary.total 与工件条目数一致
- blind-P1 的 X5 应 fail（阳性对照）；若 pass → 记录为异源 judge 敏感度不足，同样是有效数据
- 与 G1a 的 qwen 判分算条目级 κ（G1a 结果在 `receipts/c3v3-g1a-judge-calibration.json` 的 runs 字段）
- κ ≥ 0.6 → R5 家族隔离项关闭，C3 v3 主分析可出「judge 校准全过」口径；< 0.6 → 分歧条目进人工仲裁队列