let in_meter_p34 = document.querySelectorAll('.js-meter_p34');
let in_meter_30p1 = document.querySelectorAll('.js-meter_30p1');
let in_meter_10c1 = document.querySelectorAll('.js-meter_10c1');
let in_meter_10c4 = document.querySelectorAll('.js-meter_10c4');
let in_xrr_prod = document.querySelectorAll('.js-xrr_prod');

function calculated_meter(){
    in_meter_p34[1].value = 100;
    in_meter_30p1[1].value = 100;
    in_meter_10c1[1].value = 100;
    in_meter_10c4[1].value = 100;
    in_meter_p34[2].value = Number(in_meter_p34[0].value) / Number(in_meter_p34[1].value);
    in_meter_30p1[2].value = Number(in_meter_30p1[0].value)/ Number(in_meter_30p1[1].value);
    in_meter_10c1[2].value = Number(in_meter_10c1[0].value)/ Number(in_meter_10c1[1].value);
    in_meter_10c4[2].value = Number(in_meter_10c4[0].value)/ Number(in_meter_10c4[1].value);

    in_xrr_prod[0].value = Number(in_meter_p34[2].value);
    in_xrr_prod[1].value = Number(in_meter_30p1[2].value);
    in_xrr_prod[2].value = Number(in_meter_10c1[2].value);
    in_xrr_prod[3].value = Number(in_meter_10c4[2].value);

}

calculated_meter();

in_meter_p34[1].addEventListener('input',function (){
    in_meter_p34[2].value = Number(in_meter_p34[0].value) / Number(in_meter_p34[1].value);
    in_xrr_prod[0].value = Number(in_meter_p34[2].value);
})

in_meter_30p1[1].addEventListener('input', function(){
    in_meter_30p1[2].value = Number(in_meter_30p1[0].value)/ Number(in_meter_30p1[1].value);
    in_xrr_prod[1].value = Number(in_meter_30p1[2].value);
})

in_meter_10c1[1].addEventListener('input', function(){
    in_meter_10c1[2].value = Number(in_meter_10c1[0].value)/ Number(in_meter_10c1[1].value);
    in_xrr_prod[2].value = Number(in_meter_10c1[2].value);
})

in_meter_10c4[1].addEventListener('input', function(){
    in_meter_10c4[2].value = Number(in_meter_10c4[0].value)/ Number(in_meter_10c4[1].value);
    in_xrr_prod[3].value = Number(in_meter_10c4[2].value);
})