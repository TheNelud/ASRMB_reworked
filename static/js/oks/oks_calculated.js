let in_mcc = document.querySelectorAll('.js-mcc');
let in_mmc = document.querySelectorAll('.js-mmc');
let in_tmm = document.querySelectorAll('.js-tmm');
let in_cm = document.querySelectorAll('.js-cm');
let in_calcm = document.querySelectorAll('.js-calcm');

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
    in_mcc[11].value = Number(in_mcc[0].value) + Number(in_mcc[1].value) + Number(in_mcc[2].value) + Number(in_mcc[3].value) + Number(in_mcc[4].value) + Number(in_mcc[5].value) + Number(in_mcc[6].value) + Number(in_mcc[7].value) + Number(in_mcc[8].value) + Number(in_mcc[9].value) + Number(in_mcc[10].value);
}

function summa_mmc() {
    in_mmc[11].value = Number(in_mmc[0].value) + Number(in_mmc[1].value) + Number(in_mmc[2].value) + Number(in_mmc[3].value) + Number(in_mmc[4].value) + Number(in_mmc[5].value) + Number(in_mmc[6].value) + Number(in_mmc[7].value) + Number(in_mmc[8].value) + Number(in_mmc[9].value) + Number(in_mmc[10].value);
}

function summa_cm() {
    in_cm[11].value = Number(in_cm[0].value) + Number(in_cm[1].value) + Number(in_cm[2].value) + Number(in_cm[3].value) + Number(in_cm[4].value) + Number(in_cm[5].value) + Number(in_cm[6].value) + Number(in_cm[7].value) + Number(in_cm[8].value) + Number(in_cm[9].value) + Number(in_cm[10].value);
}

