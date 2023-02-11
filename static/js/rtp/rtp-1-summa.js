let span_vop = document.querySelectorAll('.js-summa_vop');
let span_prop = document.querySelectorAll('.js-summa_prop');
let numbers_vop = [];
let numver_prop = [];
for (let i=0; i<span_vop.length-1; i++){
    if (span_vop[i].textContent === '-'){
        span_vop[i].textContent = '0';
    }
    if (span_prop[i].textContent === '-'){
        span_prop[i].textContent = '0';
    }
    numbers_vop.push(parseFloat(span_vop[i].textContent));
    numver_prop.push(parseFloat(span_prop[i].textContent));
}
console.log(sumArr(numbers_vop));
console.log(sumArr(numver_prop));

span_vop[span_vop.length-1].textContent = sumArr(numbers_vop);
span_prop[span_prop.length-1].textContent = sumArr(numver_prop);

function sumArr(arr){
  let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}