let in_date = document.querySelectorAll('.js-date');
let in_num_one = document.querySelectorAll('.js-num_one');
let in_num_two = document.querySelectorAll('.js-num_two');
let result_summa =document.getElementsByClassName('.js-summa-meter_reading')

let date = new Date();
let firstDay = new Date(date.getFullYear(), date.getMonth(), 2);
let lastDay = new Date(date.getFullYear(), date.getMonth()+1, 1);

in_date[0].value = firstDay.toISOString().split('T')[0];
in_date[1].value = lastDay.toISOString().split('T')[0];


for (let i=0; i<in_num_one.length-1; i++){
    in_num_one[i].addEventListener('input', function (){
         in_num_one[2].value = Number(in_num_one[1].value) - Number(in_num_one[0].value);
         result_summa.textContent = Number(in_num_one[2].value) + Number(in_num_two[2].value);
         console.log(result_summa.textContent);
    });
}

for (let i=0; i<in_num_two.length-1; i++){
    in_num_two[i].addEventListener('input', function (){
        in_num_two[2].value = Number(in_num_two[1].value) - Number(in_num_two[0].value);
        result_summa.textContent = Number(in_num_one[2].value) + Number(in_num_two[2].value);
        console.log(result_summa.textContent);
    });
}


