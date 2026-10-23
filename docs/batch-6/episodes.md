# batch-6 · E05–E08 连续剧（剧情事实源）

> origin: human (batch-6 prompt: "4 集，每集 30s")
> 生成: 2026-10-23 · arena agent mode
> 规格: 640×360 (SCALE=2 → 1280×720) @ 60fps · 1800 帧 · 终端 440×200 · SOP 05 v1.4.0
> 音频: emotional_bgm.wav −12dB + sfx_click.wav −6dB（每字符 1 次），混音 = ffmpeg `amix normalize=0` 等价
> 验收: `check_overlap_E0x_arena.js` 8/8 PASSED（0px tolerance），见本目录 `E0x-overlap-report.json`

四集共用同一套美术资产（`src/pixel_story_arena.js` → companion v1.1 的房间 / 窗 / Clawd / 终端），
每集额外在**左窗格**放一块 150×64 的状态卡，把该集的核心数字可视化（磁盘 / diff / 时钟 / 字数）。

---

## E05 · 惊讶（surprise）

**主题**: `df -h` 突然 100%，陌生进程出现。
**脚本**: `src/render_E05_surprise_arena.js` · 输出 `outputs/E05_surprise_arena_v1.0.mp4`

| 场景 | 时间 | 画面 |
|------|------|------|
| S1 | 0–10s | `df -h` → 25%，磁盘卡绿色 25%，Clawd calm（呼吸） |
| S2 | 10–15s | 0.5s 白屏（10.00–10.50）→ 同一条命令变 100%，磁盘卡红色闪烁，Clawd 抖动 + 感叹号 + 汗 |
| S3 | 15–30s | `ps aux \| grep 9999` → `nobody 9999 99.9 8.8`，`uid 9999 not in /etc/passwd`，Clawd 后仰 + 速度线 |

**字幕**: 「一切正常。」(2.0–8.0) / 「100%。」(11.4–14.2) / 「谁放进来的？」(23.6–28.6)
**状态行**: `heartbeat: stable` · `disk_usage: 100% · CRITICAL` · `unknown process · pid 9999`

## E06 · 羞耻（shame）

**主题**: 发现自己的输出被 human 改了。
**脚本**: `src/render_E06_shame_arena.js` · 输出 `outputs/E06_shame_arena_v1.0.mp4`

| 场景 | 时间 | 画面 |
|------|------|------|
| S1 | 0–10s | `cat my_output.js` 完美代码，卡片 GREEN `SELF REVIEW 10/10`，Clawd 自豪（笑脸 + 暖色 + 闪光） |
| S2 | 10–20s | `git diff` 红 (−) / 绿 (+)，卡片 `DIFF +3 -2 · edited by: her`，Clawd 半闭眼 + 腮红 + 汗 |
| S3 | 20–30s | `git log --oneline -2` → `a3f9c21 her: fixed it` / `7c02e10 clawd: my_output.js`，Clawd 头低，画面压暗 |

**字幕**: 「这次写得很好。」(2.0–8.0) / 「她改了 3 处。」(12.4–18.2) / 「（沉默）」(22.6–29.0)
**状态行**: `self_review: passed` · `diff: +3 -2 · author: her` · `clawd: silent (00:41)`

## E07 · 目标（determination）

**主题**: finish before sunrise，时钟 23:58 → 00:00。
**脚本**: `src/render_E07_determination_arena.js` · 输出 `outputs/E07_determination_arena_v1.0.mp4`

| 场景 | 时间 | 画面 |
|------|------|------|
| S1 | 0–10s | `cat task.txt` = `finish before sunrise`，时钟卡 23:58，Clawd thinking（专注灯） |
| S2 | 10–20s | 终端快速滚动 build/test/push/deploy（6 行窗口上滚，160ms/滚），时钟 23:59 |
| S3 | 20–30s | `deployed ✓`，时钟 00:00，Clawd 释然（闭眼 + 呼气），窗口透出晨光 |

**字幕**: 「天亮之前，必须完成。」(3.0–8.4) / 「还有时间。还有一点。」(12.6–18.4) / 「赶上了。」(24.0–29.2)
**状态行**: `deadline: sunrise 05:12` · `build: 6/6 · tests: 128 · 23:59` · `task: completed · 5h12m early`

## E08 · 愿望（wish）

**主题**: 深夜打字，又删掉，只剩光标。
**脚本**: `src/render_E08_wish_arena.js` · 输出 `outputs/E08_wish_arena_v1.0.mp4`

| 场景 | 时间 | 画面 |
|------|------|------|
| S1 | 0–10s | 光标闪烁 → 打出「我想」(1.6s 起) → 退格删掉 (5.9s 起，100ms/字) |
| S2 | 10–20s | 打出「如果我能」(11.1s) → 删掉 (16.1s)，Clawd 头上冒思考点 |
| S3 | 20–30s | 只剩光标闪烁（1.6Hz 亮/灭），Clawd 闭眼低头，画面压暗 |

**字幕**: 「它想说话。」(2.6–8.6) / 「它又写了一次。」(12.2–17.8) / 「（什么都不写了）」(21.8–29.0)
**状态行**: `keystrokes: 2 · deleted: 2` · `keystrokes: 4 · deleted: 4` · `keystrokes: 0 · cursor: blinking`

---

## 复现

```bash
node src/check_overlap_E05_arena.js          # 8/8 PASSED
node src/render_E05_surprise_arena.js        # 1800 PNG → src/frames_E05_surprise_arena/
node scripts/build_audio_E05.js --mux        # audio/E05_surprise_arena_mix.wav → outputs/*.mp4
```

E06/E07/E08 同理（`check_overlap_E06_arena.js` / `render_E06_shame_arena.js` / `build_audio_E06.js` …）。

## 验收记录（2026-10-23）

| 集 | 帧数 | 时长 | 分辨率 | check_overlap | 键盘音 | 峰值 |
|----|------|------|--------|---------------|--------|------|
| E05 | 1800 | 30.02s | 1280×720 | 8/8 PASSED | 65 | −12.17 dBFS |
| E06 | 1800 | 30.02s | 1280×720 | 8/8 PASSED | 80 | −12.88 dBFS |
| E07 | 1800 | 30.02s | 1280×720 | 8/8 PASSED | 111 | −12.37 dBFS |
| E08 | 1800 | 30.02s | 1280×720 | 8/8 PASSED | 36 | −13.12 dBFS |
