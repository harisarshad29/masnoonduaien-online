// Renders favicon/app icons and one 1200x630 share image per dua into static/assets
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const duas=JSON.parse(fs.readFileSync(process.argv[2]));const OUT='static/assets';
const star=`<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#C8A24A" stroke-width="1" opacity=".3"><rect x="20" y="20" width="24" height="24"/><rect x="20" y="20" width="24" height="24" transform="rotate(45 32 32)"/><path d="M0 32h8M56 32h8M32 0v8M32 56v8"/></svg>`;
const bg=`background:#0F2236 url('data:image/svg+xml,${encodeURIComponent(star)}') repeat;background-size:64px`;
const icon=s=>`<html><body style="margin:0"><div style="width:${s}px;height:${s}px;${bg};display:grid;place-items:center;border-radius:${s*0.22}px">
<svg width="${s*0.62}" height="${s*0.62}" viewBox="0 0 100 100"><g fill="none" stroke="#C8A24A" stroke-width="5"><rect x="22" y="22" width="56" height="56"/><rect x="22" y="22" width="56" height="56" transform="rotate(45 50 50)"/></g><circle cx="50" cy="50" r="12" fill="#C8A24A"/></svg></div></body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [s,n] of [[512,'icon-512.png'],[192,'icon-192.png'],[180,'apple-touch-icon.png'],[48,'favicon-48.png']]){
 await p.setViewportSize({width:s,height:s});await p.setContent(icon(s));await p.screenshot({path:path.join(OUT,'icons',n),omitBackground:true});}
await p.setViewportSize({width:1200,height:630});
for(const d of duas){
 const html=`<html><head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&display=swap"></head><body style="margin:0">
 <div style="width:1200px;height:630px;${bg};display:flex;flex-direction:column;justify-content:center;align-items:center;font-family:Amiri,'Noto Naskh Arabic',serif;color:#fff;padding:60px;box-sizing:border-box">
 <div style="border:2px solid #C8A24A;border-radius:28px;padding:50px 60px;width:100%;box-sizing:border-box;text-align:center;background:rgba(15,34,54,.82)">
 <div dir="rtl" style="font-size:${d.ar.length>70?44:d.ar.length>40?56:72}px;line-height:1.8">${d.ar}</div>
 <div style="font-family:system-ui,sans-serif;font-size:34px;color:#E9DDB8;margin-top:24px">${d.en}</div></div>
 <div style="font-family:system-ui,sans-serif;font-size:26px;color:#C8A24A;margin-top:28px">masnoonduaien.online</div></div></body></html>`;
 await p.setContent(html);await p.waitForTimeout(150);await p.screenshot({path:path.join(OUT,'og',d.id+'.png')});}
await b.close();})();
