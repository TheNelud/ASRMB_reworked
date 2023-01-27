let in_0_msk = document.getElementById('id_form-0-molar_content_of_components');
let in_0_mmk = document.getElementById('id_form-0-molar_mass_of_the_component');
let in_0_mmo = document.getElementById('id_form-0-total_molar_mass');
let in_0_mh = document.getElementById('id_form-0-chromatograph_mass');
let in_0_mr = document.getElementById('id_form-0-calculated_mass');

let in_1_msk = document.getElementById('id_form-1-molar_content_of_components');
let in_1_mmk = document.getElementById('id_form-1-molar_mass_of_the_component');
let in_1_mmo = document.getElementById('id_form-1-total_molar_mass');
let in_1_mh = document.getElementById('id_form-1-chromatograph_mass');
let in_1_mr = document.getElementById('id_form-1-calculated_mass');

let in_2_msk = document.getElementById('id_form-2-molar_content_of_components');
let in_2_mmk = document.getElementById('id_form-2-molar_mass_of_the_component');
let in_2_mmo = document.getElementById('id_form-2-total_molar_mass');
let in_2_mh = document.getElementById('id_form-2-chromatograph_mass');
let in_2_mr = document.getElementById('id_form-2-calculated_mass');

let in_3_msk = document.getElementById('id_form-3-molar_content_of_components');
let in_3_mmk = document.getElementById('id_form-3-molar_mass_of_the_component');
let in_3_mmo = document.getElementById('id_form-3-total_molar_mass');
let in_3_mh = document.getElementById('id_form-3-chromatograph_mass');
let in_3_mr = document.getElementById('id_form-3-calculated_mass');

let in_4_msk = document.getElementById('id_form-4-molar_content_of_components');
let in_4_mmk = document.getElementById('id_form-4-molar_mass_of_the_component');
let in_4_mmo = document.getElementById('id_form-4-total_molar_mass');
let in_4_mh = document.getElementById('id_form-4-chromatograph_mass');
let in_4_mr = document.getElementById('id_form-4-calculated_mass');

let in_5_msk = document.getElementById('id_form-5-molar_content_of_components');
let in_5_mmk = document.getElementById('id_form-5-molar_mass_of_the_component');
let in_5_mmo = document.getElementById('id_form-5-total_molar_mass');
let in_5_mh = document.getElementById('id_form-5-chromatograph_mass');
let in_5_mr = document.getElementById('id_form-5-calculated_mass');

let in_6_msk = document.getElementById('id_form-6-molar_content_of_components');
let in_6_mmk = document.getElementById('id_form-6-molar_mass_of_the_component');
let in_6_mmo = document.getElementById('id_form-6-total_molar_mass');
let in_6_mh = document.getElementById('id_form-6-chromatograph_mass');
let in_6_mr = document.getElementById('id_form-6-calculated_mass');

let in_7_msk = document.getElementById('id_form-7-molar_content_of_components');
let in_7_mmk = document.getElementById('id_form-7-molar_mass_of_the_component');
let in_7_mmo = document.getElementById('id_form-7-total_molar_mass');
let in_7_mh = document.getElementById('id_form-7-chromatograph_mass');
let in_7_mr = document.getElementById('id_form-7-calculated_mass');

let in_8_msk = document.getElementById('id_form-8-molar_content_of_components');
let in_8_mmk = document.getElementById('id_form-8-molar_mass_of_the_component');
let in_8_mmo = document.getElementById('id_form-8-total_molar_mass');
let in_8_mh = document.getElementById('id_form-8-chromatograph_mass');
let in_8_mr = document.getElementById('id_form-8-calculated_mass');

let in_9_msk = document.getElementById('id_form-9-molar_content_of_components');
let in_9_mmk = document.getElementById('id_form-9-molar_mass_of_the_component');
let in_9_mmo = document.getElementById('id_form-9-total_molar_mass');
let in_9_mh = document.getElementById('id_form-9-chromatograph_mass');
let in_9_mr = document.getElementById('id_form-9-calculated_mass');

let in_10_msk = document.getElementById('id_form-10-molar_content_of_components');
let in_10_mmk = document.getElementById('id_form-10-molar_mass_of_the_component');
let in_10_mmo = document.getElementById('id_form-10-total_molar_mass');
let in_10_mh = document.getElementById('id_form-10-chromatograph_mass');
let in_10_mr = document.getElementById('id_form-10-calculated_mass');

let in_11_msk = document.getElementById('id_form-11-molar_content_of_components');
let in_11_mmk = document.getElementById('id_form-11-molar_mass_of_the_component');
let in_11_mmo = document.getElementById('id_form-11-total_molar_mass');
let in_11_mh = document.getElementById('id_form-11-chromatograph_mass');
let in_11_mr = document.getElementById('id_form-11-calculated_mass');

in_0_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_1_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_2_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_3_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_4_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_5_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_6_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_7_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_8_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_9_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})
in_10_msk.addEventListener('input', function (){summa_msk();summa_mmo();calculated_mr(summa_mmo());})

in_0_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_1_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_2_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_3_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_4_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_5_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_6_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_7_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_8_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_9_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})
in_10_mmk.addEventListener('input', function (){summa_mmk();summa_mmo();calculated_mr(summa_mmo());})

