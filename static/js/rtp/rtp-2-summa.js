let in_qgr_sh = document.querySelectorAll('.js-qgr_sh');
let in_pgr_sh = document.querySelectorAll('.js-pgr_sh');
let nums_qgr_sh = [];
let nums_pgr_sh = [];

for (let i=0; i<in_qgr_sh.length-1; i++){
    nums_qgr_sh.push(parseFloat(in_qgr_sh[i].textContent));
    nums_pgr_sh.push(parseFloat(in_pgr_sh[i].textContent));
}

in_qgr_sh[in_qgr_sh.length-1].textContent = sumArr(nums_qgr_sh);
in_pgr_sh[in_pgr_sh.length-1].textContent = sumArr(nums_pgr_sh);


function sumArr(arr){
  let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}