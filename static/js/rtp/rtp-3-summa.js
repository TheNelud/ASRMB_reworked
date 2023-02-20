let span_pr_op = document.querySelectorAll('.js-summ-pr_op');
let span_pr_pot = document.querySelectorAll('.js-summ-pr_pot');
let span_pr_pr = document.querySelectorAll('.js-summ-pr_pr');

let nums_pr_op = [];
let nums_pr_pot = [];
let nums_pr_pr = [];

for (let i=0; i<span_pr_op.length-1; i++){
    nums_pr_op.push(parseFloat(span_pr_op[i].textContent));
    nums_pr_pot.push(parseFloat(span_pr_pot[i].textContent));
    nums_pr_pr.push(parseFloat(span_pr_pr[i].textContent));
}

console.log(nums_pr_op);

span_pr_op[span_pr_op.length-1].textContent = sumArr(nums_pr_op);
span_pr_pot[span_pr_pot.length-1].textContent = sumArr(nums_pr_pot);
span_pr_pr[span_pr_pr.length-1].textContent = sumArr(nums_pr_pr);


function sumArr(arr){
  let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}