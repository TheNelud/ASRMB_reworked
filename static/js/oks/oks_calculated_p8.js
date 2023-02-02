let in_arr_c1506 = document.querySelectorAll('.js-sum-c1506');
let in_arr_c1641 = document.querySelectorAll('.js-sum-c1641');
let in_arr_average_values = document.querySelectorAll('.js-average_value');

let in_sum_c1506 = document.getElementsByClassName('js-sum-c1506-result');
let in_sum_c1641 = document.getElementsByClassName('js-sum-c1641-result');
let in_sum_avarage_value = document.getElementsByClassName('js-sum-average_value-result');

let numbers_average_value = [];
let numbers_c1506 = [];
let numbers_c1641 = [];

for (let i=0; i < in_arr_c1506.length; i++){
    in_arr_c1506[i].addEventListener('input',function (){
        numbers_c1506[i]= this.value;
        update_result();});
}

for (let i=0; i<in_arr_c1641.length; i++){
    in_arr_c1641[i].addEventListener('input', function (){
        numbers_c1641[i] = this.value;
        update_result();});

}

update_result();

function update_result(){
    in_sum_c1506[0].value=summa_array(numbers_c1506);
    in_sum_c1641[0].value=summa_array(numbers_c1641);
    average_value(numbers_c1506,numbers_c1641 );
    in_sum_avarage_value[0].value = summa_array(numbers_average_value);
}

function average_value(c1506, c1641){
    for (let i = 0; i < c1506.length; i++){
        in_arr_average_values[i].value = (Number(c1506[i]) + Number(c1641[i])) / 2;
        numbers_average_value[i] = in_arr_average_values[i].value;
    }
}

function summa_array(array){
    let x = 0;
    for( let i = 0; i < array.length; i++ ){
        x += +array[i];
    }
    return x;
}