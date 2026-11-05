# Evidence Packet 模板 v2（独立打分器输入证据包）

> origin: ai · 2026-10-30 · R5.2-evidence-packet goal 产物
> 依据：R5.1 定位的结构性分歧源（`r5/scorer-agreement-r1.json` systematic_pattern + `r4/independent-scoring-deepseek.json` key_reasons 自认缺字段）+ 02.5 矛盾 X2（摘要式 packet 错配教训）
> 适用范围：self-opt-tester bench 各 run 送独立 LLM 打分前的输入组装。**本模板是"发送前组装的输入包"schema，不是打分回执 schema**（回执格式见 r4/r5 已有 JSON，不动）。

## 设计原则（R5.1 教训固化）

1. **机械可测指标给原始值 + 来源路径，不给摘要**。原 packet 单行摘要既缺字段（M2/M5 全缺）又错配字段（X2："run3 任务书25行"实为 run2 的 25 行）——双重失败。
2. **每字段三件套**：值 + source_path + source_quote（原文摘录或命令输出）。缺任一件 = 不得入包。
   - **source_path 填写规范**（R5.2-sourcepath-hardening · W1 收口）：必须为 base 可解析的完整相对路径（`WS <workspace-relative>` / `pfb <repo-relative>` / git 对象 `commit <hash>:<path>` 形式）；**禁 `...` 缩写与裸 basename**——断言脚本已删 glob 兜底，缩写路径会直接 FAIL。多文件引用用 ` + ` 分隔，每个文件独立给出完整路径。
3. **缺口显式 null + reason**，禁止用"合理估计"填充。DeepSeek 对缺字段的反应是系统性扣 50 分（M2=50 ×2），说明"没给"会被读成"差"；null+reason 让打分器能区分"证据缺失"与"表现差"。
   - 两类 null 政策：**证据缺口型**（原始证据确无数值记录，grep 全目录无果）= 允许，必填 `reason`/`conf_note`；**未提取型**（懒得提取）= 禁止。
4. **降级/unverified 状态随字段走**（如 run2 arena 侧 token unverified、run3 无网络）——否则打分器自行脑补。
5. **观察时间戳必填**（measured_at / observed_at）——同一文件不同时点可能不同值。

## 必填字段（P1-P6）

### P1 任务书行数（M2 口径：≤200 行，wc -l 实测）

```json
{
  "file_path": "string|null",        // 任务书落盘路径；派发消息类任务书无落盘 → null
  "wc_l_output": "number|null",      // wc -l 一手输出；无落盘文件 → null
  "approx_lines": "string|null",     // 仅当 wc_l_output=null 时填执行者自估（须注明"自估"）
  "measured_at": "ISO8601|string",   // 测量/观察时刻
  "source_path": "string",           // 值的来源（git commit/blob 也算）
  "source_quote": "string"           // 命令输出原文或转录原文
}
```

规则：`wc_l_output` 与 `approx_lines` 二选一非空；两者皆空 = 违规（必须给 null+reason 解释为何连自估都没有）。

### P2 达 conf≥0.7 所需轮数（M5 口径：review.md conf 记录）

```json
{
  "rounds": "number",                // 轮数；推断/自述值必须配 rounds_basis
  "rounds_basis": "firsthand|inferred|self-reported",  // 计数性质
  "conf_at_completion": "number|null", // 终态 conf 数值；原始证据无记录 → null
  "conf_note": "string|null",         // conf_at_completion=null 时必填：达成替代证据是什么
  "source_quote": "string",
  "source_path": "string"
}
```

规则：`rounds_basis=inferred|self-reported` 时，source_quote 必须是承载该值的**原文句**（让打分器看到这是推断/自述而非精确计数）。

### P3 per-run token 切分（M1 口径）

```json
{
  "input_tokens": "number",
  "requests": "number",
  "window_utc": "string",
  "caveats": "string[]",             // 边界混入 / 侧向 unverified 等注记，逐条
  "source_path": "string",
  "source_quote": "string"
}
```

规则：任何"某侧 unverified"必须进 caveats（如 run2 arena 侧总量本地无账本）——防打分器把 Lead 侧切分误当全量。

### P4 断点 A/B/C 状态（M3 口径）

```json
{
  "A": {"status": "pass|degraded|n/a", "evidence": "string"},
  "B": {"status": "...", "evidence": "string"},
  "C": {"status": "...", "evidence": "string"},
  "degraded_notes": "string[]"       // 哪个断点因何降级（通道不可用→推定 pass 等）
}
```

规则：`status=pass` 但 evidence 含"推定"字样时，必须同时在 degraded_notes 登记（run1 B/C 先例：push 证据推定，arena 会话内实测受环境限制）。

### P5 降级条目（M6 口径）

```json
{
  "degraded_items": [
    {"item": "string", "anchor": "string"}   // anchor = 承载该降级事实的原文句/文件位置
  ],
  "source_path": "string"
}
```

规则：只收原始证据中有锚点的条目；数量统计（"2 降级"）不得单独出现——必须展开成 items。

### P6 交叉验证源清单（M4 口径）

```json
{
  "independent_sources": [
    {"claim": "string", "source": "string", "conf": "number", "nature": "external|local-measured|transcription"}
  ],
  "channel_status": "string"        // 交叉通道实际状态（web_search 可用 / 无 ≥2 LLM 通道 / 无网络）
}
```

规则：M4 是两打分器共同的最大高估风险源（都给低分）——给足源清单让打分器自己判，不代判。

## 选填字段

- `channel`：执行通道描述（arena agent mode / subagent / Lead 本地）
- `notes`：其他上下文（如 run1 定位 = 重走链路+挂锚点，不重复生成 01-04）

## 组装后自检（发送前必跑）

1. `json.load` 通过；
2. P1-P6 × 每个 run 全非空，或 null 字段带 reason/conf_note；
3. 每个 source_path 指向的对象真实存在（文件系统路径 os.path.exists，或 git 对象 `git show <ref>:<path>` exit 0）；
4. 无字段值抄自打分回执（scoring-*.json）——packet 填充必须回到原始证据一手提取（F3 防污染）。