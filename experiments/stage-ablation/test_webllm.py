import subprocess, json

query = 'H100 GPU FLOPS'
js = '''
(async () => {
const task = await taskSpace('test-chatgpt-' + Date.now());
const page = task.page('p1');
await page.goto('https://chatgpt.com/', { timeout: 30000, waitUntil: 'domcontentloaded' });
await page.waitForTimeout(5000);

const body0 = await page.evaluate(() => document.body ? document.body.innerText : '');
if (/免费搜索次数上限|free (search )?(limit|allowance)|sign in to continue|log in/i.test(body0)) {
  console.log(JSON.stringify({ error: 'QUOTA_OR_LOGIN', body: body0.slice(0, 200) }));
  return;
}

const input = await page.evaluate(() => {
  const sel = ['[role="textbox"]', 'textarea', '[contenteditable="true"]', 'input[type="text"]'];
  for (const s of sel) {
    const el = document.querySelector(s);
    if (el) { el.focus(); return true; }
  }
  return false;
});
if (!input) { console.log(JSON.stringify({ error: 'NO_INPUT' })); return; }
await page.waitForTimeout(300);

const inputResult = await page.evaluate((q) => {
  const sel = ['[role="textbox"]', 'textarea', '[contenteditable="true"]', 'input[type="text"]'];
  for (const s of sel) {
    const el = document.querySelector(s);
    if (el) {
      el.focus();
      el.textContent = q;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      return s;
    }
  }
  return null;
}, ''' + json.dumps(query) + ''');
if (!inputResult) {
  console.log(JSON.stringify({ error: 'NO_INPUT_SEL' }));
  return;
}
await page.waitForTimeout(300);
await page.keyboard.press('Enter');

let resp = '';
for (let i = 0; i < 8; i++) {
  await page.waitForTimeout(5000);
  resp = await page.evaluate(() => {
    const body = document.body ? document.body.innerText : '';
    return body;
  });
  if (resp.length > 800) break;
}
console.log('RESP_LEN:' + resp.length);
console.log('RESP_HEAD:' + resp.slice(0, 500));

const links = await page.evaluate(() => {
  const domain = window.location.hostname;
  const seen = new Set();
  const out = [];
  for (const a of document.querySelectorAll('a')) {
    const h = a.href;
    if (h && !h.includes(domain) && !h.startsWith('#') && !h.startsWith('javascript:') && /^https?:/.test(h) && !seen.has(h)) {
      seen.add(h);
      out.push(h);
    }
  }
  const bodyText = document.body ? document.body.innerText : '';
  const urlRegex = /https?:\\/\\/[^\\s<>"{}|\\^`\\x60]+/g;
  const textUrls = bodyText.match(urlRegex) || [];
  for (const u of textUrls) {
    const clean = u.replace(/[).,;!?]+$/, '');
    if (!clean.includes(domain) && !seen.has(clean)) {
      seen.add(clean);
      out.push(clean);
    }
  }
  return out;
});
console.log('LINKS:' + JSON.stringify(links));
})()
'''

result = subprocess.run(['/Users/a1-6/.local/bin/ego-browser', 'nodejs', '-e', js], capture_output=True, text=True, timeout=90)
print('STDOUT:', result.stdout)
print('STDERR:', result.stderr[:500])
