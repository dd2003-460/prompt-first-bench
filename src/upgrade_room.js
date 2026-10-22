// Adapted from d1-video-recreation render_goodmorning_arena.js (reference commit in docs).
const WIN={x:60,y:20,w:520,h:160,fw:8}, BW=640,BH=360;
const C={bgWarm:'#F5EDD5',stripe:'#EDE3C8',woodFrame:'#8B7355',woodSill:'#A08060',skyTop:'#87CEEB',skyBottom:'#E0F0FF',mountain:'#5A7A5A',pink:'#FF9AA2'};
function px(ctx,x,y,w,h,color){ctx.fillStyle=color;ctx.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
function drawBackground(ctx, t, opts = {}) {
  // 1. Warm striped wallpaper (#F5EDD5 + #EDE3C8 every 16px)
  px(ctx, 0, 0, BW, BH, C.bgWarm);
  for (let x = 0; x < BW; x += 16) {
    px(ctx, x, 0, 8, BH, C.stripe);
  }

  // 2. Window (x60 y20 520×160, wood frame #8B7355 8px)
  const { x: wx, y: wy, w: ww, h: wh, fw } = WIN;
  px(ctx, wx, wy, ww, wh, C.woodFrame);

  // Inner glass area clipped cleanly inside wood frame
  const gx = wx + fw;
  const gy = wy + fw;
  const gw = ww - 2 * fw;
  const gh = wh - 2 * fw;

  ctx.save();
  ctx.beginPath();
  ctx.rect(gx, gy, gw, gh);
  ctx.clip();

  // Sky gradient (#87CEEB -> #E0F0FF)
  const grd = ctx.createLinearGradient(0, gy, 0, gy + gh);
  grd.addColorStop(0, C.skyTop);
  grd.addColorStop(1, C.skyBottom);
  ctx.fillStyle = grd;
  ctx.fillRect(gx, gy, gw, gh);

  // Optional warm morning sun inside sky pane (G1 / morning warmth)
  if (opts.morningSun) {
    const sx = wx + 86;
    const sy = wy + 40;
    const pulse = Math.sin(t * 1.8) > 0 ? 2 : 0;
    px(ctx, sx - 18 - pulse, sy - 18 - pulse, 36 + pulse * 2, 36 + pulse * 2, 'rgba(255,228,130,0.22)');
    px(ctx, sx - 12, sy - 12, 24, 24, 'rgba(255,224,110,0.45)');
    px(ctx, sx - 8, sy - 8, 16, 16, '#FFE478');
  }

  // 2 distant mountains (#5A7A5A)
  ctx.fillStyle = C.mountain;
  ctx.beginPath();
  ctx.moveTo(gx, gy + gh);
  ctx.lineTo(wx + 130, wy + 72);
  ctx.lineTo(wx + 230, gy + gh);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(wx + 175, gy + gh);
  ctx.lineTo(wx + 330, wy + 50);
  ctx.lineTo(wx + 470, gy + gh);
  ctx.closePath();
  ctx.fill();

  // 2 animated pixel clouds
  const cx1 = wx + 104 + Math.round(Math.sin(t * 0.35) * 14);
  px(ctx, cx1, wy + 36, 40, 10, 'rgba(255,255,255,0.92)');
  px(ctx, cx1 + 8, wy + 30, 24, 6, 'rgba(255,255,255,0.92)');

  const cx2 = wx + 326 + Math.round(Math.cos(t * 0.25) * 16);
  px(ctx, cx2, wy + 52, 48, 10, 'rgba(255,255,255,0.90)');
  px(ctx, cx2 + 10, wy + 46, 28, 6, 'rgba(255,255,255,0.90)');

  ctx.restore();

  // Cross mullion (十字窗棂)
  px(ctx, wx + ww / 2 - 3, gy, 6, gh, C.woodFrame);
  px(ctx, gx, wy + wh / 2 - 3, gw, 6, C.woodFrame);

  // Windowsill (窗台)
  px(ctx, wx - 4, wy + wh, ww + 8, 8, C.woodSill);
  px(ctx, wx - 4, wy + wh, ww + 8, 2, C.woodFrame);

  // Potted plant on left windowsill (盆栽, x=88..104, clear of terminal & notes)
  const px0 = wx + 28;
  const py0 = wy + wh;
  px(ctx, px0 + 2, py0 - 16, 10, 8, '#6AA86A');
  px(ctx, px0, py0 - 13, 14, 5, '#4E864E');
  px(ctx, px0 + 4, py0 - 19, 6, 3, '#7BC07B');
  px(ctx, px0 + 6, py0 - 21, 2, 2, C.pink);
  px(ctx, px0, py0 - 8, 14, 2, '#B06A46');
  px(ctx, px0 + 1, py0 - 6, 12, 6, '#945234');
}


module.exports={drawBackground};
