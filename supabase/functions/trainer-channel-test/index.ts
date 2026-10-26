import { sharedApiProxy, proxyReply } from './api-proxy.ts';
// Authentication, permissions and encrypted channel storage live in trainer-channel-api.
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
 try{JSON.parse(raw);}catch{return proxyReply({error:'Yêu cầu không hợp lệ.'},400);}
 return sharedApiProxy(req,raw,base);
});
