# T23 Gold 差距诊断 — PFB 执行工件为何无法达到 gold

> origin: ai · 2026-11-05 · Lead 撰写
> 触发：成璐问"拿着 pfb 执行的例子还是有问题，无法实现 gold，问题究竟出在什么方面，能通过 pfb 达成吗"

## 结论先行

**gold 可达，但当前 S2+ 臂在"断网环境"下运行——调研阶段名存实亡。不是 gold 太难，是检索通道断了。** 三个层面的故障按因果链排列：

## 层 1：检索层（根因）

S2/S3 臂的 sources 字段实测（runs/*.json）：

| 臂 | Q1 sources 样例 | 判定 |
|----|----------------|------|
| S0/S1 | 0 sources（设计如此，无调研） | OK |
| S2-Q1-r1 | 5 × `bing.com/ck/a?!&&p=...` 跳转链接 | **假调研** |
| S3-Q5-r1 | 5 × `bing.com/ck/a` 跳转链接 | **假调研** |
| D1-Q1 (deepsearch baseline) | 7 × 真实 URL（hyperstack/cloudgputracker/thundercompute/runpod/io.net） | 真调研 |

- bing 跳转链接不可定位、不可核验；Q1 的 5 个来源展开后是 Microsoft Office 下载页等无关内容。
- ego-browser 通道在 run 时未接通 → 模型"调研"退化为凭记忆编 + 凑数来源。
- **讽刺点**：D1（外部 deepsearch 系统）是唯一拿到真实 URL 的臂——我们的 S2+ 臂比外部 baseline 还弱，因为 harness 没给它联网工具。

## 层 2：judge 测量层（放大失真）

- **M6（调研真实性）判 1.0**：judge 只查 URL 存活，不查"页面内容是否支持对应断言"。bing 跳转链存活 → 满分。半异源 7B 更甚（evidence 写"大部分断言有社区实测数据支持"=印象分）。
- **M5（坏消息位置）全臂 0.000**：gate 分类器没抓到任何限制句——要么报告里确实没有（与 M4 分数矛盾），要么分类器词表太窄。两个 judge 都给 0，说明是系统性测量失效而非模型行为。
- **M2 被交给 LLM 判**（半异源脚本 bug）：M2 按设计是 gates.py 确定性正则计算，产生最高 +0.95 的假分歧。

## 层 3：gold 可达性判断

gold Q1 要求带 workload 条件的结论（"单卡 decode 差 1.3–1.7x"）。工件要够到它需要：
1. 查到真实 benchmark（MLPerf / 厂商白皮书 / 社区实测）→ **层 1 断供**
2. 区分 SXM/PCIe、训练/推理场景 → 需要读多个来源交叉比对
3. 显式标注哪些数字查不到 → M4 维度

**可达路径**：修 harness 给 S2+ 臂接真实联网工具（ego-browser 或 search API）→ 重跑 S2-S5 → 用 v2 校准 prompt 的 judge 复评。预期：M6 从虚高 1.0 回落到真实水平，M4/M1 上升（真查到了才能标缺口、对事实）。

## 对论文的含义

当前 stage-ablation 结果只能解读为：**"在检索通道失效的环境下，加调研阶段（S2+）不增益甚至负效应"**——这是真实的实验发现（环境依赖性的消融），但不能外推为"调研阶段无用"。paper-draft.md 的 threats 一节必须声明此 confound，并列出修复路径作为 future work（或修复后重跑升级为主结果）。

## 行动项

- [ ] harness 接入真实联网工具（ego-browser nodejs 驱动 search，或 Bing/Google API）
- [ ] 修 M5 gate 分类器（先人工核对 3 份报告确认是词表问题还是真无限制句）
- [ ] 修半异源脚本：M2/M3 走 gates.py，LLM 只判 M1/M4/M5/M6
- [ ] 重跑 S2-S5（至少 Q1/Q5 两域各 2 rep）
- [ ] 三方 judge 对比（同源 27B / arena-v1 / arena-v2）落 T23-final-analysis.md