in_0_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_1_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_2_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_3_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_4_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_5_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_6_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_7_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_8_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})
in_10_mmo.addEventListener('input', function (){summa_mmo();calculated_mr(summa_mmo());})

in_0_mh.addEventListener('input', function (){summa_mh();})
in_1_mh.addEventListener('input', function (){summa_mh();})
in_2_mh.addEventListener('input', function (){summa_mh();})
in_3_mh.addEventListener('input', function (){summa_mh();})
in_4_mh.addEventListener('input', function (){summa_mh();})
in_5_mh.addEventListener('input', function (){summa_mh();})
in_6_mh.addEventListener('input', function (){summa_mh();})
in_7_mh.addEventListener('input', function (){summa_mh();})
in_8_mh.addEventListener('input', function (){summa_mh();})
in_9_mh.addEventListener('input', function (){summa_mh();})
in_10_mh.addEventListener('input', function (){summa_mh();})



function calculated_mr(summa_mmo){
    in_0_mr.value=Number(in_0_mmo.value)/Number(summa_mmo) * 100;
    in_1_mr.value=Number(in_1_mmo.value)/Number(summa_mmo) * 100;
    in_2_mr.value=Number(in_2_mmo.value)/Number(summa_mmo) * 100;
    in_3_mr.value=Number(in_3_mmo.value)/Number(summa_mmo) * 100;
    in_4_mr.value=Number(in_4_mmo.value)/Number(summa_mmo) * 100;
    in_5_mr.value=Number(in_5_mmo.value)/Number(summa_mmo) * 100;
    in_6_mr.value=Number(in_6_mmo.value)/Number(summa_mmo) * 100;
    in_7_mr.value=Number(in_7_mmo.value)/Number(summa_mmo) * 100;
    in_8_mr.value=Number(in_8_mmo.value)/Number(summa_mmo) * 100;
    in_9_mr.value=Number(in_9_mmo.value)/Number(summa_mmo) * 100;
    in_10_mr.value=Number(in_10_mmo.value)/Number(summa_mmo) * 100;
    in_11_mr.value=Number(in_0_mr.value) + Number(in_1_mr.value) + Number(in_2_mr.value) + Number(in_3_mr.value) + Number(in_4_mr.value) + Number(in_5_mr.value) + Number(in_6_mr.value) + Number(in_7_mr.value) + Number(in_8_mr.value) + Number(in_9_mr.value) + Number(in_10_mr.value);

}

function summa_msk(){
    in_11_msk.value = Number(in_0_msk.value) + Number(in_1_msk.value) + Number(in_2_msk.value) + Number(in_3_msk.value) + Number(in_4_msk.value) + Number(in_5_msk.value) + Number(in_6_msk.value) + Number(in_7_msk.value) + Number(in_8_msk.value) + Number(in_9_msk.value) + Number(in_10_msk.value);
    return in_11_msk.value
}
function summa_mmk(){
    in_11_mmk.value = Number(in_0_mmk.value) + Number(in_1_mmk.value) + Number(in_2_mmk.value) + Number(in_3_mmk.value) + Number(in_4_mmk.value) + Number(in_5_mmk.value) + Number(in_6_mmk.value) + Number(in_7_mmk.value) + Number(in_8_mmk.value) + Number(in_9_mmk.value) + Number(in_10_mmk.value);
    return in_11_mmk.value
}
function summa_mmo(){
    in_0_mmo.value = (Number(in_0_msk.value) * Number(in_0_mmk.value))/100;
    in_1_mmo.value = (Number(in_1_msk.value) * Number(in_1_mmk.value))/100;
    in_2_mmo.value = (Number(in_2_msk.value) * Number(in_2_mmk.value))/100;
    in_3_mmo.value = (Number(in_3_msk.value) * Number(in_3_mmk.value))/100;
    in_4_mmo.value = (Number(in_4_msk.value) * Number(in_4_mmk.value))/100;
    in_5_mmo.value = (Number(in_5_msk.value) * Number(in_5_mmk.value))/100;
    in_6_mmo.value = (Number(in_6_msk.value) * Number(in_6_mmk.value))/100;
    in_7_mmo.value = (Number(in_7_msk.value) * Number(in_7_mmk.value))/100;
    in_8_mmo.value = (Number(in_8_msk.value) * Number(in_8_mmk.value))/100;
    in_9_mmo.value = (Number(in_9_msk.value) * Number(in_9_mmk.value))/100;
    in_10_mmo.value = (Number(in_10_msk.value) * Number(in_10_mmk.value))/100;
    in_11_mmo.value = Number(in_0_mmo.value) + Number(in_1_mmo.value) + Number(in_2_mmo.value) + Number(in_3_mmo.value) + Number(in_4_mmo.value) + Number(in_5_mmo.value) + Number(in_6_mmo.value) + Number(in_7_mmo.value) + Number(in_8_mmo.value) + Number(in_9_mmo.value) + Number(in_10_mmo.value);
    return in_11_mmo.value
}
function summa_mh(){
    in_11_mh.value = Number(in_0_mh.value) + Number(in_1_mh.value) + Number(in_2_mh.value) + Number(in_3_mh.value) + Number(in_4_mh.value) + Number(in_5_mh.value) + Number(in_6_mh.value) + Number(in_7_mh.value) + Number(in_8_mh.value) + Number(in_9_mh.value) + Number(in_10_mh.value);
    return in_11_mh.value
}