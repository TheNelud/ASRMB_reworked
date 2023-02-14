let in_date = document.querySelectorAll('.js-date');
let in_num_one = document.querySelectorAll('.js-num_one');
let in_num_two = document.querySelectorAll('.js-num_two');
let result_summa =document.getElementsByClassName('.js-summa-meter_reading')


let in_qgr_sh = document.querySelectorAll('.js-qgr_sh');
let in_ng_prod = document.querySelectorAll('.js-ng_prod');
let in_ng_pl = document.querySelectorAll('.js-ng_pl');
let in_xg_prod = document.querySelectorAll('.js-xg_prod');
let in_pgr_sh = document.querySelectorAll('.js-pgr_sh');

let in_nr_prod_const = document.querySelectorAll(".js-nr_prod_const");
console.log(in_nr_prod_const[0].textContent)

let date = new Date();
let firstDay = new Date(date.getFullYear(), date.getMonth(), 2);
let lastDay = new Date(date.getFullYear(), date.getMonth()+1, 1);

in_date[0].value = firstDay.toISOString().split('T')[0];
in_date[1].value = lastDay.toISOString().split('T')[0];


for (let i=0; i<in_num_one.length-1; i++){
    in_num_one[i].addEventListener('input', function (){
         in_num_one[2].value = Number(in_num_one[1].value) - Number(in_num_one[0].value);
         result_summa.textContent = Number(in_num_one[2].value) + Number(in_num_two[2].value);
         in_qgr_sh[0].value = Number(in_num_one[2].value);
         in_pgr_sh[1].value = Number(in_qgr_sh[0].value) * Number(in_xg_prod[0].value)
    });
}

for (let i=0; i<in_num_two.length-1; i++){
    in_num_two[i].addEventListener('input', function (){
        in_num_two[2].value = Number(in_num_two[1].value) - Number(in_num_two[0].value);
        result_summa.textContent = Number(in_num_one[2].value) + Number(in_num_two[2].value);
        in_qgr_sh[1].value = Number(in_num_two[2].value);
        in_pgr_sh[1].value = Number(in_qgr_sh[1].value) * Number(in_xg_prod[1].value)
    });
}


for (let i=0; i<in_ng_prod.length; i++){
    in_ng_prod[i].value = parseFloat(in_nr_prod_const[0].textContent);
}

for (let i=0; i<in_ng_pl.length; i++){
    in_ng_pl[i].addEventListener('input', function (){
        in_xg_prod[i].value = Number(in_ng_prod[i].value)/ Number(in_ng_pl[i].value);
        in_pgr_sh[i].value = Number(in_qgr_sh[i].value) * Number(in_xg_prod[i].value)
    });
}