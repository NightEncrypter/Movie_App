feather.replace()
gsap.from('.ellipse-1',{opacity:0,duration:0.5,rotate:360,scale:0.1,stagger:0.1})
gsap.from('.theatre', { opacity: 0, duration: 2, x: 300 })
gsap.from('.writer', { opacity: 0, duration: 2, x: 200 ,stagger:0.2})






//gsap.from('.ellipse-2',{opacity:0,duration:1,x:-50,stagger:0.4})
const search_btn = document.querySelector('.search-btn');
const drop_down=document.querySelector('.dropdown')
const cancel_search=document.querySelector('.cancel-search')
const ham=document.querySelector('.ham')
const sidebar=document.querySelector('.sidebar')
const sidebar_anim=document.querySelector('.side-link-anim')
const sidebarShift=document.querySelector('.sidebar_shift');
const stickyEffect=document.querySelector('.sticky-effect');
const contentShift=document.querySelector('.content-shift');
const logoSide=document.querySelector('.logo-side');
const sideLink=document.querySelector('.side-link');
const hamIcon=document.querySelector('.ham-icon');
// const playPause=document.querySelector('.play-pause');
const playVideo=document.querySelector('.play-video');

const loginPassInput=document.getElementById('loginPassInput')
const firstName=document.getElementById('reg-firstname')
const lastName=document.getElementById('reg-lastname')
const registerEmailInput=document.getElementById('registerEmailInput')
const registerPassConfirmInput=document.getElementById('registerPassConfirmInput')
const registerPassInput=document.getElementById('registerPassInput')
const loginEmailInput=document.getElementById('loginEmailInput')
const loginButton=document.getElementById('loginButton')
const regButton=document.getElementById('reg-btn')
const showKey=document.getElementById('showkey')
const regShowKey=document.querySelector('.regshowkey')
const alertContainer=document.getElementById('alert-container')

function onPlayPause() {

  console.log("hey")
  if (playVideo.paused) {
    playVideo.play()
  } else  {
    playVideo.pause()
  }
}


let scrolled = false;
window.addEventListener("scroll", (event) => {
  if (this.scrollY > 100) {
    
    if (!scrolled) {
      stickyEffect.style.transform = "translateY(-100%)"
      
      setTimeout(() => {
      stickyEffect.style.transform = "translateY(0px)"
        
      },400)
}
    // console.log("hey",this.scrollY)
    stickyEffect.classList.add('active')
  } else {
 
    stickyEffect.classList.remove('active')
    
  }
})






ham.addEventListener('click', () => {
  const newElement = document.createElement('i');

  sidebar.classList.toggle('active');

  


  contentShift.classList.toggle('active');
  logoSide.classList.toggle('active');

  ham.classList.toggle("active")

  

  // if (sidebar.classList.contains('active')) {

  // newElement.setAttribute("data-feather", "x")
  // ham.replaceChild(newElement,hamIcon)

  // } else {
  // newElement.setAttribute("data-feather", "menu")
  // ham.replaceChild(newElement,hamIcon)

  // }
  // sidebar_anim.classList.toggle('active');
  //  if(sidebar.classList.contains('active')){
    sideLink.classList.toggle('active');
    console.log(sideLink.classList.contains('active'))

//  }

})


search_btn.addEventListener('click',()=>{
  drop_down.classList.toggle('search-dropdown')
})
cancel_search.addEventListener('click',()=>{
drop_down.classList.remove('search-dropdown')
});



function checkLoginInputVal(){

  console.log(loginEmailInput.value,loginPassInput)
if(loginEmailInput.value !== "" && loginPassInput.value !== ""){
  loginButton.classList.add("off");
  loginButton.disabled = false;


} else {
  loginButton.classList.remove("off");
  loginButton.disabled = true;

  
}



}
function checkRegisterInputVal(){

  // console.log(firstName.value,lastName.value,registerEmailInput.value,registerPassInput.value)
if(firstName.value !== "" && lastName.value !== "" && registerEmailInput.value !==''&& registerPassInput.value !==""&& registerPassConfirmInput.value!==''){
  regButton.classList.add("off");
  regButton.disabled = false;
 

} else {
  regButton.classList.remove("off");
  regButton.disabled = true;

  
}



}


function showPassword() {
  let checkStatus = loginPassInput.getAttribute("type")

  if(checkStatus=="password"){
    loginPassInput.setAttribute("type","text")
    showKey.setAttribute("data-feather","unlock")
  }else{
    loginPassInput.setAttribute("type","password")
    showKey.setAttribute("data-feather","lock")

  }

  
}
function showRegPassword() {
  let checkStatus = registerPassInput.getAttribute("type")

  if(checkStatus=="password"){
    registerPassInput.setAttribute("type","text")
    regShowKey.setAttribute("data-feather","unlock")
  }else{
    registerPassInput.setAttribute("type","password")
    regShowKey.setAttribute("data-feather","lock")

  }

  
}





// const alertDiscard=document.querySelector('.alert-discard')
if(alertContainer){
  setTimeout(()=>{
     
    alertContainer.style.opacity=0;
    alertContainer.style.transform="translateY(70px)";
    setTimeout(()=>alertContainer.remove(),1000)
  },3000)
  }
  




function discardedAlert() {
  // setTimeout(()=>{
     

  setTimeout(() => {
    alertContainer.style.opacity=0;
    alertContainer.style.transform="translateY(70px)";
    alertContainer.remove()
  }
    , 2000)
  // },3000)

}
