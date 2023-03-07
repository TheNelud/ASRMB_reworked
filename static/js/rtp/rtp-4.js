//for RecyclingcalcOneTimeForm
let in_type_time = document.querySelectorAll('.js-type_time')
let in_time = document.querySelectorAll('.js-time');

//for mj
let in_mj = document.getElementsByClassName('js-mj')[0].value;

//for RecyclingcalcOneForm
let in_type = document.querySelectorAll('.js-type ');
let in_aij = document.querySelectorAll('.js-aij');
let in_bij = document.querySelectorAll('.js-bij');
let in_tauij = document.querySelectorAll('.js-tauij');
let in_a_ij = document.querySelectorAll('.js-a_ij');
let in_mi = document.querySelectorAll('.js-mi');
let in_q_yp = document.querySelectorAll('.js-q_yp');

let in_t_type =document.querySelectorAll('.js-t_type');
let in_t_aij = document.querySelectorAll('.js-t_aij');
let in_t_bij = document.querySelectorAll('.js-t_bij');
let in_t_tauij = document.querySelectorAll('.js-t_tauij');
let in_t_a_ij = document.querySelectorAll('.js-t_a_ij');
let in_t_mi = document.querySelectorAll('.js-t_mi');
let in_t_q_yp = document.querySelectorAll('.js-t_q_yp');

for (let i=0; i < in_time.length; i++ ){
    in_time[i].addEventListener('input', function (){
        console.log(in_time[i].value)
        for(let j=0; j<in_tauij.length; j++){
            if (new RegExp(in_type_time[i].value).test(in_type[j].value)){
                in_tauij[j].value = Number(in_time[i].value);
                result_q_yp();
            }
            if (new RegExp(in_type_time[i].value).test(in_t_type[j].value)){
                in_t_tauij[j].value = Number(in_time[i].value);
                result_q_yp();
            }
        }
    })
}

for (let i=0; i < in_aij.length; i++){
    in_aij[i].addEventListener('input', function (){
        console.log(in_aij[i].value);
        result_q_yp();
    })
}

for (let i=0; i < in_t_aij.length; i++){
    in_t_aij[i].addEventListener('input', function (){
        console.log(in_t_aij[i].value);
        result_t_q_yp();
    })
}

for (let i=0; i < in_bij.length; i++){
    in_bij[i].addEventListener('input', function (){
        console.log(in_bij[i].value);
        result_q_yp();
    })
}

for (let i=0; i < in_t_bij.length; i++){
    in_t_bij[i].addEventListener('input', function (){
        console.log(in_t_bij[i].value);
        result_t_q_yp();
    })
}

for (let i=0; i < in_a_ij.length; i++){
    in_a_ij[i].addEventListener('input', function (){
        console.log(in_a_ij[i].value);
        result_q_yp();
    })
}

for (let i=0; i < in_t_a_ij.length; i++){
    in_t_a_ij[i].addEventListener('input', function (){
        console.log(in_a_ij[i].value);
        result_t_q_yp();
    })
}

for (let i=0; i < in_mi.length; i++){
    in_mi[i].value = Number(in_mj.replace(',', '.'));
    in_t_mi[i].value = Number(in_mj.replace(',', '.'));
    result_q_yp();
    result_t_q_yp();
}

// for (let i=0; i < in_q_yp.length; i++){
//     in_q_yp[i].addEventListener('input', function (){
//         console.log(in_q_yp[i].value);
//     })
// }
function result_q_yp(){
    for (let i=0; i<in_q_yp.length; i++){
    if (in_mi[i].value === 0){
        in_q_yp[i].value = 0;
    }

    in_q_yp[i].value = (24.04 * Number(in_aij[i].value) *
        Number(in_bij[i].value) *
        Number(in_tauij[i].value) *
        Number(in_a_ij[i].value) /
        Number(in_mi[i].value)).toFixed(3)
    }
}

function result_t_q_yp(){
    for (let i=0; i<in_t_q_yp.length; i++){
    if (in_t_mi[i].value === 0){
        in_t_q_yp[i].value = 0;
    }

    in_t_q_yp[i].value = (24.04 * Number(in_t_aij[i].value) *
        Number(in_t_bij[i].value) *
        Number(in_t_tauij[i].value) *
        Number(in_t_a_ij[i].value) /
        Number(in_t_mi[i].value)).toFixed(3)
    }
}

