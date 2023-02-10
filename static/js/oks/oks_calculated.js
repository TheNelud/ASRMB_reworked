let in_mcc = document.querySelectorAll('.js-mcc');
let in_mmc = document.querySelectorAll('.js-mmc');
let in_tmm = document.querySelectorAll('.js-tmm');
let in_cm = document.querySelectorAll('.js-cm');
let in_calcm = document.querySelectorAll('.js-calcm');
//for p4
let in_coc = document.querySelectorAll('.js-coc');
let in_poc = document.querySelectorAll('.js-poc');


for (let i=0; i<in_mcc.length-1; i++){
    in_mcc[i].addEventListener('input', function (){update_result();});
}

for (let i=0; i<in_mmc.length-1; i++){
    in_mmc[i].addEventListener('input', function (){update_result();});
}

for (let i=0; i<in_cm.length-1; i++){
    in_cm[i].addEventListener('input', function (){update_result();});
}

update_result();

function update_result(){
    summa_mcc();
    summa_mmc();
    calculated_tmm();
    summa_cm();
    calculated_calc();
    calculated_coc();
    calculated_poc();
}

function calculated_poc(){
    for (let i=0; i<in_poc.length-1; i++){
        in_poc[i].value = Number(in_coc[i].value) / Number(in_mmc[i].value) * 24.04;
    }
    in_poc[11].value = Number(in_poc[0].value) + Number(in_poc[1].value) + Number(in_poc[2].value) + Number(in_poc[3].value) + Number(in_poc[4].value) + Number(in_poc[5].value) + Number(in_poc[6].value) + Number(in_poc[7].value) + Number(in_poc[8].value) + Number(in_poc[9].value) + Number(in_poc[10].value);
}

function calculated_coc(){
    for (let i=0; i<in_coc.length-1; i++){
        in_coc[i].value = 1.1500 * Number(in_calcm[i].value) / 100;
    }
    in_coc[11].value = Number(in_coc[0].value) + Number(in_coc[1].value) + Number(in_coc[2].value) + Number(in_coc[3].value) + Number(in_coc[4].value) + Number(in_coc[5].value) + Number(in_coc[6].value) + Number(in_coc[7].value) + Number(in_coc[8].value) + Number(in_coc[9].value) + Number(in_coc[10].value);
}

function calculated_calc (){
    for (let i=0; i<in_calcm.length-1; i++){
        in_calcm[i].value = Number(in_tmm[i].value)/ Number(in_tmm[11].value) * 100;
    }
    in_calcm[11].value = Number(in_calcm[0].value) + Number(in_calcm[1].value) + Number(in_calcm[2].value) + Number(in_calcm[3].value) + Number(in_calcm[4].value) + Number(in_calcm[5].value) + Number(in_calcm[6].value) + Number(in_calcm[7].value) + Number(in_calcm[8].value) + Number(in_calcm[9].value) + Number(in_calcm[10].value);
}

function calculated_tmm(){
    for (let i=0; i<in_tmm.length-1; i++){
        in_tmm[i].value = (Number(in_mcc[i].value) * Number(in_mmc[i].value))/100;
    }
    in_tmm[11].value = Number(in_tmm[0].value) + Number(in_tmm[1].value) + Number(in_tmm[2].value) + Number(in_tmm[3].value) + Number(in_tmm[4].value) + Number(in_tmm[5].value) + Number(in_tmm[6].value) + Number(in_tmm[7].value) + Number(in_tmm[8].value) + Number(in_tmm[9].value) + Number(in_tmm[10].value);
    return in_tmm[11].value
}

function summa_mcc() {
    in_mcc[11].value = Number(in_mcc[0].value) + Number(in_mcc[1].value) +
        Number(in_mcc[2].value) + Number(in_mcc[3].value) +
        Number(in_mcc[4].value) + Number(in_mcc[5].value) +
        Number(in_mcc[6].value) + Number(in_mcc[7].value) +
        Number(in_mcc[8].value) + Number(in_mcc[9].value) + Number(in_mcc[10].value);
}

function summa_mmc() {
    in_mmc[11].value = Number(in_mmc[0].value) + Number(in_mmc[1].value) + Number(in_mmc[2].value) + Number(in_mmc[3].value) + Number(in_mmc[4].value) + Number(in_mmc[5].value) + Number(in_mmc[6].value) + Number(in_mmc[7].value) + Number(in_mmc[8].value) + Number(in_mmc[9].value) + Number(in_mmc[10].value);
}

function summa_cm() {
    in_cm[11].value = Number(in_cm[0].value) + Number(in_cm[1].value) + Number(in_cm[2].value) + Number(in_cm[3].value) + Number(in_cm[4].value) + Number(in_cm[5].value) + Number(in_cm[6].value) + Number(in_cm[7].value) + Number(in_cm[8].value) + Number(in_cm[9].value) + Number(in_cm[10].value);
}


// //for p8
// let in_arr_c1506 = document.querySelectorAll('.js-sum-c1506');
// let in_arr_c1641 = document.querySelectorAll('.js-sum-c1641');
// let in_arr_average_values = document.querySelectorAll('.js-average_value');
//
// for (let i=0; i<in_arr_c1506.length-1; i++){
//      in_arr_c1506[i].addEventListener('input', function (){update_result_for_p8();});
// }
//
// for (let i=0; i<in_arr_c1641.length-1; i++){
//      in_arr_c1641[i].addEventListener('input', function (){update_result_for_p8();});
// }
//
//
// function update_result_for_p8(){
//     summ_c1506();
//     summ_c1641();
//     calculated_average_values();
// }
//
// function calculated_average_values(){
//     for (let i=0; i<in_arr_average_values.length-1; i++){
//         in_arr_average_values[i].value = (Number(in_arr_c1506[i].value) + Number(in_arr_c1641[i].value)) / 2;
//     }
//     in_arr_average_values[11].value = Number(in_arr_average_values[0].value) + Number(in_arr_average_values[1].value) + Number(in_arr_average_values[2].value) + Number(in_arr_average_values[3].value) + Number(in_arr_average_values[4].value) + Number(in_arr_average_values[5].value) + Number(in_arr_average_values[6].value) + Number(in_arr_average_values[7].value) + Number(in_arr_average_values[8].value) + Number(in_arr_average_values[9].value) + Number(in_arr_average_values[10].value);
//
// }
//
// function summ_c1506(){
//     in_arr_c1506[11].value = Number(in_arr_c1506[0].value) + Number(in_arr_c1506[1].value) + Number(in_arr_c1506[2].value) + Number(in_arr_c1506[3].value) + Number(in_arr_c1506[4].value) + Number(in_arr_c1506[5].value) + Number(in_arr_c1506[6].value) + Number(in_arr_c1506[7].value) + Number(in_arr_c1506[8].value) + Number(in_arr_c1506[9].value) + Number(in_arr_c1506[10].value);
// }
//
// function summ_c1641(){
//     in_arr_c1641[11].value = Number(in_arr_c1641[0].value) + Number(in_arr_c1641[1].value) + Number(in_arr_c1641[2].value) + Number(in_arr_c1641[3].value) + Number(in_arr_c1641[4].value) + Number(in_arr_c1641[5].value) + Number(in_arr_c1641[6].value) + Number(in_arr_c1641[7].value) + Number(in_arr_c1641[8].value) + Number(in_arr_c1641[9].value) + Number(in_arr_c1641[10].value);
// }
