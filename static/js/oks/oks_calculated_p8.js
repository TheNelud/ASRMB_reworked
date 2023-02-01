let in_arr_c1506 = document.querySelectorAll('.js-sum-c1506');
let in_arr_c1641 = document.querySelectorAll('.js-sum-c1641');
let in_arr_average_values = document.querySelectorAll(('.js-average_value'))

let in_sum_c1506 = document.getElementById('id_form-11-cylinder_1506');
let in_sum_c1641 = document.getElementById('id_form-11-cylinder_1641');

let numbers_c1506 = [];
for (let i=0; i < in_arr_c1506.length; i++){
    in_arr_c1506[i].addEventListener('input',function (){
        console.log(this.value)
        numbers_c1506[i]= this.value;
        update_result();});
}


let numbers_c1641 = [];
for (let i=0; i<in_arr_c1641.length; i++){
    in_arr_c1641[i].addEventListener('input', function (){
        numbers_c1641[i] = this.value;
        update_result();});
}

update_result();

function update_result(){
    in_sum_c1506.value=summa_array(numbers_c1506);
    in_sum_c1641.value=summa_array(numbers_c1641);
}

function average_value(c1506, c1641){


}

function summa_array(array){
    let x = 0;
    for( let i = 0; i < array.length; i++ ){
    x += +array[i]; // (*2)
    }
    return x;
}