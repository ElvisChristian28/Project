
let arr = ["red","blue","yellow","green"];

let gameSeq = [];
let userSeq = [];
let started = false;
let level = 0;

document.addEventListener("mousedown", function () {
    if (started == false) {
        console.log("started");
        started = true;

        levelup();
    }
})

function levelup()
{
    userSeq = []
    level++;
    let idx = Math.floor(Math.random() * 4 );
    let h3 = document.querySelector("h3");
    h3.innerText = `Level ${level}`;
    let color = arr[idx];
    let randbtn = document.querySelector(`.${color}`);
    btnflash(randbtn);
    gameSeq.push(arr[idx]);
}

function btnflash(btn)
{
    btn.classList.add("flash");
    setTimeout(function(){
        btn.classList.remove("flash");
    },250)
}

let allbtns = document.querySelectorAll(".btn");
// console.dir(allbtns);
for(btn of allbtns)
{
    btn.addEventListener("click",btnpress);
}

function btnpress()
{
    let btn = this;
    btnflash(btn);

    let userchoice = btn.getAttribute("id");
    // console.log(userchoice);
    userSeq.push(userchoice);
    checkAns(userSeq.length - 1);
}

function checkAns(idx){
    // let idx = level - 1;
    if(gameSeq[idx] === userSeq[idx]  )
    {
        if(userSeq.length == gameSeq.length)
        {
            setTimeout(levelup,600);
        }
        
    }
    else
    {
        let h3 = document.querySelector("h3");
        h3.innerHTML = `Game Over!! Your Score was <b> ${level} </b> <br> Please Try again`;
        document.querySelector("body").style.backgroundColor = "red";
        setTimeout(function(){
            document.querySelector("body").style.backgroundColor = "#787878";
        },150)
        reset();
    }
}

function reset(){
    gameSeq = [];
    userSeq = [];
    started = false;
    level = 0;
}