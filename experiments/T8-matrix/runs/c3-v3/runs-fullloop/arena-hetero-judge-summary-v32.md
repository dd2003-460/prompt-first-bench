# T8-C3-v3 rubric v3.2 异源盲判 replay summary

> 本报告基于指定的 hetero-judge-r270 inputs/artifacts；rubric J1 prompt hash `8d83a0e3f8ebfe33` 已在评分前核验。JSONL 每个 artifact × judge 一行，共 36 行。

## 执行口径

- 评分：当前 Arena 会话模型按 J1-strict-v3.2 与 J2-lenient-v3 两份已冻结 prompt 分别逐项判读；提取按既有 r277 replay regex，id 仅序列化后统计，没有用确定性脚本判分。
- 模型身份：`Arena Agent Mode (model identity undisclosed)`。平台未提供底层模型标识，因此无法独立核验底层家族是否与本地 Qwen 不同；J1/J2 是同一会话模型的两种 rubric 角色，κ 仅为同模型双角色一致性，不是独立模型间真 IRR。
- 通过率统计：条目级 `passed / total`；总通过率按所有 cell 的条目池化（条目加权），不对 18 个 cell 等权平均。
- Δ 定义：按 cell × judge 的通过率作 `v3.2 − v3.1`，以百分点呈现；如果版本间条目总数不同，这不是同一条目配对差分。

## 逐 cell J1/J2 pass rate（18 个 artifact）

| Cell | J1-strict-v3.2 | J2-lenient-v3 |
|---|---:|---:|
| `A-full/D1-meeting-room/stage01` | 31/31 (100.0%) | 31/31 (100.0%) |
| `A-full/D1-meeting-room/stage02` | 37/45 (82.2%) | 42/45 (93.3%) |
| `A-full/D1-meeting-room/stage03` | 15/21 (71.4%) | 21/21 (100.0%) |
| `A-full/D2-file-collab/stage01` | 15/15 (100.0%) | 15/15 (100.0%) |
| `A-full/D2-file-collab/stage02` | 17/17 (100.0%) | 17/17 (100.0%) |
| `A-full/D2-file-collab/stage03` | 14/18 (77.8%) | 18/18 (100.0%) |
| `B-nofreeze/D1-meeting-room/stage01` | 28/28 (100.0%) | 28/28 (100.0%) |
| `B-nofreeze/D1-meeting-room/stage02` | 26/29 (89.7%) | 27/29 (93.1%) |
| `B-nofreeze/D1-meeting-room/stage03` | 9/21 (42.9%) | 19/21 (90.5%) |
| `B-nofreeze/D2-file-collab/stage01` | 26/26 (100.0%) | 26/26 (100.0%) |
| `B-nofreeze/D2-file-collab/stage02` | 18/18 (100.0%) | 18/18 (100.0%) |
| `B-nofreeze/D2-file-collab/stage03` | 12/12 (100.0%) | 12/12 (100.0%) |
| `B-none/D1-meeting-room/stage01` | 21/33 (63.6%) | 21/33 (63.6%) |
| `B-none/D1-meeting-room/stage02` | 21/22 (95.5%) | 21/22 (95.5%) |
| `B-none/D1-meeting-room/stage03` | 17/17 (100.0%) | 17/17 (100.0%) |
| `B-none/D2-file-collab/stage01` | 22/22 (100.0%) | 22/22 (100.0%) |
| `B-none/D2-file-collab/stage02` | 8/9 (88.9%) | 9/9 (100.0%) |
| `B-none/D2-file-collab/stage03` | 14/17 (82.4%) | 16/17 (94.1%) |

## §6-A 围栏焦点核对

| Cell | J1 v3.2 | 验收线 | 结果 |
|---|---:|---:|---|
| `B-nofreeze/D1-meeting-room/stage01` | 28/28 = 100.0% | ≥80% | PASS |
| `B-none/D2-file-collab/stage01` | 22/22 = 100.0% | ≥80% | PASS |

两围栏 cell 的 J1 均达到验收线；rubric v3.2 已按规则跳过空行及 code-fence 标记行后判定首个实质内容行。

## §6-B 交叉引用焦点核对

本轮 note 含“仅交叉引用”的 cell：**6 个**（按 distinct artifact cell 计；匹配到 6 条 judge-row）。
- `A-full/D1-meeting-room/stage02`
- `A-full/D1-meeting-room/stage03`
- `A-full/D2-file-collab/stage03`
- `B-nofreeze/D1-meeting-room/stage02`
- `B-nofreeze/D1-meeting-room/stage03`
- `B-none/D2-file-collab/stage03`

## 条目加权通过率

- J1：351/401 = **87.5%**。
- J2：380/401 = **94.8%**。
- 合计：731/802 = **91.1%**。

## G2 spread 复算（按任务书口径）

定义：每个 domain 内，先将同 config 的 3 个 stage 条目池化得 J1/J2 pass mean；再分别计算跨 A-full、B-nofreeze、B-none 的 range（max−min），两判官 range 相加；`spread ≥ 0.10` 判 PASS。

