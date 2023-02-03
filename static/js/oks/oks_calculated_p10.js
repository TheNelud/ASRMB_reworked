let in_structure = document.querySelectorAll('.js-structure');
let in_mmc = document.querySelectorAll('.js-mmc');
let in_cm = document.querySelectorAll('.js-cm');
let in_diff = document.querySelectorAll('.js-diff');

let in_structure_manual = document.querySelectorAll('.js-structure-manual');
let in_mmc_manual = document.querySelectorAll('.js-mmc-manual');
let in_cm_manual = document.querySelectorAll('.js-cm-manual');
let in_diff_manual = document.querySelectorAll('.js-diff-manual');


for (let i = 0; i < in_mmc.length; i++){
    in_mmc[i].value = 12 * Number(in_structure[i].value) + (Number(in_structure[i].value) * 2) + 2;
    in_structure[i].addEventListener('input', function (){
        in_mmc[i].value = 12 * Number(this.value) + (Number(this.value) * 2) + 2;
        in_diff[i].value = Number(in_cm[i].value) / Number(in_mmc[i].value);
    });
}

for (let i = 0; i < in_cm.length; i++){
    in_cm[i].addEventListener('input', function (){
       in_cm[i].value = this.value;
       in_diff[i].value = Number(in_cm[i].value) / Number(in_mmc[i].value);
    });
}

for (let i = 0; i < in_mmc_manual.length; i++){
    in_mmc_manual[i].addEventListener('input', function (){
        in_mmc_manual[i].value = this.value;
        in_diff_manual[i].value = Number(in_cm_manual[i].value) / Number(in_mmc_manual[i].value);
    });
}

for (let i = 0; i < in_cm_manual.length; i++){
    in_cm_manual[i].addEventListener('input', function (){
       in_cm_manual[i].value = this.value;
       in_diff_manual[i].value = Number(in_cm_manual[i].value) / Number(in_mmc_manual[i].value);
    });
}