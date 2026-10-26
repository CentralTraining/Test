import { sharedApiProxy, proxyReply } from './api-proxy.ts';
import { authenticate, AccessError } from './access.ts';
import { teamOverview } from './team-overview.ts';
// Test permits authenticated Trainers to read team-wide TikTok metrics.
// Every mutation and OAuth callback keeps its original shared API permissions.
Deno.serve(async req=>{
 const base=Deno.env.get('SUPABASE_URL'),url=new URL(req.url);
 if(!base)return proxyReply({error:'Chưa sẵn sàng TikTok API.'},503);
 if(req.method==='GET'&&url.pathname.endsWith('/oauth/callback'))return sharedApiProxy(req,'',base,true);
 const origin=req.headers.get('origin');
 if(origin&&origin!=='https://centraltraining.github.io')return proxyReply({error:'Nguồn truy cập không hợp lệ.'},403);
 if(req.method==='OPTIONS')return new Response(null,{status:204,headers:{'Access-Control-Allow-Origin':'https://centraltraining.github.io','Access-Control-Allow-Headers':'content-type,apikey,authorization','Access-Control-Allow-Methods':'POST,OPTIONS','Vary':'Origin'}});
 if(req.method!=='POST')return proxyReply({error:'Chỉ hỗ trợ POST.'},405);
 if(Number(req.headers.get('content-length')||0)>8000)return proxyReply({error:'Yêu cầu quá dài.'},413);
 const raw=await req.text();if(raw.length>8000)return proxyReply({error:'Yêu cầu quá dài.'},413);
 let body;try{body=JSON.parse(raw);if(!body||typeof body!=='object'||Array.isArray(body))throw Error();}catch{return proxyReply({error:'Yêu cầu không hợp lệ.'},400);}
 if(body.action==='overview'){
  try{const principal=await authenticate(body.dashboardToken);return proxyReply({ok:true,...await teamOverview(body,principal)});}
  catch(error){return proxyReply({error:error instanceof AccessError?error.message:'Chưa đọc được tiến độ Xây kênh. Hãy thử lại.'},error instanceof AccessError?error.status:500);}
 }
 return sharedApiProxy(req,raw,base);
});