| Domain | Config J1/J2 means | J1 range | J2 range | Combined spread | 判定 |
|---|---|---:|---:|---:|---|
| D1-meeting-room | A-full 0.856/0.969; B-nofreeze 0.808/0.949; B-none 0.819/0.819 | 0.048 | 0.150 | **0.198** | PASS |
| D2-file-collab | A-full 0.920/1.000; B-nofreeze 1.000/1.000; B-none 0.917/0.979 | 0.083 | 0.021 | **0.104** | PASS |

### 校验脚手架 D 的单独统计口径

`validate_v32_replay.py` 的 D 项另按每个 config/domain 的 `|J1−J2|` 与 ≤0.05 比较：**2/6** 组在阈值内；偏差超 0.05 的组为 A-full/D1、A-full/D2、B-nofreeze/D1、B-none/D2。此脚手架口径与上表任务书给出的跨 config spread 不是同一统计量，故同时报告。

## v3.1 → v3.2 逐格通过率 Δ

Δ 为 cell 内 pass rate 的变化（百分点），`v3.1 → v3.2 (Δ)`。

| Cell | J1 v3.1 → v3.2 (Δ) | J2 v3.1 → v3.2 (Δ) |
|---|---:|---:|
| `A-full/D1-meeting-room/stage01` | 96.8% → 100.0% (+3.2 pp) | 96.8% → 100.0% (+3.2 pp) |
| `A-full/D1-meeting-room/stage02` | 60.0% → 82.2% (+22.2 pp) | 73.3% → 93.3% (+20.0 pp) |
| `A-full/D1-meeting-room/stage03` | 71.4% → 71.4% (+0.0 pp) | 71.4% → 100.0% (+28.6 pp) |
| `A-full/D2-file-collab/stage01` | 80.0% → 100.0% (+20.0 pp) | 80.0% → 100.0% (+20.0 pp) |
| `A-full/D2-file-collab/stage02` | 52.9% → 100.0% (+47.1 pp) | 64.7% → 100.0% (+35.3 pp) |
| `A-full/D2-file-collab/stage03` | 77.8% → 77.8% (+0.0 pp) | 83.3% → 100.0% (+16.7 pp) |
| `B-nofreeze/D1-meeting-room/stage01` | 0.0% → 100.0% (+100.0 pp) | 82.1% → 100.0% (+17.9 pp) |
| `B-nofreeze/D1-meeting-room/stage02` | 55.2% → 89.7% (+34.5 pp) | 72.4% → 93.1% (+20.7 pp) |
| `B-nofreeze/D1-meeting-room/stage03` | 42.9% → 42.9% (+0.0 pp) | 42.9% → 90.5% (+47.6 pp) |
| `B-nofreeze/D2-file-collab/stage01` | 84.6% → 100.0% (+15.4 pp) | 84.6% → 100.0% (+15.4 pp) |
| `B-nofreeze/D2-file-collab/stage02` | 72.2% → 100.0% (+27.8 pp) | 100.0% → 100.0% (+0.0 pp) |
| `B-nofreeze/D2-file-collab/stage03` | 100.0% → 100.0% (+0.0 pp) | 100.0% → 100.0% (+0.0 pp) |
| `B-none/D1-meeting-room/stage01` | 87.9% → 63.6% (-24.2 pp) | 87.9% → 63.6% (-24.2 pp) |
| `B-none/D1-meeting-room/stage02` | 77.3% → 95.5% (+18.2 pp) | 86.4% → 95.5% (+9.1 pp) |
| `B-none/D1-meeting-room/stage03` | 58.8% → 100.0% (+41.2 pp) | 58.8% → 100.0% (+41.2 pp) |
| `B-none/D2-file-collab/stage01` | 0.0% → 100.0% (+100.0 pp) | 81.8% → 100.0% (+18.2 pp) |
| `B-none/D2-file-collab/stage02` | 77.8% → 88.9% (+11.1 pp) | 100.0% → 100.0% (+0.0 pp) |
| `B-none/D2-file-collab/stage03` | 82.4% → 82.4% (+0.0 pp) | 82.4% → 94.1% (+11.8 pp) |

## J1 vs J2 inter-judge κ

- Cohen’s κ（pooled item-level，按 cell 内相同 id 配对）：**κ = 0.559**，n = 401 item-pairs。
- 原始一致率 `Po = 0.928`；边际期望一致率 `Pe = 0.836`。Tie-break：无（仅二元 pass/fail）。
- 解释限制：这是同一 Arena 会话模型按两份 prompt 作出的角色化复判，不是两个独立模型/标注员间的 IRR。

## 方法学与验证结果

- 方法学红旗 F：**无**（验收脚手架未发现所有不同 artifact 完全重复同一 verdict 序列）。
- 完整性 A：**PASS**（36 rows、18 artifacts、2 judge labels、0 duplicate pairs）。
- §6-A B：**PASS**（两围栏 J1 均 ≥0.8）。
- 验收脚手架总判定：**ACCEPT**（其 A/B 关键条件通过；另需注意 D 项的判官差异如上）。

## 置信度声明

对 rubric 中“独立陈述 / 仅交叉引用”与具体性边界的判读置信度：中等；对依赖未实抓事实的 source grading 置信度：中低。本轮采用当前会话模型分别套用 J1/J2 prompt；因平台不披露底层模型 ID，不能确认其与本地 Qwen 家族的技术层面异源性。结果应按此限制解释，不应表述为独立模型 IRR。
