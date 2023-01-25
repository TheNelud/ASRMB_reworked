let sum   = document.getElementById('id_form-11-molar_content_of_components');
let small = document.querySelectorAll('.item_js_molar_content_of_components');
let numbers = [];

for (let i = 0; i < small.length; i++){
    numbers.push(small[i].value);
    small[i].addEventListener('input', function (){
        numbers[i] = this.value;
        updateResults();});
}

updateResults();

function updateResults(){
    sum.value = sumArr(numbers);
}

function sumArr(arr){
    let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}

