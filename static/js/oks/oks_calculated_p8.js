//for p8
let in_arr_c1506 = document.querySelectorAll('.js-sum-c1506');
let in_arr_c1641 = document.querySelectorAll('.js-sum-c1641');
let in_arr_average_values = document.querySelectorAll('.js-average_value');

for (let i=0; i<in_arr_c1506.length-1; i++){
     in_arr_c1506[i].addEventListener('input', function (){update_result_for_p8();});
}

for (let i=0; i<in_arr_c1641.length-1; i++){
     in_arr_c1641[i].addEventListener('input', function (){update_result_for_p8();});
}


function update_result_for_p8(){
    summ_c1506();
    summ_c1641();
    calculated_average_values();
}

function calculated_average_values(){
    for (let i=0; i<in_arr_average_values.length-1; i++){
        in_arr_average_values[i].value = (Number(in_arr_c1506[i].value) + Number(in_arr_c1641[i].value)) / 2;
    }
    in_arr_average_values[11].value = Number(in_arr_average_values[0].value) + Number(in_arr_average_values[1].value) + Number(in_arr_average_values[2].value) + Number(in_arr_average_values[3].value) + Number(in_arr_average_values[4].value) + Number(in_arr_average_values[5].value) + Number(in_arr_average_values[6].value) + Number(in_arr_average_values[7].value) + Number(in_arr_average_values[8].value) + Number(in_arr_average_values[9].value) + Number(in_arr_average_values[10].value);
    console.log(in_arr_average_values[11])
}

function summ_c1506(){
    in_arr_c1506[11].value = Number(in_arr_c1506[0].value) + Number(in_arr_c1506[1].value) + Number(in_arr_c1506[2].value) + Number(in_arr_c1506[3].value) + Number(in_arr_c1506[4].value) + Number(in_arr_c1506[5].value) + Number(in_arr_c1506[6].value) + Number(in_arr_c1506[7].value) + Number(in_arr_c1506[8].value) + Number(in_arr_c1506[9].value) + Number(in_arr_c1506[10].value);
}

function summ_c1641() {
    in_arr_c1641[11].value = Number(in_arr_c1641[0].value) + Number(in_arr_c1641[1].value) + Number(in_arr_c1641[2].value) + Number(in_arr_c1641[3].value) + Number(in_arr_c1641[4].value) + Number(in_arr_c1641[5].value) + Number(in_arr_c1641[6].value) + Number(in_arr_c1641[7].value) + Number(in_arr_c1641[8].value) + Number(in_arr_c1641[9].value) + Number(in_arr_c1641[10].value);
}