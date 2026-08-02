const questions = [

{
question:"What does CPU stand for?",
options:[
" A) Central Process Unit",
" B) Central Processing Unit",
" C) Computer Personal Unit",
" D) Central Processor Utility"
],
answer:"B"

},

{
question:"Which language is known as the mother of all languages?",
options:[
"A) Python",
"B) Java",
"C) C",
"D) C++"
],
answer:"C"

},

{
question:"What does RAM stand for?",
options:[
"A) Random Access Memory",
"B) Read Access Memory",
"C) Run Access Memory",
"D) Random Active Memory"
],
answer:"A"

}

];


let currentQuestion=0;
let score=0;
let review=[];


let question=document.getElementById("question");
let options=document.getElementById("options");
let next=document.getElementById("next-btn");


function loadQuestion(){

    let q=questions[currentQuestion];

    question.innerHTML=
    `Question ${currentQuestion+1}: ${q.question}`;


    options.innerHTML="";


    q.options.forEach(option=>{

        let button=document.createElement("button");

        button.innerText=option;


        button.onclick=function(){

            let userAnswer=option.trim()[0];


            if(userAnswer===q.answer){

                button.classList.add("correct");
                score++;

                review.push(
                    `${q.question}<br>
                    Your answer: ${userAnswer} ✅`
                );

            }

            else{

                button.classList.add("wrong");

                review.push(
                    `${q.question}<br>
                    Your answer: ${userAnswer} ❌ 
                    | Correct answer: ${q.answer}`
                );

            }


            document
            .querySelectorAll("#options button")
            .forEach(btn=>btn.disabled=true);

        };


        options.appendChild(button);

    });

}



next.onclick=function(){

    currentQuestion++;


    if(currentQuestion < questions.length){

        loadQuestion();

    }

    else{

        showResult();

    }

};



function showResult(){


document.getElementById("quiz-box")
.classList.add("hide");


document.getElementById("result")
.classList.remove("hide");


let percentage =
(score/questions.length)*100;


document.getElementById("score")
.innerHTML=
`Score: ${score}/${questions.length}`;


document.getElementById("percentage")
.innerHTML=
`${percentage}% - ${percentage>=50?"Pass":"Fail"}`;


document.getElementById("review")
.innerHTML=
review.join("<br><br>");

}


loadQuestion();
