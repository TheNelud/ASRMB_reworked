let input_rtp = document.querySelectorAll('.js-claculated');
for (let i=0; i<input_rtp.length; i++) {
    input_rtp[i].value = 0;
}

input_rtp[0].addEventListener('input', function (){calculated_vop();});
input_rtp[1].addEventListener('input', function (){calculated_vop();});
input_rtp[2].addEventListener('input', function (){calculated_vop();});
input_rtp[3].addEventListener('input', function (){calculated_vop();});
input_rtp[4].addEventListener('input', function (){calculated_vop();});
input_rtp[5].addEventListener('input', function (){calculated_vop();});
input_rtp[6].addEventListener('input', function (){calculated_vop();});
input_rtp[11].addEventListener('input', function (){calculated_vop();});


function calculated_vop(){
    input_rtp[7].value = Number(input_rtp[0]) +
        Number(input_rtp[1])+
        Number(input_rtp[2])+
        Number(input_rtp[3])+
        Number(input_rtp[4])+
        Number(input_rtp[5])+
        Number(input_rtp[6])+
        Number(input_rtp[11]);


    // input_rtp[7].value = (2893 * Number(input_rtp[0].value) *
    //     ((Number(input_rtp[1].value)/(Number(input_rtp[2].value)*Number(input_rtp[3]))) -
    //         (Number(input_rtp[4].value) / (Number(input_rtp[5].value) * Number(input_rtp[6].value)))) *
    //         Number(input_rtp[11].value)
    // );
    console.log(input_rtp[7].value);
}

calculated_vop();