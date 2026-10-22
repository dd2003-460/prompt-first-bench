#!/usr/bin/env node
/*
 * Local, fresh-context browser worker for RALPH web-LLM cross checks.
 *
 * It intentionally relies only on public UI controls and does not inspect or
 * import any browser profile, cookie, credential, or storage-state file.
 */
import { chromium } from "playwright";

const chunks = [];
for await (const chunk of process.stdin) chunks.push(chunk);

function fail(message) {
  process.stderr.write(`${String(message)}\n`);
  process.exitCode = 1;
}

async function firstVisible(locator) {
  const count = await locator.count();
  for (let index = 0; index < count; index += 1) {
    const candidate = locator.nth(index);
    if (await candidate.isVisible()) return candidate;
  }
  return null;
}

async function clickIfVisible(locator) {
  const candidate = await firstVisible(locator);
  if (candidate) await candidate.click();
}

async function perplexity(page, prompt) {
  await clickIfVisible(page.getByRole("button", { name: "拒绝可选项" }));
  await clickIfVisible(page.getByRole("button", { name: "Reject optional" }));
  await clickIfVisible(page.locator('button[aria-label="关闭"]'));
  const input = await firstVisible(page.getByRole("textbox"));
  if (!input) throw new Error("Perplexity prompt box is unavailable; login or UI changed");
  await input.click();
  await input.pressSequentially(prompt, { delay: 8 });
  const submit = await firstVisible(page.locator('button[aria-label="提交"], button[aria-label="Submit"]'));
  if (!submit) throw new Error("Perplexity submit control is unavailable");
  await submit.click();
  await page.waitForTimeout(2500);
  await page.waitForLoadState("domcontentloaded");
  const answer = await page.locator("main").innerText({ timeout: 30_000 });
  if (!answer.trim()) throw new Error("Perplexity returned an empty page");
  return answer;
}

async function chatgpt(page, prompt) {
  const input = await firstVisible(page.locator("#prompt-textarea"));
  if (!input) throw new Error("ChatGPT prompt box is unavailable; sign in manually in the visible browser first");
  await input.click();
  await input.pressSequentially(prompt, { delay: 8 });
  const submit = await firstVisible(page.locator('button[data-testid="send-button"]'));
  if (!submit) throw new Error("ChatGPT submit control is unavailable");
  await submit.click();
  await page.waitForTimeout(2500);
  const answer = await page.locator("main").innerText({ timeout: 30_000 });
  if (!answer.trim()) throw new Error("ChatGPT returned an empty page");
  return answer;
}

async function gemini(page, prompt) {
  const input = await firstVisible(page.locator('[contenteditable="true"]'));
  if (!input) throw new Error("Gemini prompt box is unavailable; sign in manually in the visible browser first");
  await input.click();
  await input.pressSequentially(prompt, { delay: 8 });
  const submit = await firstVisible(page.locator('button[aria-label*="发送"], button[aria-label*="Send"]'));
  if (!submit) throw new Error("Gemini submit control is unavailable");
  await submit.click();
  await page.waitForTimeout(2500);
  const answer = await page.locator("main").innerText({ timeout: 30_000 });
  if (!answer.trim()) throw new Error("Gemini returned an empty page");
  return answer;
}

try {
  const config = JSON.parse(Buffer.concat(chunks).toString("utf8"));
  const loginMode = config && config.mode === "login";
  if (!loginMode && (!config || typeof config.prompt !== "string" || !config.prompt.trim())) throw new Error("missing prompt");
  if (!config || typeof config.url !== "string" || !config.url.startsWith("https://")) throw new Error("missing HTTPS url");
  const persistentProfile = typeof config.profile_dir === "string" && config.profile_dir.trim();
  const launchOptions = { headless: Boolean(config.headless) };
  if (typeof config.channel === "string" && config.channel.trim()) launchOptions.channel = config.channel.trim();
  const browser = persistentProfile ? null : await chromium.launch(launchOptions);
  const context = persistentProfile
    ? await chromium.launchPersistentContext(config.profile_dir, { ...launchOptions, locale: "zh-CN" })
    : await browser.newContext({ locale: "zh-CN" });
  try {
    const page = await context.newPage();
    page.setDefaultTimeout(Math.max(5_000, Math.min(Number(config.timeout_ms) || 45_000, 120_000)));
    await page.goto(config.url, { waitUntil: "domcontentloaded" });
    if (loginMode) {
      await page.waitForTimeout(Math.max(30_000, Math.min(Number(config.timeout_ms) || 900_000, 3_600_000)));
      process.stdout.write(JSON.stringify({ login_completed: true, page_url: page.url() }));
    } else {
      const response = await ({
        perplexity,
        chatgpt,
        gemini,
      }[config.site] || (() => { throw new Error(`unsupported browser site: ${config.site}`); }))(page, config.prompt);
      process.stdout.write(JSON.stringify({ response, page_url: page.url() }));
    }
  } finally {
    await context.close();
    if (browser) await browser.close();
  }
} catch (error) {
  fail(error instanceof Error ? error.message : error);
}
