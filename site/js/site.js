(function(){
var mb=document.querySelector('.menu-btn'),nav=document.getElementById('nav');
if(mb)mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
// quote forms
document.querySelectorAll('form[data-lead]').forEach(function(f){
 var t0=Date.now(),msg=f.querySelector('.msg'),btn=f.querySelector('button[type=submit]');
 f.addEventListener('submit',function(e){
  e.preventDefault();
  var d=Object.fromEntries(new FormData(f).entries());d.elapsed=Date.now()-t0;d.page=location.pathname;
  btn.disabled=true;var old=btn.textContent;btn.textContent='Sending…';msg.className='msg';
  fetch('/api/lead',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)})
   .then(function(r){return r.json().catch(function(){return{}}).then(function(j){return{ok:r.ok&&j.ok,j:j}})})
   .then(function(x){
     if(x.ok){f.reset();msg.className='msg ok';msg.textContent='Thank you. Your request has been sent and we will call you shortly.'}
     else{msg.className='msg err';msg.textContent=(x.j&&x.j.error)||'Sorry, that did not send. Please call (770) 508-0971 and we will help right away.'}
   })
   .catch(function(){msg.className='msg err';msg.textContent='Sorry, that did not send. Please call (770) 508-0971 and we will help right away.'})
   .finally(function(){btn.disabled=false;btn.textContent=old});
 });
});
// gallery filter + lightbox
var fb=document.querySelectorAll('.filters button');
fb.forEach(function(b){b.addEventListener('click',function(){
 fb.forEach(function(x){x.setAttribute('aria-pressed',x===b)});
 var c=b.dataset.f;document.querySelectorAll('.gallery figure').forEach(function(g){g.style.display=(c==='all'||g.dataset.c===c)?'':'none'});
})});
var lb=document.getElementById('lb');
if(lb){document.querySelectorAll('.gallery img').forEach(function(i){i.addEventListener('click',function(){lb.querySelector('img').src=i.dataset.full||i.src;lb.querySelector('img').alt=i.alt;lb.classList.add('on')})});
 lb.addEventListener('click',function(){lb.classList.remove('on')});document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')})}
})();
