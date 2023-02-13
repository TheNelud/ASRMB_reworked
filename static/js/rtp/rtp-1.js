let input_rtp = document.querySelectorAll('.js-calculated');
console.log(input_rtp)

input_rtp[0].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[1].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[2].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[3].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[4].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[5].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[6].addEventListener('input', function (){calculated_vop();calculated_pr_op();});
input_rtp[11].addEventListener('input', function (){calculated_vop();calculated_pr_op();});

input_rtp[9].addEventListener('input', function (){calculated_xr_prod();calculated_pr_op();});

input_rtp[13].addEventListener('input', function (){input_rtp[8].value = input_rtp[13].value;calculated_pr_op();})

calculated_vop();
function calculated_vop(){
    input_rtp[7].value = (2893 * Number(input_rtp[0].value) *
        ((Number(input_rtp[1].value) / (Number(input_rtp[2].value)*Number(input_rtp[3].value))) -
            (Number(input_rtp[4].value) / (Number(input_rtp[5].value) * Number(input_rtp[6].value)))) *
            Number(input_rtp[11].value)).toFixed(3);
}

function calculated_xr_prod(){
    if (Number(input_rtp[9].value) === 0){
        input_rtp[10].value = 0;

    }else{
        input_rtp[10].value = (Number(input_rtp[8].value) / Number(input_rtp[9].value)).toFixed(3);
    }
}

function calculated_pr_op(){
    input_rtp[12].value = (2893 * (2893 * Number(input_rtp[0].value) *
        ((Number(input_rtp[1].value) / (Number(input_rtp[2].value)*Number(input_rtp[3].value))) -
            (Number(input_rtp[4].value) / (Number(input_rtp[5].value) * Number(input_rtp[6].value)))) *
           Number(input_rtp[10].value) * Number(input_rtp[11].value)) ).toFixed(3);
}